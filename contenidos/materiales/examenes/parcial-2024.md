# Diseño Lógico - Parcial 2024

## Ejercicio 1

Implementar utilizando _slices_ de FPGA. Para ello dibujar los _slices_ y
resaltar los componentes del _slice_ usado indicando qué funcionalidad cumple.

1. Dos funciones de 2 variables y una función de 7 variables.
2. Una función de 10 variables. Considerar $f(x_{9}, ..., x_{0}) = x_{9}', x_{8}'. g(x_{7}, ..., x_{0}) + x_{9}'.x_{8}.h(x_{7}, ..., x_{0}) + x_{9}.x_{8}'.k(x_{7}, ..., x_{0}) + x_{9}.x_{8}.t(x_{7}, ..., x_{0})$, donde $g()$, $h()$, $k()$ y $t()$ son funciones de 8 variables.

## Ejercicio 2

Implementar un circuito que realice la suma entre dos operandos de naturales de
$2 \text{ b}$, $r = a + b$, en donde el tamaño de $a$ y $b$ es de $2 \text{ b}$
y $r$ de tamaño de $3 \text{ b}$, conteniendo acarreo final.

1. Utilizar ROM de 16 celdas de $8 \text{ b}$.
2. Utilizar PLA.
3. Utilizar solo dos memorias ROM de 8 celdas de $4 \text{ b}$.

## Ejercicio 3

Realizar un contador de programa de $8 \text{ b}$. El contador de programa es un
registro que posee una entrada $J$ (_jump_), de modo que cuando $J = 0$ el
registro se incrementa en uno, y cuando $J = 1$ el registro toma el valor
presente en la entrada $D$ ($8 \text{ b}$).

1. Implementar el contador con _flip-flop JK_.
2. ¿Se puede implementar con _latches_? Justificar la respuesta.
3. ¿El contador implementado es sincrónico o asincrónico? Justificar la
   respuesta.
