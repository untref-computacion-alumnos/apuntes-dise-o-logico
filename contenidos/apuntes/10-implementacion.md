---
title: "Implementación"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Implementación

```{admonition} Sobre este apunte
:class: note
Este apunte reorganiza la primera mitad de la clase de **Síntesis Lógica** (Prof. Dr. Martín
Vázquez): el contexto de materialización de sistemas digitales (niveles de abstracción,
alternativas tecnológicas) y las cinco técnicas de síntesis de circuitos combinacionales a
partir de una tabla de verdad. Los ejemplos numéricos de PLA y ROM se reconstruyeron de forma
autoconsistente a partir de los datos parciales de la presentación original, preservando la
estructura y el resultado que allí se plantean.
```

## 1. Materialización de sistemas digitales

Diseñar una función lógica en el papel (tabla de verdad, ecuación, esquema de compuertas) es
solo la mitad del problema: tarde o temprano ese diseño tiene que **materializarse** en un
dispositivo físico real. El contexto actual de esa materialización incluye:

- **Sistemas ciberfísicos (CPS)**: integración de sistemas físicos (sensores, actuadores) con
  cómputo y comunicación en red; uno de los pilares de la Industria 4.0 (domótica, producción,
  medicina, logística, energía).
- **Internet de las cosas (IoT)**: interconexión de dispositivos cotidianos a través de
  Internet, con recopilación de datos por sensores y comunicación con la nube; una herramienta
  central dentro de los sistemas CPS.
- **Sistemas embebidos**: sistemas de cómputo dedicados a un problema específico, que requieren
  **codiseño hardware/software**: diseño e implementación de hardware (desde el nivel más bajo,
  el circuito físico, hasta la adaptación de soluciones de fabricantes como microcontroladores,
  microprocesadores o FPGAs) y de software (sistema operativo, aplicación).

### 1.1 Niveles de abstracción del diseño hardware

El diseño de hardware digital se organiza en niveles de abstracción, cada uno más cercano al
dispositivo físico que el anterior:

```{mermaid}
flowchart TD
    A["Algorítmico / Funcional (HLL, HDL de alto nivel)"] --> B["Lógico (HDL, esquemáticos)"]
    B --> C["Circuito lógico (compuertas genéricas o de biblioteca)"]
    C --> D["Físico (transistor y layout)"]
```

- **Algorítmico o funcional**: descripciones de algoritmos (lenguajes de alto nivel, HLLs) o de
  comportamiento (lenguajes de descripción de hardware, HDLs — ver
  [Lenguajes de programación HDL](22-lenguajes-de-programacion-hdl.md)), simulables a alto
  nivel.
- **Lógico**: esquemáticos o HDL a nivel de compuertas, con simulación a nivel de puerta y
  análisis de tiempos.
- **Circuito lógico / esquemático**: red de puertas concretas, de biblioteca genérica o
  específica de un fabricante.
- **Físico**: nivel de transistor y de disposición geométrica (*layout*) sobre el chip.

**Síntesis** es el proceso por el cual se obtiene un diseño de un nivel de abstracción inferior
a partir de un diseño de nivel superior; puede ser manual o automática, y se la clasifica como
síntesis de alto nivel, síntesis lógica o síntesis física, según entre qué niveles opera. Este
capítulo se concentra en la **síntesis lógica**: el proceso por el que se obtiene un circuito
en términos de compuertas lógicas (de bibliotecas genéricas o específicas) a partir de una
descripción abstracta —tabla de verdad, ecuación lógica, o una descripción en VHDL o Verilog.

### 1.2 Alternativas tecnológicas

| Alternativa | Descripción | Conocimiento requerido |
|---|---|---|
| **ASIC** (*Application Specific Integrated Circuit*) | Circuito integrado diseñado a medida para una aplicación específica | Fuertemente de electrónica y de fabricación de semiconductores |
| **Dispositivos programables por el usuario** (PAL, CPLD, FPGA) | Circuitos integrados genéricos que el usuario configura después de fabricados | Principalmente de diseño lógico digital (ver [Lógica programable](23-logica-programable.md)) |
| **Circuitos impresos (PCB)** | Ensamblan circuitos integrados (estándar, específicos o programables) y componentes discretos | De electrónica, especialmente en placas multicapa y de alta frecuencia |

```{note}
La elección de tecnología es, en gran medida, un compromiso entre costo de desarrollo inicial
(*NRE*, *non-recurring engineering*), costo por unidad, velocidad, consumo y flexibilidad para
corregir o actualizar el diseño. Un ASIC tiene el mayor costo de desarrollo pero el menor costo
por unidad a gran escala; un FPGA permite reprogramar el diseño sin fabricar un nuevo chip. Ver
[Lógica programable](23-logica-programable.md) para la comparación detallada entre PAL, CPLD y
FPGA.
```

## 2. Técnicas de síntesis de circuitos combinacionales

Dada una función especificada por su tabla de verdad, existen (al menos) cinco técnicas
clásicas para sintetizarla como circuito. Todas se ilustran con la misma función de ejemplo:

$$f = x_2'x_1'x_0 + x_2'x_1x_0' + x_2x_1'x_0$$

cuya tabla de verdad es:

| $x_2$ | $x_1$ | $x_0$ | $f$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | **1** |
| 0 | 1 | 0 | **1** |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | **1** |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |

### 2.1 Compuertas AND-OR-INV

Es la síntesis "canónica" ya desarrollada en detalle en
[Formas canónicas](07-formas-canonicas.md): un nivel de compuertas AND (una por minterm, con
inversores para las variables negadas) seguido de una compuerta OR que las combina. Es la
técnica de referencia contra la que se comparan las demás.

### 2.2 Multiplexores

Se utiliza un multiplexor con tantas entradas de selección como variables tenga la función: un
$MUX_{2^n\_1}$ para $n$ variables (ver
[Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md)). Las variables de
entrada de la función se conectan a las líneas de selección, y cada una de las $2^n$ entradas
de datos del MUX se conecta a la constante 0 o 1 según el valor de $f$ en esa fila de la tabla
de verdad:

| Selección $x_2x_1x_0$ | Entrada del MUX | Valor conectado |
|:---:|:---:|:---:|
| 000 | $d_0$ | 0 |
| 001 | $d_1$ | 1 |
| 010 | $d_2$ | 1 |
| 011 | $d_3$ | 0 |
| 100 | $d_4$ | 0 |
| 101 | $d_5$ | 1 |
| 110 | $d_6$ | 0 |
| 111 | $d_7$ | 0 |

```{tip}
Esta técnica es muy directa: no requiere simplificar la función en absoluto, cualquier tabla de
verdad de $n$ variables se sintetiza con un único $MUX_{2^n\_1}$. Es, además, exactamente la
misma idea que después se usa en la síntesis mediante ROM (sección 2.4) y en las LUT de las
FPGA (sección 2.5): "cablear" la salida como una tabla de consulta indexada por las entradas.
```

### 2.3 PLA (*Programmable Logic Array*)

Un PLA combina un **plano AND** programable con un **plano OR** programable.

- **Plano AND**: una matriz de compuertas AND con hasta $n$ entradas (las variables, en forma
  normal o negada) y hasta $k$ salidas (los términos producto $p_1,\dots,p_k$).
- **Plano OR**: una matriz de compuertas OR con $k$ entradas (los términos producto) y $m$
  salidas ($s_1,\dots,s_m$), cada una suma de algunos de los términos producto.

```text
        AND                          OR
x1 ─┬──────────┐            p1 ─┬──────────┐
x2 ─┼──►[plano]├─ p1..pk    p2 ─┼──►[plano]├─ s1..sm
xn ─┘  AND     │            pk ─┘   OR     │
       └───────┘                   └───────┘
```

La programación del plano AND se codifica como una cadena de bits: por cada término producto y
cada variable se usan 2 bits, `10` si la variable aparece en forma normal, `01` si aparece
negada, y `00` si no participa del término (`11` no se usa). Por ejemplo, con $n=3$ variables
$(x_1,x_2,x_3)$, los términos $p_1 = x_1 \cdot x_2'$ y $p_2 = x_1' \cdot x_2' \cdot x_3'$ se
codifican:

| Término | $x_1$ | $x_2$ | $x_3$ |
|---|:---:|:---:|:---:|
| $p_1=x_1x_2'$ | 10 | 01 | 00 |
| $p_2=x_1'x_2'x_3'$ | 01 | 01 | 01 |

El plano OR se programa de forma análoga, con un bit por cada término producto que indica si
participa o no de cada salida. Por ejemplo, para implementar $y_1 = x_1x_2' + x_1x_3$ e
$y_2 = x_1x_2' + x_1'x_3$ se necesitan tres términos producto compartidos entre ambas salidas
($p_1=x_1x_2'$, $p_2=x_1x_3$, $p_3=x_1'x_3$), y el plano OR se programa como:

| Salida | $p_1$ | $p_2$ | $p_3$ |
|---|:---:|:---:|:---:|
| $y_1$ | 1 | 1 | 0 |
| $y_2$ | 1 | 0 | 1 |

```{note}
La ventaja central de un PLA frente a la síntesis AND-OR-INV directa es que los términos
producto se **comparten** entre varias salidas (en el ejemplo, $p_1$ se usa tanto para $y_1$
como para $y_2$), lo que reduce sensiblemente la cantidad de compuertas AND necesarias cuando
se implementan varias funciones relacionadas simultáneamente.
```

### 2.4 ROM (*Read-Only Memory*)

Una ROM es, estructuralmente, un caso particular de PLA: el **plano AND está fijo** (es,
literalmente, un decodificador que genera los $2^n$ minterms posibles de las $n$ entradas de
dirección) y solo el **plano OR es programable**. Una ROM de $2^n$ palabras de $m$ bits de
ancho tiene $n$ líneas de dirección y $m$ salidas de datos.

```text
              plano AND (fijo = decodificador)     plano OR (programable)
x1 ─┬──►[DECODE n a 2^n]── m0,m1,...,m(2^n-1) ──►[OR]── y0..y(m-1)
xn ─┘
```

Por ejemplo, una ROM de $n=2$ (4 palabras) y $m=4$ bits de ancho podría programarse así:

| Dirección $x_1x_0$ | $y_3y_2y_1y_0$ |
|:---:|:---:|
| 00 | 0110 |
| 01 | 0010 |
| 10 | 1101 |
| 11 | 0100 |

El plano AND ya está resuelto por el decodificador interno (cada dirección activa una única
línea de minterm); lo único que se "programa" —fusibles, máscara de fabricación, celdas de
memoria, según la tecnología de ROM— es qué minterms alimentan a cada salida del plano OR. Ver
[Memoria](21-memoria.md) para la clasificación completa de tipos de ROM (máscara, PROM, EPROM,
EEPROM) y su rol como memoria (más allá de su uso aquí como técnica de síntesis lógica).

### 2.5 ROM + MUX (y su relación con las LUT de FPGA)

Una limitación de la ROM pura es que su tamaño crece exponencialmente con el número de
variables ($2^n$ palabras). La técnica ROM+MUX reduce este costo dividiendo las variables en
dos grupos: unas pocas gobiernan un multiplexor de salida, y el resto direcciona ROMs más
chicas que producen los valores para cada rama del multiplexor.

Por ejemplo, para funciones $y_1,y_2$ de $(x_2,x_1,x_0)$, se puede usar $x_2$ como línea de
selección de un MUX2\_1 y separar cada función en sus dos **cofactores** respecto de $x_2$:

$$y_{10} = y_1(x_2=0) \qquad y_{11} = y_1(x_2=1) \qquad y_{20} = y_2(x_2=0) \qquad y_{21} = y_2(x_2=1)$$

cada uno de los cuales depende solo de $(x_1,x_0)$ y por lo tanto cabe en una ROM (o tabla) de
apenas $2^2=4$ palabras, en lugar de $2^3=8$.

```{tip}
Esta descomposición en cofactores respecto de una variable es, en esencia, la misma idea que
la **expansión de Shannon** —el mismo Shannon que en 1938 conectó los conmutadores con el
álgebra de Boole (ver [Introducción a los sistemas digitales](01-introduccion-a-los-sistemas-digitales.md))—:
$f = x_i' \cdot f(x_i=0) + x_i \cdot f(x_i=1)$. Descomponer por una variable y resolver los dos
casos con una tabla más chica es exactamente lo que hace un multiplexor con esa variable como
selección.
```

Esta es, precisamente, la estructura interna de las **LUT** (*Look-Up Tables*) de las FPGA
modernas: por ejemplo, una LUT de 6 entradas (LUT-6) puede implementar cualquier función de
hasta 6 variables como una ROM de 64 posiciones de 1 bit; combinando dos LUT-6 con un MUX2\_1
adicional (como en un *slice* simplificado de un bloque configurable lógico, CLB, de FPGAs
Xilinx) se pueden realizar funciones de hasta 7 u 8 variables. Ver
[Lógica programable](23-logica-programable.md) para el desarrollo completo de la arquitectura
de FPGA.

## 3. Comparación de las técnicas

| Técnica | Costo (área) | Velocidad | Flexibilidad / reprogramabilidad |
|---|---|---|---|
| AND-OR-INV (canónica) | Alto si no se simplifica | Alta (2 niveles) | Nula una vez fabricado |
| Multiplexor | Fijo, $2^n$ entradas | Alta | Nula (cableado a 0/1) |
| PLA | Medio (comparte términos producto) | Media | Programable una vez (fusibles) o en fábrica |
| ROM | Alto para $n$ grande ($2^n$ palabras) | Media-alta | Depende del tipo de ROM (ver [Memoria](21-memoria.md)) |
| ROM + MUX / LUT de FPGA | Bajo (tablas más chicas) | Media | Totalmente reprogramable (FPGA) |

## 4. Resumen

- La materialización de un diseño lógico atraviesa niveles de abstracción decrecientes
  (algorítmico → lógico → circuito → físico); la síntesis es el proceso de bajar de nivel,
  manual o automáticamente.
- Las alternativas tecnológicas van desde el ASIC (a medida, alto NRE) hasta los dispositivos
  programables por el usuario (PAL/CPLD/FPGA) y los circuitos impresos con componentes
  discretos e integrados estándar.
- Existen cinco técnicas clásicas de síntesis de un circuito combinacional a partir de su tabla
  de verdad: compuertas AND-OR-INV, multiplexores, PLA, ROM y ROM+MUX (esta última, la base
  conceptual de las LUT de FPGA).
- Todas estas técnicas, salvo la canónica AND-OR-INV, ganan eficiencia explotando estructura
  adicional: compartir términos producto (PLA), reutilizar el decodificador de direcciones
  (ROM), o descomponer la función en cofactores más chicos (ROM+MUX/LUT).

## 5. Ejercicios propuestos

```{exercise}
:label: ex-implem-1
Sintetizar mediante un multiplexor la función $f = x_1'x_0 + x_1x_0'$ (de 2 variables),
indicando qué constante se conecta a cada entrada de datos del MUX.
```

```{solution} ex-implem-1
:class: dropdown
Tabla de verdad: $x_1x_0=00\to0$, $01\to1$, $10\to1$, $11\to0$. Se usa un MUX4\_1 con
selección $x_1x_0$ y entradas de datos $d_0=0,\ d_1=1,\ d_2=1,\ d_3=0$. (Es, de hecho, la
función XOR de 2 variables.)
```

```{exercise}
:label: ex-implem-2
¿Cuántas palabras y de qué ancho necesitaría una ROM para implementar completamente un sumador
completo de 1 bit (dos operandos y acarreo de entrada, dos salidas: suma y acarreo de salida)?
```

```{solution} ex-implem-2
:class: dropdown
El sumador completo tiene 3 entradas, por lo que necesita $2^3=8$ palabras de dirección, y 2
salidas, por lo que cada palabra tiene 2 bits de ancho: una ROM de 8 palabras × 2 bits.
```

```{exercise}
:label: ex-implem-3
Explicar por qué la técnica ROM+MUX (o, equivalentemente, una LUT de FPGA) permite implementar
funciones de más variables con menos memoria que una ROM pura, sin perder generalidad (es
decir, sin restringir qué funciones se pueden representar).
```

```{solution} ex-implem-3
:class: dropdown
Porque descompone la función en cofactores respecto de una o más variables (expansión de
Shannon), de modo que cada cofactor depende de menos variables y cabe en una tabla
exponencialmente más chica; el multiplexor adicional recombina los cofactores sin restringir
qué función se puede representar, ya que cualquier función admite esa descomposición.
```

## 6. Bibliografía

```{bibliography}
:filter: docname in docnames
```
