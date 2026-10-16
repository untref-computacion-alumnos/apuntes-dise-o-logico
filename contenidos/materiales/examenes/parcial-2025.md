# Diseño Lógico - Parcial 2025

## Ejercicio 1

Implementar mediante esquemático un contador de programa de $4 \text{ b}$ basado
en _flip-flop JK_. El contador posee una señal _ctrl_ de $2 \text{ b}$.

- $ctrl = 00$, el contador mantiene el valor.
- $ctrl = 01$, el contador decrementa en uno.
- $ctrl = 10$, el contador se incrementa en uno.
- $ctrl = 11$, el contador se carga con la entrada _din_ de $4 \text{ b}$.

## Ejercicio 2

Describir en **VHDL** una ALU que posee una señal de control _ctrl_ de
$2 \text{ b}$ que indica operación a realizar dos operandos de entrada $a$ y $b$
de $8 \text{ b}$ y una salida correspondiente al resultado $r$ de $8 \text{ b}$.

- $ctrl = 00$, $r = a + b$.
- $ctrl = 01$, $r = a$.
- $ctrl = 10$, $r = a \text{OR} b$.
- $ctrl = 11$, $r = a \text{AND} b$.

## Ejercicio 3

Responder.

1. Mencionar las diferencias entre los circuitos combinacionales y secuenciales.
2. Indicar si el contador del Ejercicio 1 es sincrónico o asincrónico.
   Justificar la respuesta.
3. En el diseño de un circuito digital, mencionar cuándo es conveniente utilizar
   un _latch_ y cuándo un _flip-flop_. Justificar la respuesta.
4. Realizar el análisis de tiempo de cálculo en un multiplexor de 8 entradas de
  $4 \text{ b}$ ($MUX_{8\_4}$).
