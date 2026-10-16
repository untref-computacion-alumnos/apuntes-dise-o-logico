---
title: "Formas Canónicas"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Formas Canónicas

```{admonition} Sobre este apunte
:class: note
Este capítulo desarrolla el método sistemático para pasar de una tabla de verdad a una ecuación
booleana, tal como se presenta en la sección "Funciones lógicas – Tablas de Verdad" de la presentación
de la cátedra. Se reutiliza la misma función de tres variables definida en
[Funciones Lógicas](04-funciones-logicas.md) para que el ejemplo sea comparable entre capítulos. La
notación de índices de minterm/maxterm se completa con bibliografía estándar ({cite}`tocci2007`,
{cite}`floyd2000`).
```

## 1. El problema: de la tabla a la ecuación, sin adivinar

El [capítulo de Funciones Lógicas](04-funciones-logicas.md) estableció que toda tabla de verdad puede
describirse mediante una ecuación booleana, y el [capítulo de Funciones de Boole](06-funciones-de-boole.md)
mostró cómo manipular y simplificar esas ecuaciones una vez que existen. Falta resolver el primer paso:
¿cómo se obtiene **mecánicamente** una ecuación a partir de una tabla de verdad, sin necesidad de
"adivinarla"?

La respuesta son las **formas canónicas**: dos procedimientos —duales entre sí— que producen, siempre,
una ecuación booleana correcta a partir de cualquier tabla de verdad.

### 1.1 Función de trabajo

Se retoma la función de tres variables $o = f(x,y,z)$ ya definida:

| $x$ | $y$ | $z$ | $o$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | **1** |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | **1** |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | **1** |
| 1 | 1 | 0 | **1** |
| 1 | 1 | 1 | 0 |

## 2. Forma canónica disyuntiva (suma de minterms / SOP)

**Estrategia:** se consideran todas las filas en las que la función **vale 1**. Para cada una de esas
filas se construye un producto (**minterm**) que toma cada variable sin complementar si vale 1, y
complementada si vale 0. La función es la **suma (OR)** de todos esos minterms.

Filas donde $o=1$: $(x,y,z) = (0,0,0),\ (0,1,1),\ (1,0,1),\ (1,1,0)$.

$$o = \underbrace{x' \cdot y' \cdot z'}_{\text{minterm}} + x' \cdot y \cdot z + x \cdot y' \cdot z + x \cdot y \cdot z'$$

Esta expresión —suma de minterms— se llama **expresión (o forma) disyuntiva canónica**.

### 2.1 Implementación mediante compuertas lógicas

Cada minterm se implementa con una compuerta **AND de 3 entradas** (usando las entradas complementadas
donde corresponda mediante compuertas NOT), y los cuatro minterms se combinan con una compuerta **OR de
4 entradas**:

```text
x,y,z ─┬─[NOT]──┐
       │        │
x' y' z' ──[AND3]──┐
x' y  z  ──[AND3]──┤
x  y' z  ──[AND3]──┼─[OR4]── o
x  y  z' ──[AND3]──┘
```

Esta estructura de dos niveles —**AND (nivel 1) seguido de OR (nivel 2)**— es la forma canónica de
implementación conocida como **suma de productos** (*Sum of Products*, SOP), y es directamente
sintetizable a partir de cualquier tabla de verdad sin necesidad de simplificación previa.

## 3. Forma canónica conjuntiva (producto de maxterms / POS)

**Estrategia alternativa:** se consideran todas las filas en las que la función **no se cumple** (vale
0), y se trabaja sobre el complemento $o' = f(x,y,z)'$.

Filas donde $o=0$: $(x,y,z) = (0,0,1),\ (0,1,0),\ (1,0,0),\ (1,1,1)$.

$$o' = x' \cdot y' \cdot z + x' \cdot y \cdot z' + x \cdot y' \cdot z' + x \cdot y \cdot z$$

Esta es la **expresión disyuntiva** de $o'$ (suma de los minterms de $o'$). Para obtener $o$, se niega
toda la expresión y se aplican las leyes de De Morgan (ver
[Funciones de Boole](06-funciones-de-boole.md), sección 4) paso a paso:

$$o = \left(x' y' z + x' y z' + x y' z' + x y z\right)'$$

Aplicando De Morgan a la negación de una suma —se convierte en producto de negaciones—:

$$o = (x' y' z)' \cdot (x' y z')' \cdot (x y' z')' \cdot (x y z)'$$

Aplicando De Morgan nuevamente a cada término —la negación de un producto se convierte en suma de
negaciones—:

$$o = (x + y + z') \cdot (x + y' + z) \cdot (x' + y + z) \cdot (x' + y' + z')$$

Cada uno de estos factores es un **maxterm**, y el resultado —producto de maxterms— es la **expresión
(o forma) conjuntiva canónica**:

$$o = \underbrace{(x+y+z')}_{\text{maxterm}} \cdot (x+y'+z) \cdot (x'+y+z) \cdot (x'+y'+z')$$

```{admonition} Relación minterm ↔ maxterm
:class: tip
Cada maxterm es el **complemento del minterm correspondiente a la misma combinación de variables** (vía
De Morgan): la fila $(x,y,z)=(0,0,1)$, cuyo minterm sería $x'y'z$, da origen al maxterm $(x+y+z')$. La
forma conjuntiva se construye con las filas donde $o=0$, exactamente al revés que la forma disyuntiva.
```

### 3.1 Implementación mediante compuertas lógicas

Esta estructura de dos niveles —**OR (nivel 1) seguido de AND (nivel 2)**— se conoce como **producto de
sumas** (*Product of Sums*, POS), y es la implementación dual de la forma SOP vista en la sección
anterior:

```text
x,y,z ─┬─[NOT]──┐
       │        │
(x +y +z') ──[OR3]──┐
(x +y'+z ) ──[OR3]──┤
(x'+y +z ) ──[OR3]──┼─[AND4]── o
(x'+y'+z') ──[OR3]──┘
```

## 4. Notación abreviada: índices de minterm y maxterm

Cuando la cantidad de variables crece, escribir cada minterm o maxterm completo se vuelve tedioso.
Existe una notación abreviada, muy usada en bibliografía y en enunciados de ejercicios
{cite}`tocci2007`: se numera cada combinación de $(x,y,z)$ con el valor decimal que representa como
número binario, y se listan solo esos índices.

| $x$ | $y$ | $z$ | Índice | Minterm | Maxterm |
|:---:|:---:|:---:|:---:|---|---|
| 0 | 0 | 0 | 0 | $m_0=x'y'z'$ | $M_0=x+y+z$ |
| 0 | 0 | 1 | 1 | $m_1=x'y'z$ | $M_1=x+y+z'$ |
| 0 | 1 | 0 | 2 | $m_2=x'yz'$ | $M_2=x+y'+z$ |
| 0 | 1 | 1 | 3 | $m_3=x'yz$ | $M_3=x+y'+z'$ |
| 1 | 0 | 0 | 4 | $m_4=xy'z'$ | $M_4=x'+y+z$ |
| 1 | 0 | 1 | 5 | $m_5=xy'z$ | $M_5=x'+y+z'$ |
| 1 | 1 | 0 | 6 | $m_6=xyz'$ | $M_6=x'+y'+z$ |
| 1 | 1 | 1 | 7 | $m_7=xyz$ | $M_7=x'+y'+z'$ |

Con esta notación, la función de trabajo de este capítulo (que vale 1 en las filas $0,3,5,6$ y vale 0 en
las filas $1,2,4,7$) se escribe:

$$o = \sum m(0,3,5,6) = \prod M(1,2,4,7)$$

```{note}
Fijate que los índices de la forma $\Sigma m$ (donde $o=1$) y los de la forma $\Pi M$ (donde $o=0$) son
exactamente **complementarios** entre sí dentro del rango $0$ a $2^n-1$: entre ambos cubren todas las
filas de la tabla de verdad, sin superponerse.
```

## 5. Las formas canónicas no son la implementación óptima

```{warning}
Las formas canónicas garantizan que **siempre** se puede pasar de una tabla de verdad a un circuito de
dos niveles, pero casi nunca son la implementación más económica. Por ejemplo, la forma SOP de este
capítulo usa 4 compuertas AND de 3 entradas más una OR de 4 entradas, cuando en realidad —como se ve en
el [capítulo de Redundancias](08-redundancias.md)— la misma función puede simplificarse a una expresión
bastante más corta usando mapas de Karnaugh.
```

Las formas canónicas son, sin embargo, el punto de partida imprescindible: son el único método que
garantiza no perder ni agregar información respecto de la tabla de verdad original. Toda técnica de
simplificación (algebraica, Karnaugh, Quine–McCluskey) parte, conceptualmente, de la forma canónica.

## 6. Resumen

- Toda tabla de verdad tiene una forma canónica disyuntiva (SOP, suma de minterms de las filas en 1) y
  una forma canónica conjuntiva (POS, producto de maxterms de las filas en 0), ambas obtenidas de forma
  puramente mecánica.
- Minterm y maxterm de una misma fila son complementarios entre sí (De Morgan).
- La notación $\Sigma m(\ldots)$ / $\Pi M(\ldots)$ permite escribir formas canónicas de forma compacta
  usando los índices decimales de las filas.
- Las formas canónicas rara vez son la implementación más económica; sirven como punto de partida para
  los métodos de simplificación del [próximo capítulo](08-redundancias.md).

## 7. Ejercicios propuestos

```{exercise}
:label: ex-canon-1
Escribir, en notación de índices, la forma canónica disyuntiva y conjuntiva de una función de 2
variables $g(x,y)$ cuya tabla de verdad vale 1 solo cuando $x=y$ (es decir, $g$ es la compuerta XNOR).
```

```{solution} ex-canon-1
:class: dropdown
$g$ vale 1 en $(x,y)=(0,0)$ e $(1,1)$, índices 0 y 3. Vale 0 en los índices 1 y 2. Por lo tanto
$g = \sum m(0,3) = \prod M(1,2)$.
```

```{exercise}
:label: ex-canon-2
A partir de $o = \sum m(0,3,5,6)$ (la función de trabajo de este capítulo), escribir explícitamente el
minterm $m_5$ y el maxterm $M_5$, y verificar que $M_5$ es el complemento de $m_5$.
```

```{solution} ex-canon-2
:class: dropdown
Índice 5 en binario (3 bits) es $101$, es decir $x=1,y=0,z=1$. Entonces $m_5 = x \cdot y' \cdot z$ y
$M_5 = x' + y + z'$. Aplicando De Morgan: $m_5' = (x\cdot y'\cdot z)' = x'+y+z' = M_5$. Efectivamente
coinciden.
```

```{exercise}
:label: ex-canon-3
Obtener la forma canónica disyuntiva de la función NAND de 2 entradas, $o=(x\cdot y)'$.
```

```{solution} ex-canon-3
:class: dropdown
La NAND vale 1 en 3 de las 4 filas: $(0,0),(0,1),(1,0)$, índices 0,1,2. Por lo tanto
$o = \sum m(0,1,2) = x'y' + x'y + xy'$.
```

```{exercise}
:label: ex-canon-4
¿Cuántos minterms tiene, como máximo, la forma canónica disyuntiva de una función de 4 variables? ¿En
qué caso se alcanza ese máximo?
```

```{solution} ex-canon-4
:class: dropdown
Como máximo $2^4=16$ minterms (uno por cada fila de la tabla de verdad). Ese máximo se alcanza cuando la
función vale 1 en **todas** las filas, es decir, cuando la función es la constante $1$.
```

## 8. Bibliografía

```{bibliography}
:filter: docname in docnames
```
