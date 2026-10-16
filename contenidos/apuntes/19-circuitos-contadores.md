---
title: "Circuitos Contadores"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Circuitos Contadores

```{admonition} Sobre este apunte
:class: note
Este apunte desarrolla la sección "Contadores" de la presentación *Circuitos Secuenciales II*
(Lucas Leiva, Diseño Lógico 2024). Se completa con bibliografía estándar de la materia
{cite}`tocci2007` y {cite}`floyd2000` para las secciones de organización general y comparación de
arquitecturas. Se asume conocido el contenido de
[Circuitos secuenciales asincrónicos y sincrónicos](17-circuitos-secuenciales-asincronicos-y-sincronicos.md)
(biestables, flip-flops T/JK/D, tiempos de setup/hold).
```

## 1. Definición y clasificación

Un **contador** es un circuito secuencial cuyo conjunto de estados recorre una **secuencia de
valores que se repite** (un invariante): al llegar al último valor de la secuencia, vuelve a
comenzar. La secuencia más simple y más usada es el conteo binario natural.

| Ciclo | $S_3$ | $S_2$ | $S_1$ | $S_0$ | Decimal |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 2 | 0 | 0 | 1 | 0 | 2 |
| 3 | 0 | 0 | 1 | 1 | 3 |
| 4 | 0 | 1 | 0 | 0 | 4 |
| 5 | 0 | 1 | 0 | 1 | 5 |
| 6 | 0 | 1 | 1 | 0 | 6 |
| 7 | 0 | 1 | 1 | 1 | 7 |
| 8 | 1 | 0 | 0 | 0 | 8 |
| 9 | 1 | 0 | 0 | 1 | 9 |
| ... | | | | | ... hasta 15, y vuelve a 0000 |

Existen **dos maneras de analizar** cómo se genera esta secuencia, y cada una conduce a una
arquitectura de contador distinta:

- **Desde el evento**: se observa, bit a bit, *cuándo* cambia cada señal → conduce al **contador
  asincrónico**.
- **Desde el estado**: se observa, bit a bit, *bajo qué condición* cambia cada señal en cada flanco
  de reloj → conduce al **contador sincrónico**.

## 2. Contador asincrónico

### 2.1 Análisis bit a bit (por evento)

Mirando la tabla anterior columna por columna:

- $S_0$ cambia de valor **en cada ciclo de reloj**: es un flip-flop tipo T con $T=1$ permanente,
  conmutado directamente por el reloj.
- $S_1$ cambia únicamente en la transición de $S_0$ de $1$ a $0$ (flanco descendente de $S_0$, o
  equivalentemente flanco ascendente de $S_0'$).
- $S_2$ cambia en la transición de $S_1$ de $1$ a $0$ (flanco descendente de $S_1$).
- $S_3$ cambia en la transición de $S_2$ de $1$ a $0$ (flanco descendente de $S_2$).

En general, el bit $S_i$ cambia en el flanco descendente de $S_{i-1}$.

### 2.2 Implementación con flip-flops T

Cada bit se implementa con un flip-flop T con $T=1$ fijo (es decir, conmuta en cada flanco activo
de su entrada de reloj), y cada etapa se **encadena** usando la salida de la etapa anterior como
reloj de la siguiente:

```text
            T=1          T=1          T=1          T=1
             │            │            │            │
          ┌──▼──┐      ┌──▼──┐      ┌──▼──┐      ┌──▼──┐
   clk ──►│ T Q │─ S0 ─►│ T Q │─ S1 ─►│ T Q │─ S2 ─►│ T Q │─ S3
          └─────┘      └─────┘      └─────┘      └─────┘
```

Cada flip-flop conmuta en el flanco descendente de la señal que recibe en su entrada de reloj
(la salida de la etapa anterior), reproduciendo exactamente la condición de cambio detectada en el
análisis bit a bit.

### 2.3 Por qué es "asincrónico"

Se denomina **asincrónico** (o *ripple counter*, contador en cascada) porque **los elementos de
memoria no se actualizan todos en el mismo instante**: cada etapa dispara a la siguiente con el
retardo de propagación $t_p$ propio del flip-flop anterior. El siguiente cronograma (3 bits) lo
muestra:

```text
clk  0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1
S0   0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1
S1   0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1
S2   0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1
```

```{important}
Entre el flanco de reloj y la actualización del bit $S_i$ transcurre un retardo acumulado de
$i \cdot t_p$ (la suma de los $t_p$ de todas las etapas anteriores). A medida que aumenta la
cantidad de bits del contador, este retardo total **crece linealmente**, lo que limita la
frecuencia máxima de reloj admisible: por un instante, mientras el "carry" se propaga etapa por
etapa, el contador puede mostrar valores intermedios inválidos (glitches) antes de estabilizarse.
```

## 3. Contador sincrónico

### 3.1 Análisis por estado (caso 2)

La alternativa es preguntar, para cada bit, **bajo qué condición** debe cambiar en el **mismo**
flanco de reloj que todos los demás:

- $S_0$ cambia en cada ciclo de reloj: $T_0 = 1$.
- $S_1$ cambia en el flanco de reloj únicamente si $S_0=1$: $T_1 = S_0$.
- $S_2$ cambia en el flanco de reloj únicamente si $S_1=1$ y $S_0=1$: $T_2 = S_1 \cdot S_0$.
- $S_3$ cambia en el flanco de reloj únicamente si $S_2=S_1=S_0=1$: $T_3 = S_2 \cdot S_1 \cdot S_0$.

$$T_0 = 1 \qquad T_1 = S_0 \qquad T_2 = S_0 \cdot S_1 \qquad T_3 = S_0 \cdot S_1 \cdot S_2$$

### 3.2 Implementación

Todos los flip-flops comparten la **misma** señal de reloj; lo que cambia entre etapas es la
lógica combinacional (compuertas AND) que genera la entrada $T$ de cada una:

```text
                T0=1        T1=S0      T2=S0·S1    T3=S0·S1·S2
                 │            │            │            │
              ┌──▼──┐      ┌──▼──┐      ┌──▼──┐      ┌──▼──┐
       ┌─────►│ T Q │─S0─┬►│ T Q │─S1─┬►│ T Q │─S2─┬►│ T Q │─S3
       │      └─────┘    │ └─────┘    │ └─────┘    │ └─────┘
  clk ─┴─────────────────┴────────────┴────────────┘
                          [AND2]       [AND3]
```

Se denomina **sincrónico** porque las salidas de todos los elementos de memoria se actualizan **en
el mismo instante de tiempo**, sin la cascada de retardos del caso asincrónico.

### 3.3 Comparación

| Aspecto | Asincrónico (ripple) | Sincrónico |
|---|---|---|
| Señal de reloj | Cada etapa usa la salida de la anterior | Todas las etapas comparten el mismo reloj |
| Estabilidad de salidas | Puede mostrar valores intermedios transitorios | Salidas estables, sin retardos acumulados |
| Retardo total | Crece linealmente con la cantidad de bits | Constante (un único $t_p$ de flip-flop) |
| Costo (compuertas) | Mínimo (sin compuertas AND adicionales) | Crece con la cantidad de bits (una AND de $i$ entradas por etapa $i$) |
| Frecuencia máxima | Menor a medida que crece el contador | Mayor, prácticamente independiente del ancho |

## 4. Divisor de frecuencia

Como cada bit de un contador binario cambia a la mitad de la frecuencia del bit anterior, un
contador puede usarse como **divisor de frecuencia**: cada salida sucesiva divide por 2 la
frecuencia de la anterior.

| Señal | Frecuencia | Período |
|---|---:|---:|
| clk | 100 MHz | 10 ns |
| $S_0$ | 50 MHz | 20 ns |
| $S_1$ | 25 MHz | 40 ns |
| $S_2$ | 12.5 MHz | 80 ns |

```{tip}
Esta propiedad permite combinar, dentro de un mismo sistema digital, subsistemas que operan a
distintas frecuencias de reloj derivadas todas de un único oscilador de referencia.
```

## 5. Otras arquitecturas de contadores

### 5.1 Contador basado en registro y sumador

Un contador puede modelarse de forma más abstracta como un **registro con realimentación** a
través de un sumador que incrementa en 1 el valor almacenado en cada ciclo de reloj:

```text
        ┌─────────────┐
   ┌───►│  Adder (+1) ├───┐
   │    └─────────────┘   │
   │                       ▼
   │                 ┌───────────┐
   └─────────────────┤  Reg (n)  ├──► salida (cuenta actual)
              clk ──►└───────────┘
```

```{important}
Como la nueva salida del registro depende combinacionalmente de su propio valor anterior (a través
del sumador), este es exactamente el patrón de $R_i = F(R_i)$ que en
[Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md) y en
[Registros](20-registros.md) se señala como un caso en el que **es obligatorio** usar flip-flops
(no latches) para el registro: con latches, la transparencia del elemento de memoria combinada con
el camino combinacional del sumador haría que el valor "corra" de forma descontrolada dentro de un
mismo nivel de reloj.
```

### 5.2 Contador ascendente/descendente

Si el bloque combinacional es un **sumador/restador** controlado por una señal `dec`, el mismo
registro puede contar hacia arriba o hacia abajo:

```text
        ┌───────────────┐
   ┌───►│  Adder/Sub ±1 │◄── dec
   │    └───────────────┘
   │            │
   │            ▼
   │      ┌───────────┐
   └──────┤  Reg (n)  ├──► salida
    clk ─►└───────────┘
```

### 5.3 Contador módulo n

Un **contador módulo $n$** cuenta desde $0$ hasta $n-1$ y, al alcanzar el valor $n$ (o $n-1$ según
la convención), se **resetea**. Se implementa agregando un comparador que detecta el valor límite:

```text
        ┌─────────────┐
   ┌───►│ Contador +1 ├───┬──► salida
   │    └─────────────┘   │
   │           ▲          │
   │          clk         ▼
   │                 ┌───────────┐
   └─────────────────┤ CMP (=n)  │
        reset         └───────────┘
```

```{note}
¿El reset debe ser síncrono o asíncrono? Un reset **asíncrono** actúa de inmediato al detectar el
valor límite, sin esperar al flanco de reloj, lo que puede generar un estado transitorio espurio
(riesgo de "glitch") y en general se lo reserva para la inicialización del sistema. Un reset
**síncrono** espera al próximo flanco de reloj para tomar efecto: es más prolijo desde el punto de
vista temporal (todos los cambios de estado ocurren en flancos de reloj), aunque requiere que el
valor límite se sostenga hasta ese flanco. En diseño sincrónico moderno se prefiere, salvo para la
inicialización general del sistema, el reset síncrono.
```

## 6. Contador de programa

El **contador de programa** (*Program Counter*, PC) es un elemento secuencial presente en todas las
arquitecturas de computadoras: mantiene la dirección de la próxima instrucción a ejecutar y ofrece
la posibilidad de realizar saltos:

```text
                    ┌─────────┐
    0 ────┐         │         │
          ├─[MUX]──►│  Reg PC ├───┬──► addr (dirección de próxima instrucción)
jump_addr─┘   ▲      │         │  │
              │      └─────────┘  │
            jump           ▲      │
                       ┌────┴───┐ │
                       │  +1    │◄┘
                       └────────┘
```

En cada ciclo, si `jump=0` el PC se incrementa en 1 (ejecución secuencial); si `jump=1`, se carga
`jump_addr` (salto a otra instrucción). Este es un caso particular del **registro con
realimentación** de la sección 5.1, combinado con un multiplexor de dos entradas.

## 7. Resumen

- Un contador recorre una secuencia de estados que se repite; puede diseñarse analizando **el
  evento** que dispara cada bit (contador **asincrónico**, con flip-flops T encadenados) o **la
  condición de estado** que habilita el cambio de cada bit en un flanco común (contador
  **sincrónico**, con lógica AND generando cada $T_i$).
- Los contadores asincrónicos son más económicos pero acumulan retardo de propagación linealmente
  con la cantidad de bits; los sincrónicos son más rápidos y estables a costa de más compuertas.
- Un contador binario es, de manera natural, un **divisor de frecuencia**: cada bit sucesivo divide
  por 2 la frecuencia del anterior.
- Un contador también puede modelarse como un **registro realimentado a través de un sumador**
  (o sumador/restador para contadores ascendente/descendente), lo que exige el uso de flip-flops en
  el registro (ver [Registros](20-registros.md)).
- Un contador **módulo $n$** agrega un comparador que detecta el valor límite y dispara un reset,
  síncrono o asíncrono según el diseño.
- El **contador de programa** es la aplicación arquetípica de estos conceptos en arquitectura de
  computadoras.

## 8. Ejercicios propuestos

```{exercise}
:label: ex-contador-1
Diseñar, a partir de flip-flops T, un contador asincrónico módulo 6 (cuenta de 000 a 101 y vuelve a
000). Indicar qué señal adicional hace falta y cómo se genera.
```

```{solution} ex-contador-1
:class: dropdown
Se arma un contador asincrónico de 3 bits normal (módulo 8) y se agrega una compuerta AND que
detecte el estado 110 (el primer valor fuera de rango) para forzar un **reset asíncrono** de los
tres flip-flops. De esta manera la secuencia observable es 000, 001, 010, 011, 100, 101, y al llegar
brevemente a 110 el reset la lleva de inmediato a 000.
```

```{exercise}
:label: ex-contador-2
Comparar, para un contador de 8 bits, el retardo total en el peor caso de la versión asincrónica
contra la versión sincrónica, sabiendo que $t_p$ de cada flip-flop es 3 ns y que cada compuerta AND
adicional de la versión sincrónica agrega 1 ns.
```

```{solution} ex-contador-2
:class: dropdown
Asincrónico: en el peor caso (por ejemplo, al pasar de 01111111 a 10000000) el acarreo debe
propagarse por las 8 etapas, con un retardo total de $8 \times 3\text{ns} = 24\text{ns}$.
Sincrónico: todas las etapas cambian en el mismo flanco; el camino más largo es el de la compuerta
AND de 7 entradas que genera $T_7$, con un retardo total de $3\text{ns} + 1\text{ns} = 4\text{ns}$
(el $t_p$ del flip-flop más el retardo de la lógica combinacional de entrada). El sincrónico resulta
seis veces más rápido en este ejemplo.
```

```{exercise}
:label: ex-contador-3
Diseñar, combinando contadores módulo $n$, un reloj digital que recorra las horas, minutos y
segundos de 00:00:00 a 23:59:59.
```

```{solution} ex-contador-3
:class: dropdown
Se encadenan tres contadores módulo $n$ (sección 5.3): uno módulo 60 para los segundos, uno módulo
60 para los minutos y uno módulo 24 para las horas. El contador de segundos incrementa en cada
pulso de 1 Hz; cada vez que el contador de segundos alcanza 59 y recibe un nuevo pulso (su condición
de "fin de cuenta"), habilita —a modo de acarreo— un pulso de incremento para el contador de
minutos, y de la misma forma el contador de minutos habilita al de horas al llegar a 59. Es la misma
idea que un contador módulo $n$ de la sección 5.3, pero usando la señal de reset/recarga de una
etapa como habilitación de conteo de la siguiente.
```

```{exercise}
:label: ex-contador-4
¿Por qué un contador de programa (PC) no puede implementarse con latches en lugar de flip-flops?
Relacionar con el capítulo de registros.
```

```{solution} ex-contador-4
:class: dropdown
El PC es un registro realimentado a través de un sumador (+1) y, eventualmente, un multiplexor de
salto: su próximo valor depende combinacionalmente de su valor actual. Si se implementara con
latches (transparentes durante todo el nivel activo del reloj), el nuevo valor calculado por el
sumador volvería a atravesar el latch mientras el reloj sigue activo, y el PC podría incrementarse
varias veces dentro de un mismo ciclo en lugar de exactamente una vez. Ver la discusión detallada en
[Registros](20-registros.md) y en [Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md).
```

## 9. Bibliografía

```{bibliography}
:filter: docname in docnames
```
