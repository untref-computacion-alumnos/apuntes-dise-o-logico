# Trabajo Práctico 2: Síntesis de Circuitos Digitales

## Ejercicio 1

Minimizar las siguientes funciones booleanas utilizando el método tabular de
Karnaugh.

1. | $x$ | $y$ | $z$ | $f(x, y, z)$ |
   | :-: | :-: | :-: | :----------: |
   |  0  |  0  |  0  |      1       |
   |  0  |  0  |  1  |      0       |
   |  0  |  1  |  0  |      0       |
   |  0  |  1  |  1  |      1       |
   |  1  |  0  |  0  |      1       |
   |  1  |  0  |  1  |      1       |
   |  1  |  1  |  0  |      0       |
   |  1  |  1  |  1  |      1       |

2. $f(x, y, z, t) = (3, 4, 6, 7, 8, 11, 12, 13)$

3. $f(x, y, z, t) = x \cdot \overline{y} \cdot z + y \cdot z + \overline{x}
   \cdot \overline{y} \cdot z + x \cdot y + \overline{z}$

## Ejercicio 2

Dadas las siguientes funciones:

$$
f_{1} = x_{1} \cdot \overline{x_{2}} + \overline{x_{0}} \cdot x_{3} \cdot x_{4}
+ x_{2} \cdot \overline{x_{4}}
$$

$$
f_{2} = \overline{x_{0}} \cdot \overline{x_{2}} + x_{1} \cdot x_{2} \cdot
\overline{x_{3}} + x_{1} \cdot x_{2}
$$

Sintetizar en:

1. PLA
2. Compuertas AND, OR, INV, etc.
3. $f_{1}$ solo con compuertas NAND y $f_{2}$ solo con compuertas NOR.
4. ROM de 8 celdas y multiplexores.
5. ROM de 32 celdas.

## Ejercicio 3

Dadas las siguientes funciones:

$$
f_{1} = x_{6} \cdot x_{5} \cdot \overline{x_{2}} + x_{1} \cdot \overline{x_{2}}
+ \overline{x_{0}} \cdot x_{3} \cdot x_{4} + x_{2} \cdot \overline{x_{4}} \cdot
x_{5}
$$

$$
f_{2} = \overline{x_{0}} \cdot \overline{x_{2}} + x_{1} \cdot x_{2} \cdot
\overline{x_{3}} + x_{1} \cdot x_{2}
$$

Sintetizar utilizando un slice de dispositivo FPGA.

## Ejercicio 4

Sintetizar una ALU (_Aritmetic Logic Unit_).

Considerar:

- Operandos de entrada de $8 \text{ b}$: $a$ y $b$.
- Señal de control de $2 \text{ b}$: $\text{ctrl}$.
- Resultado $r$ de $8 \text{ b}$.

Operaciones:

| $ctrl$ | Operación |
| :----: | :-------: |
|   0    |     +     |
|   1    |     -     |
|   2    |    AND    |
|   3    |    OR     |

## Ejercicio 5

Sintetizar un restador binario de operandos de $4 \text{ b}$, $r = a - b$ (con
$a, b, r$ de $4 \text{ b}$). Para ello utilizar PLAs de 3 variables de entrada y
2 salidas.

> Se deben utilizar varios PLAs conectados.
> Cada PLA puede implementar un restador completo de $1 \text{ b}$.

## Ejercicio 6

Sintetizar utilizando slices de FPGA:

1. Una función de 6 y una función de 7 variables.
2. Una función de 8 variables y una función de 6 variables.
3. Una función de 10 variables. Considerar: $f(x_{9}, \dots, x_{0}) =
   \overline{x_{9}} \cdot \overline{x_{8}} \cdot g(x_{7}, \dots, x_{0}) +
   \overline{x_{9}} \cdot x_{8} \cdot h(x_{7}, \dots, x_{0}) + x_{9} \cdot
   \overline{x_{8}} \cdot l(x_{7}, \dots, x_{0}) + x_{9} \cdot x_{8} \cdot
   q(x_{7}, \dots, x_{0})$, donde $g()$, $h()$, $l()$ y $q()$ son funciones de
   8 variables.

> Mostrar el circuito con slices conectados, en donde se encuentren resaltados
> los componentes utilizados.
