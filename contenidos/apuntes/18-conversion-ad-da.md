---
title: "Conversión A/D, D/A"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Conversión A/D, D/A

```{admonition} Sobre este apunte
:class: note
Este tema no está desarrollado en las presentaciones de la cátedra. Se completa íntegramente con
el tratamiento estándar de bibliografía de Diseño Lógico y Sistemas Digitales
{cite}`tocci2007,floyd2000,harris2012`, manteniendo la notación y el estilo del resto del apunte.
```

## 1. Introducción

El mundo físico —temperatura, sonido, posición, tensión— es, en general, **analógico**: varía en
forma continua. Los sistemas digitales, en cambio, procesan únicamente valores discretos (0 y 1).
Para que un sistema digital pueda leer un sensor o controlar un actuador analógico, se necesitan
circuitos que traduzcan entre ambos mundos:

- **ADC** (*Analog-to-Digital Converter*, conversor A/D): traduce una tensión analógica a un
  código digital.
- **DAC** (*Digital-to-Analog Converter*, conversor D/A): traduce un código digital a una tensión
  analógica.

```text
  Sensor          ┌─────┐          Sistema
 (analógico) ────►│ ADC ├────────► digital
                   └─────┘

  Sistema          ┌─────┐         Actuador
  digital  ───────►│ DAC ├────────►(analógico)
                   └─────┘
```

## 2. Conversión digital-analógica (DAC)

### 2.1 Red de resistores ponderados binariamente

La técnica más directa para construir un DAC es sumar corrientes ponderadas según el peso binario
de cada bit de entrada, usando una resistencia distinta para cada bit:

```text
  b3 ──[R]────┐
  b2 ──[2R]───┤
  b1 ──[4R]───┼──► sumador de corriente ──► V_out (analógica)
  b0 ──[8R]───┘
```

Cada bit $b_i$ que está en 1 aporta una corriente proporcional a $1/(2^i R)$; la salida analógica
resulta proporcional al valor decimal representado por la palabra binaria de entrada. El problema
práctico de este esquema es que requiere resistencias de valores muy dispares (y por lo tanto
difíciles de fabricar con precisión) cuando crece la cantidad de bits.

### 2.2 Red R-2R

La **red R-2R** resuelve ese problema: usa únicamente dos valores de resistencia ($R$ y $2R$)
combinados en una topología en escalera, logrando el mismo efecto de ponderación binaria sin
necesitar resistores de valores extremos. Es la técnica más usada en DACs integrados
{cite}`tocci2007`.

### 2.3 Resolución

La **resolución** de un DAC es el menor cambio de tensión que puede producir, correspondiente al
bit menos significativo (LSB):

$$\text{LSB} = \frac{V_{FS}}{2^n - 1}$$

donde $V_{FS}$ es la tensión de fondo de escala (*full scale*) y $n$ la cantidad de bits.

```{note}
**Ejemplo**: un DAC de $n=4$ bits con $V_{FS}=10\ \text{V}$ tiene
$\text{LSB} = 10/(2^4-1) = 10/15 \approx 0{,}667\ \text{V}$. La entrada $1010$ (10 en decimal)
produce una salida aproximada de $10 \times 0{,}667 \approx 6{,}67\ \text{V}$.
```

Cuantos más bits tiene el DAC, más fina es la resolución (menor es el escalón entre valores
consecutivos), a costa de un circuito más complejo.

## 3. Conversión analógica-digital (ADC)

El bloque elemental de cualquier ADC es el **comparador** (ver
[Sumadores, restadores y comparadores](16-sumadores-restadores-y-comparadores.md) para el
comparador digital; acá se trata de un comparador analógico, que compara una tensión de entrada
contra una tensión de referencia y produce una salida digital 0/1 según cuál sea mayor).

### 3.1 ADC flash (paralelo)

El ADC **flash** compara la tensión de entrada simultáneamente contra $2^n - 1$ niveles de
referencia, usando $2^n - 1$ comparadores en paralelo, y codifica el resultado con un
codificador de prioridad (ver
[Codificadores y decodificadores](14-codificadores-y-decodificadores.md)):

```text
 V_in ──┬──────────────────────────────┐
        │                              │
        ▼                              ▼
   [Comparador 1]  ...  [Comparador (2^n - 1)]
        │                              │
        └──────────► Codificador ──────┘
                     de prioridad
                          │
                          ▼
                    código digital (n bits)
```

Es el ADC más **rápido** posible (una sola comparación simultánea), pero también el más **costoso**
en cantidad de compuertas: para $n$ bits de salida necesita $2^n-1$ comparadores, lo que lo hace
poco práctico para resoluciones altas.

### 3.2 ADC de aproximaciones sucesivas (SAR)

El ADC de **aproximaciones sucesivas** (*Successive Approximation Register*, SAR) es un buen
compromiso entre velocidad y costo: usa un único comparador, un DAC interno y un registro que va
"adivinando" el resultado bit a bit, del más al menos significativo.

Algoritmo (para $n$ bits):

```{mermaid}
flowchart TD
    A["Poner el bit más significativo\naún no definido en 1"] --> B["Convertir el registro\ncon el DAC interno"]
    B --> C{"¿V_DAC > V_in?"}
    C -->|Sí| D["Volver ese bit a 0"]
    C -->|No| E["Dejar ese bit en 1"]
    D --> F{"¿Quedan bits\npor definir?"}
    E --> F
    F -->|Sí| A
    F -->|No| G["Registro = resultado final"]
```

Cada bit se decide con una sola comparación, por lo que una conversión de $n$ bits tarda $n$
ciclos de comparación: mucho más rápido que probar las $2^n$ combinaciones una por una, y mucho
más económico en compuertas que el ADC flash.

### 3.3 ADC de rampa/contador

Una variante más simple (y más lenta) usa un **contador** (ver
[Circuitos contadores](19-circuitos-contadores.md)) que incrementa su valor paso a paso; en cada
paso, su salida se convierte a analógico con un DAC interno y se compara contra $V_{in}$. Cuando
la salida del DAC supera a $V_{in}$, el valor del contador en ese instante es el resultado de la
conversión. Es simple de implementar pero, en el peor caso, requiere hasta $2^n$ pasos.

## 4. Muestreo y cuantización

Para digitalizar una señal analógica que varía en el tiempo (por ejemplo, audio) no alcanza con
convertir un único valor: hay que **muestrear** la señal a intervalos regulares y convertir cada
muestra por separado.

- **Frecuencia de muestreo** ($f_s$): cantidad de muestras tomadas por segundo.
- **Teorema de muestreo (Nyquist-Shannon)**: para poder reconstruir sin ambigüedad una señal cuya
  componente de frecuencia más alta es $f_{max}$, la frecuencia de muestreo debe cumplir
  $f_s > 2 f_{max}$ {cite}`harris2012`. Muestrear por debajo de ese límite produce **aliasing**
  (distorsión irreversible de la señal reconstruida).
- **Error de cuantización**: como el ADC solo puede representar $2^n$ niveles discretos, cada
  muestra se redondea al nivel más cercano, introduciendo un pequeño error que disminuye a medida
  que aumenta la cantidad de bits $n$.

```{tip}
Cuantos más bits tenga el ADC, menor es el error de cuantización (mayor fidelidad), y cuanto mayor
es la frecuencia de muestreo, mejor se capturan los detalles rápidos de la señal. Ambos parámetros
—resolución en bits y frecuencia de muestreo— determinan juntos la calidad de una conversión A/D
(es, por ejemplo, la razón por la que el audio de un CD se especifica como "44.1 kHz, 16 bits").
```

## 5. Resumen

- El **DAC** convierte un código digital en una tensión analógica proporcional; la red R-2R es la
  técnica más usada en la práctica frente a la red de resistores ponderados.
- La **resolución** de un DAC (el LSB) mejora cuantos más bits tiene.
- El **ADC** convierte una tensión analógica en un código digital, usando comparadores como bloque
  elemental. El **ADC flash** es el más rápido pero el más costoso ($2^n-1$ comparadores); el
  **ADC de aproximaciones sucesivas (SAR)** es el compromiso más usado en la práctica; el ADC de
  rampa/contador es el más simple pero el más lento.
- **Muestrear** una señal continua requiere respetar el **teorema de Nyquist** ($f_s > 2f_{max}$)
  para evitar aliasing; la **cuantización** introduce un error inevitable que se reduce aumentando
  la cantidad de bits del conversor.

## 6. Bibliografía

```{bibliography}
:filter: docname in docnames
```

## 7. Ejercicios propuestos

```{exercise}
:label: ex-adda-1
Calcular la resolución (LSB) de un DAC de 8 bits con $V_{FS}=5\ \text{V}$.
```

```{solution} ex-adda-1
:class: dropdown
$$\text{LSB} = \frac{5}{2^8-1} = \frac{5}{255} \approx 0{,}0196\ \text{V} \approx 19{,}6\ \text{mV}$$
```

```{exercise}
:label: ex-adda-2
¿Cuántos comparadores necesita un ADC flash de 6 bits? ¿Y cuántos ciclos de comparación necesita,
en el peor caso, un ADC SAR de 6 bits?
```

```{solution} ex-adda-2
:class: dropdown
El ADC flash necesita $2^6-1=63$ comparadores (una sola comparación simultánea, muy rápido pero
muy costoso). El ADC SAR necesita exactamente 6 ciclos de comparación (uno por cada bit, del más
al menos significativo), sin importar cuál sea el valor de entrada.
```

```{exercise}
:label: ex-adda-3
Una señal de audio tiene componentes de frecuencia de hasta 20 kHz. ¿Cuál es la frecuencia de
muestreo mínima teórica según Nyquist? ¿Por qué el estándar de audio de CD usa 44,1 kHz y no
exactamente el doble de 20 kHz?
```

```{solution} ex-adda-3
:class: dropdown
Nyquist exige $f_s > 2 \times 20\,\text{kHz} = 40\,\text{kHz}$. El estándar usa 44,1 kHz para dejar
un margen de guarda por encima del mínimo teórico, ya que los filtros analógicos reales (filtros
anti-aliasing) no cortan de forma perfectamente abrupta en 20 kHz.
```
