---
title: "Códigos Binarios"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Códigos Binarios

```{admonition} Sobre este apunte
:class: note
Este capítulo no proviene de manera directa de las presentaciones de la cátedra: desarrolla,
a partir de bibliografía estándar de Diseño Lógico ({cite}`tocci2007`, {cite}`floyd2000`,
{cite}`mandado1998`), el marco teórico general de los **códigos binarios**. Es la base
conceptual sobre la que se apoyan los dos capítulos siguientes: [Códigos numéricos](12-codigos-numericos.md)
y [Códigos alfanuméricos](13-codigos-alfanumericos.md), que presentan códigos concretos.
```

## 1. Qué es un código

En sistemas digitales, la información (números, letras, símbolos, estados de un proceso) debe
representarse mediante combinaciones de bits. Un **código** es, precisamente, la regla de
asignación entre cada elemento de un conjunto de información y una combinación particular de
bits (una **palabra código**).

```{important}
Un código no es una propiedad intrínseca de la información, sino una **convención**: la misma
cantidad de información puede codificarse de muchas maneras distintas (BCD, Gray, ASCII, etc.),
cada una con ventajas para un propósito específico (aritmética, transmisión, detección de
errores, posicionamiento mecánico, etc.).
```

Formalmente, un código es una función inyectiva

$$C : E \to \{0,1\}^n$$

que asigna a cada elemento de un conjunto finito de información $E$ (por ejemplo, los dígitos
decimales $\{0,1,\dots,9\}$, o el alfabeto latino) una palabra de $n$ bits. Con $n$ bits existen
$2^n$ palabras código posibles, por lo que para codificar $|E|$ elementos se necesita como mínimo

$$n = \lceil \log_2 |E| \rceil \text{ bits.}$$

## 2. Códigos ponderados y no ponderados

### 2.1 Códigos ponderados

En un **código ponderado**, a cada posición (bit) del código se le asigna un **peso**, y el
valor representado se obtiene como la suma de los pesos de las posiciones que valen 1. El
código binario natural es el ejemplo más directo: el bit en la posición $i$ tiene peso $2^i$.

$$N = \sum_{i=0}^{n-1} b_i \cdot 2^i$$

Otros códigos ponderados (que se desarrollan en el próximo capítulo) usan pesos distintos a las
potencias de 2 —por ejemplo, el código Aiken usa los pesos $2,4,2,1$— pero conservan la idea de
que el valor se reconstruye sumando pesos.

### 2.2 Códigos no ponderados

En un **código no ponderado**, no existe una regla aritmética de pesos que permita reconstruir
el valor representado a partir de la posición de los bits: la asignación es arbitraria o sigue
otro criterio (por ejemplo, minimizar la cantidad de bits que cambian entre palabras
consecutivas). El código Gray y el código exceso-3 (capítulo 12) son los ejemplos clásicos.

| Criterio | Código ponderado | Código no ponderado |
|---|---|---|
| Reconstrucción del valor | Suma de pesos $\times$ bit | No hay fórmula aritmética directa |
| Ejemplo | Binario natural, BCD, Aiken (2421) | Gray, exceso-3 |
| Uso típico | Aritmética | Detección de errores, posicionamiento, autocomplemento |

## 3. Distancia de Hamming

Dos palabras código de igual longitud pueden compararse contando en cuántas posiciones
difieren. Esa cantidad se llama **distancia de Hamming**.

```{admonition} Definición: distancia de Hamming
:class: note
Dadas dos palabras binarias $A$ y $B$ de $n$ bits, la distancia de Hamming $d(A,B)$ es la
cantidad de posiciones en las que $A$ y $B$ tienen bits distintos. Equivale a la cantidad de
unos en $A \oplus B$ (la suma XOR bit a bit).
```

Por ejemplo, entre $A=1011$ y $B=1001$: $A \oplus B = 0010$, por lo que $d(A,B)=1$.

La distancia de Hamming es la base teórica de la **detección y corrección de errores**: si un
código se diseña de manera que la distancia mínima entre dos palabras válidas cualesquiera sea
$d_{min}$, entonces:

- Con $d_{min} \geq 2$ se pueden **detectar** hasta $d_{min}-1$ errores de bit.
- Con $d_{min} \geq 3$ se pueden **corregir** hasta $\lfloor (d_{min}-1)/2 \rfloor$ errores de bit.

```{note}
El binario natural sin ningún bit adicional tiene $d_{min}=1$ entre palabras consecutivas (por
ejemplo, $0111 \to 1000$ cambia los 4 bits, pero entre $0011$ y $0100$ también hay más de un bit
distinto): no ofrece ninguna capacidad de detección de errores por sí mismo. Por eso se agregan
bits redundantes, como el bit de paridad.
```

El desarrollo completo de códigos correctores de errores (por ejemplo, Hamming como algoritmo)
excede el nivel de este curso introductorio; alcanza con comprender el concepto de distancia
mínima como fundamento de por qué algunos códigos "detectan" y otros no.

## 4. Bit de paridad

La técnica de detección de errores más simple es agregar un **bit de paridad** a la palabra
código original, elegido de manera que la cantidad total de unos (incluyendo el bit agregado)
sea siempre par (**paridad par**) o siempre impar (**paridad impar**).

$$p = b_{n-1} \oplus b_{n-2} \oplus \dots \oplus b_0 \qquad \text{(paridad par)}$$

### Ejemplo

Para la palabra $1011000$ (cuatro unos):

- Con **paridad par**: como ya hay una cantidad par de unos, se agrega $p=0$ → palabra
  transmitida $10110000$.
- Con **paridad impar**: se agrega $p=1$ para que el total de unos sea impar → palabra
  transmitida $10110001$.

En el receptor, se vuelve a calcular la paridad de los bits recibidos y se compara contra la
convención acordada; si no coincide, se detectó un error de un bit (o de una cantidad impar de
bits, ya que un número par de errores puede pasar inadvertido).

```{warning}
El bit de paridad **detecta** errores de un número impar de bits, pero **no indica en qué
posición** ocurrió el error ni permite corregirlo. Para eso se necesitan esquemas más elaborados
(matrices de paridad, códigos de Hamming), fuera del alcance de este curso.
```

## 5. Códigos reflejados: una idea que se retoma en el próximo capítulo

Una familia importante de códigos no ponderados son los **códigos reflejados** (o de distancia
unitaria), diseñados de manera que **entre dos palabras código consecutivas cambia un único
bit**. Esta propiedad es muy valiosa en aplicaciones donde la variable representada cambia de a
pequeños pasos (por ejemplo, la posición de un eje mecánico) y se quiere evitar que un error de
lectura transitorio en varios bits simultáneos produzca una lectura completamente errónea.

El ejemplo más importante de código reflejado es el **código Gray**, que se desarrolla en
detalle —con su algoritmo de conversión y sus aplicaciones— en el capítulo de
[Códigos numéricos](12-codigos-numericos.md).

## 6. Resumen

- Un código es una asignación (función inyectiva) entre elementos de información y palabras de
  $n$ bits; se necesitan al menos $\lceil \log_2 |E| \rceil$ bits para codificar $|E|$
  elementos.
- Los códigos se clasifican en **ponderados** (el valor se reconstruye sumando pesos por
  posición, como el binario natural o BCD) y **no ponderados** (sin esa regla aritmética, como
  Gray o exceso-3).
- La **distancia de Hamming** mide en cuántos bits difieren dos palabras, y su valor mínimo
  dentro de un código determina cuántos errores se pueden detectar o corregir.
- El **bit de paridad** es el mecanismo de detección de errores más simple: agrega un bit para
  fijar la paridad (par o impar) de la cantidad de unos.
- Los **códigos reflejados** (como Gray) cambian un solo bit entre palabras consecutivas, lo que
  los hace ideales para mediciones físicas continuas.
- Estos conceptos generales se aplican en los capítulos siguientes: [Códigos numéricos](12-codigos-numericos.md)
  (BCD, Aiken, exceso-3, Gray) y [Códigos alfanuméricos](13-codigos-alfanumericos.md) (ASCII).

## 7. Ejercicios propuestos

```{exercise}
:label: ex-codbin-1
Calcular la distancia de Hamming entre las palabras $A = 110101$ y $B = 100111$.
```

```{solution} ex-codbin-1
:class: dropdown
$A \oplus B = 010010$, que tiene dos unos. Por lo tanto $d(A,B) = 2$.
```

```{exercise}
:label: ex-codbin-2
¿Cuántos bits como mínimo se necesitan para codificar en binario natural los 26 caracteres del
alfabeto latino (sin mayúsculas/minúsculas ni símbolos adicionales)?
```

```{solution} ex-codbin-2
:class: dropdown
Se necesita $n$ tal que $2^n \geq 26$. Como $2^4=16 < 26$ y $2^5=32 \geq 26$, se necesitan
$n=5$ bits (con 6 combinaciones sin usar).
```

```{exercise}
:label: ex-codbin-3
Calcular el bit de paridad par e impar para la palabra $1100101$.
```

```{solution} ex-codbin-3
:class: dropdown
La palabra tiene cuatro unos (cantidad par). Para paridad par, $p=0$ (queda par). Para paridad
impar, $p=1$ (para que el total pase a ser impar).
```

```{exercise}
:label: ex-codbin-4
Un código utiliza palabras de 4 bits pero solo usa 10 de las 16 combinaciones posibles para
representar los dígitos decimales. Indicar a qué familia de códigos (ponderados o no
ponderados) podría pertenecer, sabiendo que el valor se puede reconstruir sumando los pesos
$8,4,2,1$ de las posiciones en 1.
```

```{solution} ex-codbin-4
:class: dropdown
Es un código **ponderado**: los pesos $8,4,2,1$ corresponden exactamente al BCD natural (ver
[Códigos numéricos](12-codigos-numericos.md)), donde el valor decimal se reconstruye sumando
los pesos de los bits en 1.
```

## 8. Bibliografía

```{bibliography}
:filter: docname in docnames
```
