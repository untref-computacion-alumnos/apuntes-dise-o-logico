# Diseño Lógico - Parcial 2024

## Ejercicio 1

Un _minterm_ es una expresión booleana en donde intervienen todas las variables
de la función. Se cumple que:

1. Es una conjunción que se evalúa como verdadera solo para una combinación de
   esas variables.
2. Es una disyunción que se evalúa como verdadera solo para una combinación de
   esas variables.
3. Es una conjunción que se evalúa como falsa solo para una combinación de esas
   variables.

## Ejercicio 2

La síntesis de una función lógica de cuatro variables se puede realizar si se
dispone de:

1. Una ROM de 8 celdas de $4 \text{ b}$ y un $MUX_{2\_1}$.
2. Una ROM de 16 celdas de $8 \text{ b}$.
3. Una ROM de 32 celdas de $1 \text{ b}$.
4. Ninguna de las opciones anteriores.
5. Cualquiera de las primeras tres opciones.

## Ejercicio 3

Según la versión simplificada de _slice_ de FPGA vista, con un _slice_ se pueden
implementar simultáneamente:

1. Una función de 8 variables y una función de 7 variables.
2. Una función de 8 variables y una función de 6 variables.
3. Dos funciones de 7 variables.
4. Tres funciones de 6 variables y una función de 7 variables.
5. Cualquiera de las opciones anteriores.

## Ejercicio 4

Considerar un sumador binario de $5 \text{ b}$, $r = x + y$, donde cada sumador
completo de $1 \text{ b}$ se implementa de la siguiente forma:

imagen

¿Cuál es el tiempo de estabilización del circuito para determinar $r_{4}$ (más
significativo)?

Para ello considerar:

- $T_{XOR} = 2 \text{ ns}$.
- $T_{OR} = 4 \text{ ns}$.

> Las compuertas de dos y tres entradas poseen el mismo tiempo de cómputo.

1. $28 \text{ ns}$.
2. $30 \text{ ns}$.
3. $35 \text{ ns}$.
4. $45 \text{ ns}$.

## Ejercicio 5

Dado el contador de $4 \text{ b}$ descripto en la siguiente figura

imagen

1. Es un contador sincrónico.
2. Es un contador asincrónico.
3. Puede ser cualquiera de las dos opciones anteriores, dependiendo de la
   aplicación.

## Ejercicio 6

Un circuito lógico combinacional depende de:

1. La combinación de entradas.
2. La combinación de entradas y estados en que se encuentra.
3. La secuencia de combinaciones de entradas a lo largo de todo el tiempo de
   actividad del circuito.
4. La combinación de entradas y salidas.

## Ejercicio 7

Considerar un _flip-flop D_. Qué afirmación es verdadera.

1. Ocupa menos área que un _latch D_.
2. Registra un bit en los flancos (alto y bajo) de la señal de sincronización.
3. Registra un bit durante el estado (alto o bajo) de la señal de
   sincronización.

## Ejercicio 8

Considerar el circuito que se encuntra a continuación. Para que implemente un
_latch SR_:

imagen

1. $A = R$, $B = S$.
2. $A = S'$, $B = R$.
3. $A = S$, $B = R$.
4. $A = R'$, $B = S'$.

## Ejercicio 9

Un registro SIPO de $4 \text{ b}$ se tiene que implementar con:

1. Cuatro _flip-flop D_.
2. Cuatro _latch D_.
3. Cualquiera de las opciones anteriores.

## Ejercicio 10

Dado el contador de programa de $8 \text{ b}$ descripto en la siguiente figura:

imagen

1. Se puede implementar con ocho _latch D_.
2. Se puede implementar con ocho _flip-flop D_.
3. Se puede implementar con cualquiera de las dos opciones anteriores,
   dependiendo de la aplicación.
