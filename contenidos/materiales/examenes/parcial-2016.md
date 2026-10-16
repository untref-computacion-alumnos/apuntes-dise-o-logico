# Diseño Lógico - Parcial 2016

## Ejercicio 1

Dada la siguiente función $f_{1} = { 0, 1, 2, 3, 4, 5, 10, 11, 14, 15 }$:

1. Minimizar la función utilizando el método gráfico de Karnaugh.
2. Identificar los implicantes primos y los esenciales.
3. Resolver por el método de Quinn-McCluskey.
4. Sintetizar la solución en un PLA.

## Ejercicio 2

Se desea implementar en hardware una estructura Fila Circular (FIFO), con una
capacidad de $32$ elementos de $8 \text{ b}$ a partir de un banco de registros y
lógica adicional.

El componente posee como entradas:

- Señal de reloj _clk_.
- Reset asincrónico _rst_.
- Dato a guardar _din_.
- Dos señales de control que permiten poner _put_ y sacar _get_ elementos.

Las salidas se componen de:

- El dato mśa antiguo en la estructura _dout_.
- Dos señales que indican el estado de la fila, el cual puede ser vacío _empty_
  o lleno _full_.

Las escrituras se deben realizar en forma ascendente comenzando desde la
dirección $0$, y está permitido el uso de hasta $2$ contadores de $5 \text{ b}$.

## Ejercicio 3

Dada las siguientes representaciones IBM 360, 4D23D70A y 519E0F26, realizar las
siguientes operaciones:

1. Suma.
2. Multiplicación

## Ejercicio 4

Responder.

1. Describir las diferencias entre _latch_ y _flip-flop_.
2. Definir síntesis lógica.
3. ¿Tiene sentido la implementación de un _latch T_? Justificar la respuesta.
4. Para aplicaciones de qué tipo o en qué casos se usaría una representación de
   números en CB. Justificar la respuesta.
5. Realizar un ejemplo para:
   1. Operación de resta entre dos números en CB(10, 2) que genere _overflow_ y
      _carry_.
   2. Operación de suma entre dos números en CB(2, 8) que genere _carry_ y no
      _overflow_.
6. Representar en IEEE 754 ($32 \text{ b}$):
   1. $9 \cdot 10^{-42}$.
   2. $234.745$.
