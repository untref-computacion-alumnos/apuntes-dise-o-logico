---
title: "Sumadores, Restadores y Comparadores"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Sumadores, Restadores y Comparadores

```{admonition} Sobre este apunte
:class: note
Este capítulo no proviene directamente de las diapositivas de la cátedra: los bloques
aritméticos (sumador, restador, comparador) se mencionan de pasada en las presentaciones de
circuitos secuenciales (como el bloque *Adder* usado en contadores) y de VHDL (el *comparador*
usado como ejemplo de lenguaje), pero su diseño lógico como circuitos combinacionales no se
desarrolla ahí. Se completa aquí con el tratamiento estándar de la bibliografía de la materia
{cite}`tocci2007,harris2012,floyd2000`, manteniendo la misma notación (`x'` para negación, `·`
para AND, `+` para OR) que el resto del apunte.
```

## 1. Introducción

Los sumadores, restadores y comparadores son los bloques combinacionales elementales de toda
unidad aritmética. Se construyen a partir de las compuertas básicas (ver
[Compuertas lógicas](05-compuertas-logicas.md)) y son un ejemplo directo de diseño combinacional
siguiendo la metodología general presentada en
[Circuitos lógicos combinacionales](09-circuitos-logicos-combinacionales.md): especificación →
tabla de verdad → ecuación → simplificación → implementación.

## 2. Semisumador (Half Adder)

Un **semisumador** suma dos bits $x$ e $y$ y produce una **suma** $s$ y un **acarreo** $c$
(*carry*), pero no contempla un acarreo de entrada.

| $x$ | $y$ | $s$ | $c$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$$s = x \oplus y \qquad\qquad c = x \cdot y$$

```text
      ┌─────┐
 x ──►│ XOR ├──► s
 y ──►│     │
      └─────┘
      ┌─────┐
 x ──►│ AND ├──► c
 y ──►│     │
      └─────┘
```

```{note}
La salida $s$ coincide con la compuerta XOR y la salida $c$ con la compuerta AND. Son las mismas
dos funciones que aparecen en el catálogo de funciones de dos variables del capítulo
[Funciones lógicas](04-funciones-logicas.md).
```

## 3. Sumador completo (Full Adder)

Para sumar números de más de un bit hace falta poder propagar el acarreo generado por la columna
anterior. El **sumador completo** suma tres bits: $x$, $y$ y un acarreo de entrada $c_{in}$, y
produce una suma $s$ y un acarreo de salida $c_{out}$.

| $x$ | $y$ | $c_{in}$ | $s$ | $c_{out}$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

$$s = x \oplus y \oplus c_{in} \qquad\qquad c_{out} = x \cdot y + x \cdot c_{in} + y \cdot c_{in}$$

Un sumador completo puede armarse con dos semisumadores y una compuerta OR:

```text
        ┌───────────┐            ┌───────────┐
 x ────►│           ├──s1──►    │           │
 y ────►│  HA (1)   │            │  HA (2)   ├──► s
        │           ├──c1──┐    │           │
        └───────────┘      │ ┌─►│           │
                            │ │  └─────┬─────┘
 c_in ──────────────────────┼─┘        c2
                            │           │
                            └──[OR]◄────┘
                                 │
                                 ▼
                               c_out
```

$c_{out} = c_1 + c_2$, donde $c_1 = x \cdot y$ (acarreo del primer semisumador) y $c_2$ es el
acarreo del segundo semisumador (entre $s_1$ y $c_{in}$).

## 4. Sumador binario de n bits (Ripple Carry Adder)

Encadenando $n$ sumadores completos, con el acarreo de salida de cada etapa conectado al acarreo
de entrada de la siguiente, se obtiene un **sumador de acarreo serie** (*ripple carry adder*) de
$n$ bits:

```text
      x3 y3        x2 y2        x1 y1        x0 y0
       │  │         │  │         │  │         │  │
       ▼  ▼         ▼  ▼         ▼  ▼         ▼  ▼
      ┌──────┐     ┌──────┐     ┌──────┐     ┌──────┐
0────►│  FA  ├────►│  FA  ├────►│  FA  ├────►│  FA  ├──► c_out
      │  (3) │ c3  │  (2) │ c2  │  (1) │ c1  │  (0) │
      └──┬───┘     └──┬───┘     └──┬───┘     └──┬───┘
         ▼            ▼            ▼            ▼
         s3           s2           s1           s0
```

El acarreo de entrada del bit menos significativo se conecta a 0 (o se usa como entrada de un
sumador/restador combinado, ver más abajo).

```{important}
El nombre "acarreo serie" viene de que el acarreo debe **propagarse** secuencialmente desde el
bit menos significativo hasta el más significativo: el resultado final no está estable hasta que
el acarreo atravesó las $n$ etapas. El **camino crítico** del circuito (ver
[Circuitos lógicos combinacionales](09-circuitos-logicos-combinacionales.md)) crece linealmente
con $n$, por lo que el tiempo de propagación de un sumador de $n$ bits es $O(n)$.
```

Para reducir este retardo existen esquemas de **acarreo anticipado** (*carry look-ahead*), que
calculan el acarreo de cada etapa directamente en función de las entradas mediante señales de
generación ($g_i = x_i \cdot y_i$) y propagación ($p_i = x_i + y_i$) del acarreo, a costa de un
circuito combinacional más complejo. Es un tema de diseño avanzado que se desarrolla en
bibliografía específica de arquitectura de computadoras {cite}`harris2012`.

## 5. Restadores

### 5.1 Semirrestador y restador completo

De forma dual al sumador, un **semirrestador** (*half subtractor*) calcula la diferencia $d$ y el
préstamo (*borrow*) $b$ de $x - y$:

| $x$ | $y$ | $d$ | $b$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

$$d = x \oplus y \qquad\qquad b = x' \cdot y$$

El **restador completo**, que además contempla un préstamo de entrada $b_{in}$, sigue el mismo
patrón que el sumador completo (con $d$ en lugar de $s$ y $b_{out}$ en lugar de $c_{out}$).

### 5.2 Resta mediante complemento a 2

En la práctica, los circuitos digitales casi nunca implementan un restador dedicado: es más
económico reutilizar el sumador ya construido, sumando el **complemento a 2** del sustraendo (ver
[Representación de números](03-representacion-de-numeros-enteros-fraccionarios-y-negativos.md)):

$$x - y = x + (-y) = x + (y' + 1)$$

Es decir, para restar $y$ basta con invertir todos sus bits (obtener $y'$) y sumar 1 al resultado
mediante el acarreo de entrada del sumador.

### 5.3 Sumador/restador combinado

Un único sumador de $n$ bits puede configurarse para sumar o restar agregando una compuerta XOR
por cada bit de $y$, controlada por una señal de modo $M$:

```text
                    M
                    │
        ┌───────────┼───────────┬── ... ──┐
        │           │           │         │
       y0 ──[XOR]  y1 ──[XOR]  y2 ──[XOR] y3 ──[XOR]
        │            │           │         │
        ▼            ▼           ▼         ▼
      ┌──────┐     ┌──────┐    ┌──────┐  ┌──────┐
M ───►│  FA  │────►│  FA  │───►│  FA  │─►│  FA  │──► c_out
(cin) │  (0) │ c0  │  (1) │ c1 │  (2) │c2│  (3) │
      └──┬───┘     └──┬───┘    └──┬───┘  └──┬───┘
         s0           s1          s2        s3
```

- $M=0$: cada $y_i \oplus 0 = y_i$, y el acarreo de entrada es 0 → el circuito suma $x+y$.
- $M=1$: cada $y_i \oplus 1 = y_i'$, y el acarreo de entrada es 1 → el circuito calcula
  $x + y' + 1 = x - y$.

```{tip}
Esta técnica —controlar con una única señal si el circuito suma o resta— es un ejemplo clásico de
reutilización de hardware: el mismo sumador de $n$ bits, con $n$ compuertas XOR adicionales,
implementa las dos operaciones sin duplicar el sumador completo.
```

## 6. Comparadores de magnitud

### 6.1 Comparador de 1 bit

Un comparador determina si $x=y$, $x>y$ o $x<y$. Para un único bit:

| $x$ | $y$ | $x=y$ | $x>y$ | $x<y$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 |

$$
(x=y) = x \odot y = (x \cdot y) + (x' \cdot y') \qquad\qquad
(x>y) = x \cdot y' \qquad\qquad
(x<y) = x' \cdot y
$$

donde $x \odot y$ es la compuerta XNOR (complemento de XOR, ver
[Compuertas lógicas](05-compuertas-logicas.md)).

### 6.2 Comparador de n bits en cascada

Para comparar números de $n$ bits se comparan primero los bits más significativos: si son
iguales, el resultado depende de los bits siguientes, y así sucesivamente. Esto permite construir
comparadores de $n$ bits en **cascada** a partir de bloques de comparación más pequeños, cada uno
con entradas de "mayor/igual/menor en las etapas anteriores" que se van propagando desde el bit
más significativo hacia el menos significativo.

```{note}
El circuito integrado comercial **74LS85** es un comparador de magnitud de 4 bits con entradas de
cascada, pensado exactamente para encadenarse y construir comparadores de 8, 12, 16... bits sin
rediseñar el circuito interno.
```

## 7. Hacia la ALU

Los bloques vistos en este capítulo —sumador, restador, comparador— junto con las compuertas
lógicas bit a bit (AND, OR, XOR aplicadas en paralelo a cada bit de dos operandos) son los
componentes que integra una **Unidad Aritmético-Lógica** (ALU), seleccionando la operación deseada
mediante un multiplexor controlado por un código de operación (ver
[Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md)). El diseño completo de
una ALU y su integración en un procesador corresponde a la materia de Arquitectura de
Computadoras, fuera del alcance de este apunte.

## 8. Resumen

- El **semisumador** suma dos bits ($s=x \oplus y$, $c=x \cdot y$); el **sumador completo** suma
  además un acarreo de entrada y es la base para construir sumadores de más bits.
- El **sumador de acarreo serie** encadena sumadores completos, con un retardo de propagación que
  crece linealmente con la cantidad de bits; el **acarreo anticipado** es la alternativa rápida.
- Restar es sumar el **complemento a 2** del sustraendo; con compuertas XOR controladas por una
  señal de modo, un mismo sumador implementa suma y resta.
- Un **comparador de magnitud** determina igualdad y orden entre dos números; se construye en
  cascada para operar con más bits sin rediseñar el circuito.

## 9. Bibliografía

```{bibliography}
:filter: docname in docnames
```

## 10. Ejercicios propuestos

```{exercise}
:label: ex-sumador-1
Diseñar la tabla de verdad y las ecuaciones de un semirrestador completo (con préstamo de
entrada $b_{in}$), por analogía con el sumador completo.
```

```{solution} ex-sumador-1
:class: dropdown
$$d = x \oplus y \oplus b_{in} \qquad\qquad b_{out} = x' \cdot y + x' \cdot b_{in} + y \cdot b_{in}$$
Se obtiene reemplazando en la tabla del sumador completo la condición de "acarreo" por la de
"préstamo": hay préstamo cuando $x < y$, o cuando son iguales pero ya había un préstamo previo.
```

```{exercise}
:label: ex-sumador-2
Explicar por qué, al sumar el complemento a 2 de $y$ para restar $x-y$, es necesario sumar 1
además de invertir los bits de $y$.
```

```{solution} ex-sumador-2
:class: dropdown
El complemento a 2 de un número se define como su complemento a 1 (bits invertidos) más 1 (ver
[Representación de números](03-representacion-de-numeros-enteros-fraccionarios-y-negativos.md)).
Sumar solo $y'$ (complemento a 1) da $x + y' = x - y - 1$, que no es el resultado buscado; sumar
también 1 corrige esa diferencia.
```

```{exercise}
:label: ex-sumador-3
Un sumador/restador de 4 bits como el de la sección 5.3 tiene $x=0110$ (6) e $y=0011$ (3).
Indicar la salida para $M=0$ y para $M=1$.
```

```{solution} ex-sumador-3
:class: dropdown
Con $M=0$: $y$ no se invierte y $c_{in}=0$, el circuito calcula $0110+0011=1001$ (9).
Con $M=1$: $y$ se invierte a $1100$ y $c_{in}=1$, el circuito calcula
$0110+1100+1=0011$ (3, descartando el acarreo de salida), que es $6-3=3$.
```

```{exercise}
:label: ex-sumador-4
Construir un comparador de 2 bits ($x_1x_0$ vs. $y_1y_0$) a partir de comparadores de 1 bit,
indicando cómo se combinan los resultados de cada bit (pista: primero se compara el bit más
significativo).
```

```{solution} ex-sumador-4
:class: dropdown
Se comparan $x_1$ con $y_1$: si son distintos, ese resultado define la comparación completa. Si
son iguales ($x_1=y_1$), el resultado depende de comparar $x_0$ con $y_0$. Esto se puede expresar
como:
$$(x>y) = (x_1 \cdot y_1') + (x_1 \odot y_1)\cdot(x_0 \cdot y_0')$$
y de forma análoga para $(x<y)$ y $(x=y)$, generalizando el mecanismo de cascada de la sección 6.2.
```
