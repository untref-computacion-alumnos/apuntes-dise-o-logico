---
title: "Memoria"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Memoria

```{admonition} Sobre este apunte
:class: note
La noción de ROM como plano AND-OR retoma brevemente lo visto en
[Implementación](10-implementacion.md), a partir de la presentación *Síntesis Lógica*
(Prof. Dr. Martín Vázquez, Diseño Lógico) — acá el enfoque cambia: en lugar de la ROM como técnica
de síntesis de funciones lógicas, se la trata como **dispositivo de almacenamiento**. El resto del
capítulo (RAM, taxonomía de ROM, organización y jerarquía de memoria) es contenido de bibliografía
estándar de la materia {cite}`tocci2007`, {cite}`harris2012` y {cite}`mandado1998`.
```

## 1. Concepto general de memoria digital

Una **memoria** digital almacena $2^n$ palabras de $m$ bits cada una. Cada palabra se identifica
mediante una **dirección** de $n$ bits, y el acceso a una palabra particular se resuelve
internamente con un **decodificador** de $n$ líneas de entrada y $2^n$ salidas (ver
[Codificadores y decodificadores](14-codificadores-y-decodificadores.md)): la salida activada por el
decodificador selecciona la fila de memoria correspondiente a la dirección solicitada.

```text
                    ┌───────────┐
  dirección (n) ───►│  Memoria  │
                    │ 2^n × m   │◄── control (lectura/escritura, chip select)
                    └─────┬─────┘
                          │
                     dato (m) ←→
```

## 2. Clasificación: RAM vs. ROM

| | RAM | ROM |
|---|---|---|
| Operaciones | Lectura **y** escritura | Solo lectura (en operación normal) |
| Volatilidad | Volátil (pierde el contenido sin alimentación) | No volátil (retiene el contenido sin alimentación) |
| Uso típico | Memoria de trabajo, registros de datos | Firmware, tablas de constantes, síntesis lógica (capítulo 10) |

```{note}
Históricamente "RAM" significa *Random Access Memory* (memoria de acceso aleatorio), en oposición a
memorias de acceso secuencial como una cinta magnética. Estrictamente, una ROM también es de acceso
aleatorio. En la práctica, sin embargo, "RAM" se usa como sinónimo de "memoria de lectura/escritura
volátil" y "ROM" como sinónimo de "memoria de solo lectura no volátil", que es el sentido que se
usa en este apunte.
```

## 3. Memorias de lectura/escritura (RAM)

### 3.1 SRAM

La **SRAM** (*Static RAM*) almacena cada bit en un **biestable** (ver
[Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md)): mientras haya
alimentación, el bit se mantiene indefinidamente sin necesidad de ninguna acción adicional. Es
rápida, pero cada celda requiere varios transistores, por lo que es menos densa y más cara.
Se usa típicamente en **memorias caché**, donde la velocidad es crítica.

### 3.2 DRAM

La **DRAM** (*Dynamic RAM*) almacena cada bit como carga eléctrica en un capacitor, accedido por un
único transistor. Esto la hace mucho más densa y económica que la SRAM, pero la carga se fuga con el
tiempo, por lo que requiere un **refresco periódico** (releer y reescribir cada celda antes de que
pierda su valor). Es más lenta que la SRAM (por el refresco y por los amplificadores de detección
necesarios para leer una carga muy pequeña), y es la tecnología dominante para la **memoria
principal** de una computadora.

### 3.3 Comparación

| Aspecto | SRAM | DRAM |
|---|---|---|
| Celda | Biestable (varios transistores) | 1 transistor + 1 capacitor |
| Velocidad | Alta | Media/baja (requiere refresco) |
| Densidad | Baja | Alta |
| Costo por bit | Alto | Bajo |
| Refresco | No necesita | Sí, periódico |
| Uso típico | Caché | Memoria principal (RAM del sistema) |

## 4. Memorias de solo lectura (ROM)

### 4.1 ROM como plano AND-OR

Una ROM puede describirse como un dispositivo **totalmente cableado**: un decodificador fijo
(el "plano AND", que genera cada línea de palabra a partir de la dirección) conectado a un plano OR
programable (el contenido de cada palabra). Este esquema, junto con un ejemplo completo de ROM de
4 palabras de 4 bits, se desarrolla en detalle en [Implementación](10-implementacion.md), en el
contexto de la síntesis de funciones lógicas. Acá interesa la ROM como **dispositivo de
almacenamiento de datos o programas**, no como técnica de síntesis: la misma estructura interna
sirve para guardar, por ejemplo, el firmware de arranque de un sistema embebido.

### 4.2 Taxonomía de ROM

| Tipo | Programación | Borrado | Uso típico |
|---|---|---|---|
| ROM de máscara | En fábrica (durante la fabricación del chip) | No se puede borrar/reprogramar | Producción masiva, costo unitario mínimo |
| PROM | Una única vez, por el usuario (quema de fusibles) | No se puede borrar | Prototipos, series pequeñas |
| EPROM | Eléctricamente, por el usuario | Con luz ultravioleta (ventana de cuarzo), borrado total | Desarrollo, reprogramación ocasional |
| EEPROM | Eléctricamente, por el usuario | Eléctricamente, a nivel de byte | Configuración persistente, calibración |
| Flash | Eléctricamente, por el usuario | Eléctricamente, por bloques | Almacenamiento masivo (pendrives, SSD), memoria de programa de microcontroladores |

```{tip}
La memoria Flash es, en esencia, una evolución de la EEPROM optimizada para borrar bloques enteros
en lugar de bytes individuales, lo que permite una densidad mucho mayor y es la razón por la que
domina hoy el almacenamiento no volátil de estado sólido.
```

## 5. Organización y direccionamiento

### 5.1 Palabra vs. bit

Una memoria se especifica por su **organización**: cantidad de palabras × bits por palabra. Por
ejemplo, una memoria "1K × 8" tiene $1024 = 2^{10}$ palabras de 8 bits, por lo que necesita 10
líneas de dirección y 8 líneas de datos.

### 5.2 Ampliación de memorias

Cuando un único chip de memoria no alcanza, se combinan varios:

- **Más palabras** (mayor profundidad): se agregan líneas de dirección adicionales y un
  decodificador externo que selecciona (mediante la señal de *chip select*) cuál de los chips
  responde a cada rango de direcciones.
- **Más bits por palabra** (mayor ancho): se colocan varios chips **en paralelo**, todos
  recibiendo las mismas líneas de dirección y control, aportando cada uno una porción del bus de
  datos total.

```{exercise}
:label: ex-memoria-5
Se dispone de chips de memoria de 1K × 8 bits. Diseñar la organización necesaria para construir una
memoria de 4K × 16 bits.
```

```{solution} ex-memoria-5
:class: dropdown
Para 16 bits de ancho por palabra se necesitan 2 chips en paralelo (2 × 8 = 16 bits), compartiendo
dirección y control. Para 4K de profundidad ($4096 = 4 \times 1024$) se necesitan 4 grupos de esos
2 chips (8 chips en total), seleccionados por un decodificador de 2 a 4 que usa los 2 bits más
significativos de la dirección de 12 bits (ya que $4096=2^{12}$, y cada chip cubre $2^{10}$
direcciones, sobran 2 bits para elegir entre los 4 grupos).
```

## 6. Jerarquía de memoria

Ninguna tecnología de memoria es simultáneamente la más rápida, la más densa y la más barata; por
eso los sistemas de cómputo combinan varios niveles, cada uno haciendo de "caché" del siguiente:

$$\text{Registros} \;\to\; \text{Caché (SRAM)} \;\to\; \text{Memoria principal (DRAM)} \;\to\; \text{Almacenamiento secundario (disco, Flash)}$$

A medida que se desciende en esta cadena, la capacidad aumenta y el costo por bit disminuye, pero
también aumenta el tiempo de acceso. El diseño detallado de esta jerarquía es tema de **Arquitectura
de Computadoras**; acá solo interesa notar que los bloques vistos en este apunte (biestables para
SRAM, registros del [capítulo 20](20-registros.md), decodificadores de dirección) son los
componentes de diseño lógico con los que se construye cada uno de esos niveles.

## 7. Resumen

- Toda memoria se organiza como $2^n$ palabras de $m$ bits, direccionadas mediante un decodificador.
- RAM (lectura/escritura, volátil) se distingue de ROM (solo lectura, no volátil); dentro de la RAM,
  la SRAM (biestables, rápida, cara) se distingue de la DRAM (capacitor + refresco, densa, barata).
- Existe una taxonoma de ROM según cómo se programa y se borra: máscara, PROM, EPROM, EEPROM y
  Flash, en orden creciente de flexibilidad de reprogramación.
- Las memorias se amplían agregando líneas de dirección con un decodificador externo (más
  profundidad) o poniendo chips en paralelo (más ancho de palabra).
- La jerarquía de memoria combina varias tecnologías para balancear velocidad, capacidad y costo.

## 8. Ejercicios propuestos

```{exercise}
:label: ex-memoria-1
Explicar por qué una DRAM necesita refresco periódico y una SRAM no.
```

```{solution} ex-memoria-1
:class: dropdown
La DRAM almacena cada bit como carga eléctrica en un capacitor, que se descarga naturalmente con el
tiempo (corrientes de fuga); si no se relee y reescribe periódicamente, el dato se pierde. La SRAM
almacena cada bit en un biestable realimentado (dos inversores cruzados) que se sostiene a sí mismo
mientras haya alimentación, sin necesidad de refresco.
```

```{exercise}
:label: ex-memoria-2
Un microcontrolador debe almacenar su firmware, que se actualiza ocasionalmente por el fabricante
mediante un programador externo, sin necesidad de exponer una ventana de cuarzo. ¿Qué tipo de ROM
de la sección 4.2 es más adecuada?
```

```{solution} ex-memoria-2
:class: dropdown
Una **EEPROM** (o, más comúnmente hoy, una memoria **Flash**): permite reprogramación eléctrica sin
exposición a luz ultravioleta (a diferencia de la EPROM) y sin quedar fijada de fábrica (a
diferencia de la ROM de máscara o la PROM).
```

```{exercise}
:label: ex-memoria-3
¿Cuántas líneas de dirección necesita una memoria de 64K palabras? ¿Y si la memoria fuera de 256K
palabras?
```

```{solution} ex-memoria-3
:class: dropdown
$64K = 2^{16}$ palabras → 16 líneas de dirección. $256K = 2^{18}$ palabras → 18 líneas de dirección.
```

```{exercise}
:label: ex-memoria-4
Relacionar la ROM como "plano AND-OR" (capítulo 10) con la ROM como dispositivo de almacenamiento
de este capítulo: ¿qué cambia y qué se mantiene igual?
```

```{solution} ex-memoria-4
:class: dropdown
La estructura interna es la misma en ambos casos: un decodificador fijo (plano AND) selecciona una
palabra, y un plano OR programable define el contenido de esa palabra. Lo que cambia es la
**interpretación** de ese contenido: en el capítulo 10, cada palabra representa el valor de una
función lógica para una combinación de entradas (la ROM se usa como tabla de verdad cableada); en
este capítulo, cada palabra es simplemente un dato o una instrucción almacenada (la ROM se usa como
memoria de propósito general, por ejemplo para guardar firmware).
```

## 9. Bibliografía

```{bibliography}
:filter: docname in docnames
```
