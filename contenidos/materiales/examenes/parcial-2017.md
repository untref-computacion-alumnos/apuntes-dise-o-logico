# Diseño Lógico - Parcial 2017

## Ejercicio 1

Se desea implementar un banco de registros de 8 registros de $8 \text{ b}$, a
partir de registros de $8 \text{ b}$ implementados con _flip-flop D_.

Las entradas del banco de registro son:

- _clr_: Señal de reloj.
- _rst_: Reset asincrónico del circuito.
- _r\_addr_: Dirección de lectura.
- _w\_addr_: Dirección de escritura.
- _we_: Habilitación de escritura.
- _d\_in_: Dato a escribir.
- _d\_out_: Dato de lectura.

1. Implementar el banco de registros de $8 \text{ b}$.
2. Implementar un banco de 32 registros de $16 \text{ b}$ a partir del banco de
   registros del inciso anterior.
3. ¿Cómo se modela la habilitación de escritura de un registro?

## Ejercicio 2

Considerar una ALU de $8 \text{ b}$. La misma posee como entradas/salidas $a$ y
$b$ de $8 \text{ b}$ (operandos de entrada)

- _op_ de $2 \text{ b}$: Operación a realizar.
- _r_ de $8 \text{ b}$: Resultado de la operación.

- $op = 0$, $a + b$
- $op = 1$, $a - b$.
- $op = 2$, $a \text{AND} b$
- $op = 3$, $a \text{OR} b$.

Se dispone para la implementación de la ALU:

- Multiplexores de dos entradas de $1 \text{ b}$ ($MUX_{2\_1}$).
- Demultiplexores de dos salidas de $1 \text{ b}$ ($DMUX_{2\_1}$).
- _full adder_ de tres operandos de $1 \text{ b}$ ($FA$).
- Compuertas lógicas (AND, OR, XOR e INV).

> Las operaciones se suma/resta se realizan en complemento a 2.

## Ejercicio 3

Representar y operar en el sistema especificado. Indicar en decimal cuál es el
resultado representado.

1. Resta en CD(4, 4) con frontera igual a $57_{10}$ entre $120_{10}$ y
   $- 60_{10}$.
2. Suma en CD(4, 4) con frontera igual a $57_{10}$ entre $120_{10}$ y $70_{10}$.
3. Suma en CI(10, 3) entre $- 120_{10}$ y $- 70_{10}$.
4. Suma en CI(10, 3) entre $- 120_{10}$ y $- 390_{10}$.

## Ejercicio 4

Responder.

1. Explicar la diferencia entre _latch_ y _flip-flop_. Dar un ejemplo de cuándo
   es conveniente utilizar cada uno.
2. Definir síntesis lógica.
3. Mencionar ventajas y desventajas de los tres métodos de minimización vistos.
4. Para aplicaciones de qué tipo o en qué casos se usaría representación de
   números en CB. Justificar la respuesta.
