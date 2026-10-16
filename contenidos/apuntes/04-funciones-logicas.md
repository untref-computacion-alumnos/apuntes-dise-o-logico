---
title: "Funciones lógicas"
subject: "Diseño Lógico"
---

# Funciones lógicas

```{admonition} Sobre este apunte
:class: note
Este apunte formaliza una idea que quedó planteada al final de
[Introducción a los sistemas digitales](01-introduccion-a-los-sistemas-digitales.md): que un
circuito de conmutadores puede describirse con una función que solo toma los valores $0$ y $1$. El
contenido retoma la sección "Funciones lógicas – Tablas de Verdad" de la presentación de la cátedra
y se completa con bibliografía estándar de la materia ({cite}`tocci2007`, {cite}`floyd2000`) para la
enumeración sistemática de funciones de una y dos variables.
```

## 1. ¿Qué es una función lógica?

Una **función lógica** (o función booleana) de $n$ variables es una función

$$
f: \{0,1\}^n \longrightarrow \{0,1\}
$$

que a cada combinación posible de valores de entrada $(x_1, x_2, \ldots, x_n)$, cada uno $0$ o $1$,
le asigna una única salida $0$ o $1$. Estas funciones son el objeto central del diseño lógico:
cualquier bloque combinacional (una compuerta, un sumador, un decodificador) no es otra cosa que la
implementación física de una o varias funciones lógicas.

```{note} Nota
A diferencia de una función matemática "continua" (como $f(x) = x^2$), una función lógica tiene un
dominio **finito:** con $n$ variables de entrada existen exactamente $2^n$ combinaciones posibles, y
la función debe definir una salida para cada una de ellas.
```

## 2. La tabla de verdad como descripción universal

La forma más directa y sin ambigüedades de describir una función lógica es enumerar, para cada una
de las $2^n$ combinaciones de entrada, el valor de salida correspondiente. Esta enumeración es la
**tabla de verdad**.

### 2.1. Ejemplo de trabajo: función de tres variables

A lo largo de varios capítulos de este apunte (formas canónicas, multiplexores) se va a retomar el
mismo ejemplo, para poder comparar las distintas técnicas sobre una única función. Sea
$o = f(x,y,z)$ definida por:

| $x$ | $y$ | $z$ |  $o$  |
| :-: | :-: | :-: | :---: |
|  0  |  0  |  0  | **1** |
|  0  |  0  |  1  |   0   |
|  0  |  1  |  0  |   0   |
|  0  |  1  |  1  | **1** |
|  1  |  0  |  0  |   0   |
|  1  |  0  |  1  | **1** |
|  1  |  1  |  0  | **1** |
|  1  |  1  |  1  |   0   |

Esta tabla, por sí sola, define $f$ completamente: no hace falta ninguna otra información para saber
qué salida produce cualquier combinación de $x,y,z$.

## 3. Equivalencia entre tabla de verdad, ecuación booleana y circuito

Existe una equivalencia total entre tres formas distintas de describir la **misma** función lógica:

$$
\text{Tabla de verdad} \;\Longleftrightarrow\; \text{Ecuación booleana} \;\Longleftrightarrow\; \text{Circuito de compuertas}
$$

- Cualquier función lógica puede describirse mediante una **tabla de verdad** (sección anterior).
- Cualquier tabla de verdad puede describirse mediante una **ecuación booleana** (una expresión con
  variables, $+$, $\cdot$ y $'$).
- Cualquier ecuación booleana puede implementarse como un **circuito de compuertas lógicas**.

```{important} Importante
Estas tres representaciones no son "parecidas": son exactamente la misma información expresada de
tres maneras distintas. Poder pasar de una a otra en cualquier dirección es la habilidad central de
todo el diseño lógico combinacional. El [capítulo de formas canónicas](07-formas-canonicas.md)
muestra un método sistemático para obtener la ecuación booleana directamente a partir de la tabla de
verdad.
```

Las compuertas físicas que permiten construir el circuito (NOT, AND, OR y sus derivadas) se
desarrollan en el [próximo capítulo](05-compuertas-logicas.md). El marco algebraico formal que
permite manipular la ecuación booleana (axiomas y teoremas) se ve en
[Funciones de Boole](06-funciones-de-boole.md).

## 4. Cantidad de funciones lógicas posibles

Una pregunta natural es: dadas $n$ variables de entrada, ¿cuántas funciones lógicas distintas
existen?

Con $n$ variables hay $2^n$ combinaciones de entrada, y cada una de esas combinaciones puede tomar,
independientemente de las demás, el valor $0$ o el valor $1$ en la salida. Por lo tanto, la cantidad
de funciones lógicas distintas de $n$ variables es:

$$N(n) = 2^{\left(2^n\right)}$$

| $n$ | Combinaciones de entrada ($2^n$) | Funciones posibles ($2^{2^n}$) |
| :-: | :------------------------------: | :----------------------------: |
|  1  |                2                 |               4                |
|  2  |                4                 |               16               |
|  3  |                8                 |              256               |
|  4  |                16                |             65536              |

```{note} Nota
El crecimiento es doblemente exponencial: al pasar de 3 a 4 variables la cantidad de funciones
posibles pasa de 256 a 65536. Esto es, en el fondo, la razón por la que hacen falta métodos
sistemáticos (tabla de verdad, formas canónicas, mapas de Karnaugh) en lugar de intentar "adivinar"
o memorizar funciones a mano.
```

### 4.1. Funciones de una variable

Con $n=1$ hay $2^1=2$ combinaciones de entrada y $2^{2^1}=4$ funciones posibles:

| Función | $x=0$ | $x=1$ | Nombre                               |
| :-----: | :---: | :---: | ------------------------------------ |
|  $F_0$  |   0   |   0   | Constante $0$                        |
|  $F_1$  |   0   |   1   | Transferencia (identidad): $F_1 = x$ |
|  $F_2$  |   1   |   0   | Negación: $F_2 = x'$                 |
|  $F_3$  |   1   |   1   | Constante $1$                        |

### 4.2. Funciones de dos variables

Con $n=2$ hay $2^2=4$ combinaciones de entrada y $2^{2^2}=16$ funciones posibles. La siguiente tabla
las enumera todas, junto con el nombre que reciben las que son de uso frecuente en diseño lógico:

| Función  | $(x,y){=}00$ | $01$ | $10$ | $11$ | Nombre                        |
| :------: | :----------: | :--: | :--: | :--: | ----------------------------- |
|  $F_0$   |      0       |  0   |  0   |  0   | Constante $0$                 |
|  $F_1$   |      0       |  0   |  0   |  1   | AND: $x \cdot y$              |
|  $F_2$   |      0       |  0   |  1   |  0   | Inhibición: $x \cdot y'$      |
|  $F_3$   |      0       |  0   |  1   |  1   | Transferencia de $x$          |
|  $F_4$   |      0       |  1   |  0   |  0   | Inhibición: $x' \cdot y$      |
|  $F_5$   |      0       |  1   |  0   |  1   | Transferencia de $y$          |
|  $F_6$   |      0       |  1   |  1   |  0   | XOR: $x \oplus y$             |
|  $F_7$   |      0       |  1   |  1   |  1   | OR: $x + y$                   |
|  $F_8$   |      1       |  0   |  0   |  0   | NOR: $(x+y)'$                 |
|  $F_9$   |      1       |  0   |  0   |  1   | XNOR: $(x \oplus y)'$         |
| $F_{10}$ |      1       |  0   |  1   |  0   | Negación de $y$               |
| $F_{11}$ |      1       |  0   |  1   |  1   | Implicación $y \to x$: $x+y'$ |
| $F_{12}$ |      1       |  1   |  0   |  0   | Negación de $x$               |
| $F_{13}$ |      1       |  1   |  0   |  1   | Implicación $x \to y$: $x'+y$ |
| $F_{14}$ |      1       |  1   |  1   |  0   | NAND: $(x \cdot y)'$          |
| $F_{15}$ |      1       |  1   |  1   |  1   | Constante $1$                 |

```{tip} Atención
Notá que las 16 filas de la tabla, leídas de $F_0$ a $F_{15}$, son simplemente los números binarios
de 4 bits contados en orden ($0000, 0001, 0010, \ldots, 1111$). Esta es una manera rápida de
verificar que no falta ni sobra ninguna función: cada patrón de 4 bits en la columna de salida
corresponde a exactamente una función, y hay $2^4=16$ patrones posibles.
```

De estas 16 funciones, las que reciben nombre propio y se implementan como compuertas físicas
dedicadas (AND, OR, NAND, NOR, XOR, XNOR y NOT) son el tema del próximo capítulo.

## 5. Resumen

- Una función lógica de $n$ variables es una función $f:\{0,1\}^n \to \{0,1\}$, completamente
  definida por sus $2^n$ valores de salida.
- La tabla de verdad, la ecuación booleana y el circuito de compuertas son tres representaciones
  equivalentes de la misma función lógica.
- Con $n$ variables existen $2^{2^n}$ funciones lógicas distintas: 4 con una variable, 16 con dos
  variables, 256 con tres variables.
- De las 16 funciones de dos variables, un pequeño subconjunto (AND, OR, NAND, NOR, XOR, XNOR, NOT)
  se usa con tanta frecuencia que se implementa como compuerta física dedicada — tema del
  [próximo capítulo](05-compuertas-logicas.md).

## 6. Ejercicios propuestos

```{exercise}
:label: ex-funclog-1
¿Cuántas funciones lógicas distintas existen de 5 variables de entrada? Expresar el resultado como
potencia de 2 y como número decimal.
```

```{solution} ex-funclog-1
:class: dropdown
$N(5) = 2^{2^5} = 2^{32} = 4294967296$ funciones distintas.
```

```{exercise}
:label: ex-funclog-2
Identificar, en la tabla de funciones de dos variables de la sección 4.2, cuál es la función $F_{13}$ y
escribir su tabla de verdad por separado.
```

```{solution} ex-funclog-2
:class: dropdown
$F_{13} = x' + y$ (implicación $x \to y$). Su tabla de verdad es:

| $x$ | $y$ | $F_{13}$ |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
```

```{exercise}
:label: ex-funclog-3
Dada la función de tres variables de la sección 2.1, construir la tabla de verdad de su función
complementaria $o' = f(x,y,z)'$.
```

```{solution} ex-funclog-3
:class: dropdown
Basta con invertir cada valor de salida de la tabla original:

| $x$ | $y$ | $z$ | $o'$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | **1** |
| 0 | 1 | 0 | **1** |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | **1** |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | **1** |
```

```{exercise}
:label: ex-funclog-4
¿Por qué la cantidad de funciones lógicas de $n$ variables crece como $2^{2^n}$ y no simplemente como
$2^n$?
```

```{solution} ex-funclog-4
:class: dropdown
Porque $2^n$ es la cantidad de **combinaciones de entrada** (filas de la tabla de verdad), no la
cantidad de funciones. Cada una de esas $2^n$ filas puede tener, de forma independiente, salida $0$ o
$1$; por lo tanto la cantidad de tablas de verdad distintas (es decir, de funciones distintas) es
$2$ elevado a la cantidad de filas, o sea $2^{(2^n)}$.
```

## 7. Bibliografía

```{bibliography}
:filter: docname in docnames
```
