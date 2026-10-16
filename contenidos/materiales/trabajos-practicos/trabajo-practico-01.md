# Trabajo Práctico 1: Componentes lógicos

## Ejercicio 1

Dada la siguiente tabla de verdad:

| $x$ | $y$ | $z$ | $f(x, y, z)$ |
| :-: | :-: | :-: | :----------: |
| $0$ | $0$ | $0$ |     $1$      |
| $0$ | $0$ | $1$ |     $1$      |
| $0$ | $1$ | $0$ |     $0$      |
| $0$ | $1$ | $1$ |     $0$      |
| $1$ | $0$ | $0$ |     $0$      |
| $1$ | $0$ | $1$ |     $1$      |
| $1$ | $1$ | $0$ |     $1$      |
| $1$ | $1$ | $1$ |     $1$      |

1. Hallar la expresión disyuntiva canónica.
2. Hallar la expresión conjuntiva canónica.
3. Implementar mediante compuertas lógicas (**AND**, **OR**, **NOT**) las
   expresiones de los incisos anteriores.

### Ejercicio 1 resuelto

1. $(\bar{x} \cdot \bar{y} \cdot \bar{z}) + (\bar{x} \cdot \bar{y} \cdot z) +
    (x \cdot \bar{y} \cdot z) + (x \cdot y \cdot \bar{z}) + (x \cdot y \cdot z)$
2. $(\bar{x} + y + \bar{z}) \cdot (\bar{x} + y + z) \cdot (x + \bar{y} +
    \bar{z})$

## Ejercicio 2

Implementar demultiplexores:

1. $\text{DMUX}_{4\_1}$ utilizando $\text{DMUX}_{2\_1}$.
2. $\text{DMUX}_{8\_1}$ utilizando $\text{DMUX}_{2\_1}$.
3. $\text{DMUX}_{2\_8}$ utilizando $\text{DMUX}_{2\_1}$.
4. $\text{DMUX}_{8\_8}$ utilizando $\text{DMUX}_{2\_8}$.

## Ejercicio 3

Determinar expresiones para calcular el tiempo de cálculo y área del
$\text{MUX}_{8\_8}$ y $\text{MUX}_{m\_n}$ ($m = 2^{i}$) a partir de
$\text{MUX}_{2\_1}$.
