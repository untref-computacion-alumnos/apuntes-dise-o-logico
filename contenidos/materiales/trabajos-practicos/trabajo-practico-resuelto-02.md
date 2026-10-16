# Práctica 2: Síntesis de Circuitos Digitales

## Ejercicio 1

Minimizar las siguientes funciones booleanas utilizando el método tabular de Karnaugh.

### Parte 1.1

| $x$ | $y$ | $z$ | $f(x, y, z)$ |
| --- | --- | --- | ------------ |
| 0   | 0   | 0   | 1            |
| 0   | 0   | 1   | 0            |
| 0   | 1   | 0   | 0            |
| 0   | 1   | 1   | 1            |
| 1   | 0   | 0   | 1            |
| 1   | 0   | 1   | 1            |
| 1   | 1   | 0   | 0            |
| 1   | 1   | 1   | 1            |

#### Resolución Parte 1.1

![Resolución Parte 1.1](ejercicio1p1.png)

$f = \neg x \cdot \neg z + y \cdot z + x \cdot z$

### Parte 1.2

$f(x, y, z, t) = (3, 4, 6, 7, 8, 11, 12, 13)$

#### Resolución Parte 1.2

| $x$ | $y$ | $z$ | $t$ | $f(x, y, z, t)$ |
| --- | --- | --- | --- | --------------- |
| 0   | 0   | 0   | 0   | 0               |
| 0   | 0   | 0   | 1   | 0               |
| 0   | 0   | 1   | 0   | 0               |
| 0   | 0   | 1   | 1   | 1               |
| 0   | 1   | 0   | 0   | 1               |
| 0   | 1   | 0   | 1   | 0               |
| 0   | 1   | 1   | 0   | 1               |
| 0   | 1   | 1   | 1   | 1               |
| 1   | 0   | 0   | 0   | 1               |
| 1   | 0   | 0   | 1   | 0               |
| 1   | 0   | 1   | 0   | 0               |
| 1   | 0   | 1   | 1   | 1               |
| 1   | 1   | 0   | 0   | 1               |
| 1   | 1   | 0   | 1   | 1               |
| 1   | 1   | 1   | 0   | 0               |
| 1   | 1   | 1   | 1   | 0               |

![Resolución Parte 1.2](ejercicio1p2.png)

$f = y \cdot \neg z \cdot \neg t + x \cdot \neg z \cdot \neg t + \neg y \cdot z \cdot t + \neg x \cdot y \cdot z + x \cdot y \cdot \neg z$

### Parte 1.3

$f(x, y, z, t) = x \cdot \overline{y} \cdot z + y \cdot z + \overline{x} \cdot \overline{y} \cdot z + x \cdot y + \overline{z}$

#### Resolución Parte 1.3

| $x$ | $y$ | $z$ | $t$ | $f(x, y, z, t)$ |
| --- | --- | --- | --- | --------------- |
| 0   | 0   | 0   | 0   | 1               |
| 0   | 0   | 0   | 1   | 1               |
| 0   | 0   | 1   | 0   | 1               |
| 0   | 0   | 1   | 1   | 1               |
| 0   | 1   | 0   | 0   | 1               |
| 0   | 1   | 0   | 1   | 1               |
| 0   | 1   | 1   | 0   | 1               |
| 0   | 1   | 1   | 1   | 1               |
| 1   | 0   | 0   | 0   | 1               |
| 1   | 0   | 0   | 1   | 1               |
| 1   | 0   | 1   | 0   | 1               |
| 1   | 0   | 1   | 1   | 1               |
| 1   | 1   | 0   | 0   | 1               |
| 1   | 1   | 0   | 1   | 1               |
| 1   | 1   | 1   | 0   | 1               |
| 1   | 1   | 1   | 1   | 1               |

![Resolución Parte 1.3](ejercicio1p3.png)

$f = 1$

## Ejercicio 2

Dadas las siguientes funciones:

$f1 = x1 \cdot \overline{x2} + \overline{x0} \cdot x3 \cdot x4 + x2 \cdot \overline{x4}$

$f2 = \overline{x0} \cdot \overline{x2} + x1 \cdot x2 \cdot \overline{x3} + x1 \cdot x2$

| x4  | x3  | x2  | x1  | x0  | f1  |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 1   | 0   |
| 0   | 0   | 0   | 1   | 0   | 1   |
| 0   | 0   | 0   | 1   | 1   | 1   |
| 0   | 0   | 1   | 0   | 0   | 1   |
| 0   | 0   | 1   | 0   | 1   | 1   |
| 0   | 0   | 1   | 1   | 0   | 1   |
| 0   | 0   | 1   | 1   | 1   | 1   |
| 0   | 1   | 0   | 0   | 0   | 0   |
| 0   | 1   | 0   | 0   | 1   | 0   |
| 0   | 1   | 0   | 1   | 0   | 1   |
| 0   | 1   | 0   | 1   | 1   | 1   |
| 0   | 1   | 1   | 0   | 0   | 1   |
| 0   | 1   | 1   | 0   | 1   | 1   |
| 0   | 1   | 1   | 1   | 0   | 1   |
| 0   | 1   | 1   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 0   | 1   | 0   |
| 1   | 0   | 0   | 1   | 0   | 1   |
| 1   | 0   | 0   | 1   | 1   | 1   |
| 1   | 0   | 1   | 0   | 0   | 0   |
| 1   | 0   | 1   | 0   | 1   | 0   |
| 1   | 0   | 1   | 1   | 0   | 0   |
| 1   | 0   | 1   | 1   | 1   | 0   |
| 1   | 1   | 0   | 0   | 0   | 1   |
| 1   | 1   | 0   | 0   | 1   | 0   |
| 1   | 1   | 0   | 1   | 0   | 1   |
| 1   | 1   | 0   | 1   | 1   | 1   |
| 1   | 1   | 1   | 0   | 0   | 1   |
| 1   | 1   | 1   | 0   | 1   | 0   |
| 1   | 1   | 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 1   | 1   | 0   |

| x3  | x2  | x1  | x0  | f2  |
| --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 1   |
| 0   | 0   | 0   | 1   | 0   |
| 0   | 0   | 1   | 0   | 1   |
| 0   | 0   | 1   | 1   | 0   |
| 0   | 1   | 0   | 0   | 0   |
| 0   | 1   | 0   | 1   | 0   |
| 0   | 1   | 1   | 0   | 1   |
| 0   | 1   | 1   | 1   | 1   |
| 1   | 0   | 0   | 0   | 1   |
| 1   | 0   | 0   | 1   | 0   |
| 1   | 0   | 1   | 0   | 1   |
| 1   | 0   | 1   | 1   | 0   |
| 1   | 1   | 0   | 0   | 0   |
| 1   | 1   | 0   | 1   | 0   |
| 1   | 1   | 1   | 0   | 1   |
| 1   | 1   | 1   | 1   | 1   |

### Parte 2.1

Sintetizar mediante PLA.

#### Resolución Parte 2.1

![Sintetización mediante PLA](ejercicio2p1.png)

### Parte 2.2

Sintetizar mediante compuertas AND, OR, INV.

#### Resolución Parte 2.2

![ANDORINV f1](ejercicio2p2_1.png)

![ANDORINV f2](ejercicio2p2_2.png)

### Parte 2.3

Sintetizar $f1$ solo con compuertas NAND y $f2$ solo con compuertas NOR.

#### Resolución Parte 2.3

![NAND f1](ejercicio2p3_1.png)

![NOR f2](ejercicio2p3_2.png)

### Parte 2.4

Sintetizar mediante ROM de 8 celdas y multiplexores.

#### Resolución Parte 2.4

![ROM de 8 celdas y multiplexores - f1](ejercicio2p4_1.png)

![ROM de 8 celdas y multiplexores - f2](ejercicio2p4_2.png)

### Parte 2.5

Sintetizar mediante ROM de 32 celdas.

#### Resolución Parte 2.5

![ROM de 32 celdas](ejercicio2p5_1.png)

## Ejercicio 3

Dadas las siguientes funciones:

$f1 = x6 \cdot x5 \cdot \overline{x2} + x1 \cdot \overline{x2} + \overline{x0} \cdot x3 \cdot x4 + x5 \cdot x2 \cdot \overline{x4}$

$f2 = \overline{x0} \cdot \overline{x2} + x1 \cdot x2 \cdot \overline{x3} + x1 \cdot x2$.

Sintetizar utilizando un slice de dispositivo FPGA.

### Resolución Ejercicio 3

![FPGA](ejercicio3.png)

## Ejercicio 4

Sintetizar una Unidad Aritmética Lógica.

Considerar:

- Operandos de entrada de 8 bits: $a$ y $b$.
- Señal de control de 2 bits: ctrl.
- Resultado $r$ de 8 bits.
- Operaciones:
  
  | ctrl | operación |
  | ---- | --------- |
  | 0    | +         |
  | 1    | -         |
  | 2    | and       |
  | 3    | or        |

## Ejercicio 5

Sintetizar un restador binario de operandos de 4 bits, $r = a - b$ (con $a$, $b$, $r$ de 4 bits). Para ello utilizar PLAs de 3 variables de entradas y 2 salidas.

**Nota 1**: Se deben utilizar varios PLAs conectados.

**Nota 2**: Cada PLA puede implementar un restador completo de 1 bit.

## Ejercicio 6

Sintetizar utilizando slices de FPGA:

### Parte 6.1

Una función de 6 y una función de 7 variables.

### Parte 6.2

Una función de 8 variables y una función de 6 variables.

### Parte 6.3

Una función de 10 variables. Considerar $f(x9, ..., x0) = \neg x9 \cdot \neg x8 \cdot g(x7, ..., x0) + \neg x9 \cdot x8 \cdot h(x7, ..., x0) + x9 \cdot \neg x8 \cdot l(x7, ..., x0) + x9 \cdot x8 \cdot q(x7, ..., x0)$, donde $g()$, $h()$, $l()$, y $q()$ son funciones de 8 variables.

**Nota 1**: Mostrar circuito con slices conectados, en donde se encuentren resaltados los componentes utilizados.
