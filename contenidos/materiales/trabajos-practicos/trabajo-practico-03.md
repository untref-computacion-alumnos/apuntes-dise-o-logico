# Trabajo Práctico 3: Síntesis de circuitos secuenciales

## Ejercicio 1

Implementar los siguientes biestables

1. **Latch SR** sincrónico con _preset_ y _reset_ asincrónico basado en compuertas **NOR**.
2. **Latch SR** sincrónico con _preset_ y _reset_ asincrónico basado en compuertas **NAND**.
3. **Flip Flop D**.
4. **Flip Flop JK** a partir de **Flip Flop D**.
5. **Latch JK**.
6. **Flip Flop T** a partir de **Flip Flop D**.
7. **Flip Flop T** a partir de **Flip Flop JK**.

## Ejercicio 2

Sintetizar un registro de $8 \text{ b}$. El mismo tiene que tener una señal de habilitación
_enable_, una entrada _input_ de $8 \text{ b}$, reset asincrónico _ra_, una entrada de reloj _clk_ y
una salida _output_ de $8 \text{ b}$:

1. Basado en **Flip Flop D**.
2. Basado en **Flip Flop JK**.

## Ejercicio 3

Sintetizar el registro del inciso anterior con **Latch D**. Mencionar ventajas y desventajas
respecto a la implementación 2.1.

## Ejercicio 4

Considerar el circuito que se prsenta en la siguiente figura, en donde el tiempo de estabilización
para las operaciones de $8 \text{ b}$ son:

- suma $10 \text{ ns}$.
- resta 11 ns.
- shift 1 ns.
- multiplicación 25 ns.

El tiempo de multiplexor de 4 a 1 de $1 \text{ b}$ es de 2 ns, y los tiempos asociados a los
registros son:

- $t_{\text{setup}}: 0.5 \text{ ns}$.
