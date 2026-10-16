---
title: "Funciones de Boole"
subject: "Diseño Lógico"
---

# Funciones de Boole

```{admonition} Sobre este apunte
:class: note
Este capítulo desarrolla el marco algebraico formal (álgebra de Boole: historia, axiomas y
teoremas). Se agregan demostraciones paso a paso de algunos teoremas y ejemplos de simplificación
algebraica, con apoyo de bibliografía estándar ({cite}`tocci2007`, {cite}`floyd2000`).
```

## 1. George Boole y el nacimiento del álgebra de la lógica

En **1847**, George Boole (1815–1864), matemático y lógico autodidacta británico, publica _"Análisis
matemático de la lógica, ensayo de un cálculo de razonamiento deductivo"_. Sus ideas centrales son:

- La **lógica** puede tratarse como una rama de las matemáticas.
- Los razonamientos lógicos están sujetos a leyes matemáticas y pueden representarse y analizarse
  como **ecuaciones matemáticas**.
- Esta álgebra no opera sobre números en el sentido usual, sino sobre **clases de objetos**, y
  cumple la propiedad particular $x^2 = x$ (idempotencia).

Más adelante surge la **lógica booleana de los silogismos**, que representa cada silogismo y su
conclusión mediante una ecuación matemática.

## 2. El álgebra de Boole como estructura algebraica

En **1860**, en trabajos posteriores de **Charles S. Peirce** (1839–1914) y **William Stanley
Jevons** (1835–1882), aparece el concepto más general de **"álgebra de Boole"** como estructur
algebraica abstracta.

Formalmente, un álgebra de Boole es:

- Un conjunto $B$ con (al menos) dos elementos distinguibles: $0$ y $1$.
- Dados dos elementos $x, y \in B$, se definen dos operaciones binarias: $x + y$ (suma / OR) y
  $x \cdot y$ (producto / AND).
- Se define además una operación unaria de **negación** (complemento): $x'$, $y'$.

El **álgebra de conjuntos** y el **cálculo proposicional** son ejemplos clásicos de álgebras de
Boole: ambos satisfacen los axiomas y teoremas que caracterizan esta estructura.

```{note} Nota
En el álgebra de conjuntos, $+$ corresponde a la unión, $\cdot$ a la intersección, $'$ al
complemento, $0$ al conjunto vacío y $1$ al conjunto universal. En el cálculo proposicional, $+$
corresponde a "o" lógico, $\cdot$ a "y" lógico, $'$ a la negación, $0$ a "falso" y $1$ a
"verdadero". El diseño lógico usa la misma álgebra aplicada a **señales digitales**: $0$ y $1$ son
los dos niveles de tensión posibles.
```

## 3. Axiomas

| Propiedad       | Forma con "+" (OR)                | Forma con "·" (AND)                         |
| --------------- | --------------------------------- | ------------------------------------------- |
| Conmutatividad  | $x+y = y+x$                       | $x \cdot y = y \cdot x$                     |
| Asociatividad   | $x+(y+z) = (x+y)+z$               | $x \cdot (y \cdot z) = (x \cdot y) \cdot z$ |
| Distributividad | $x+(y \cdot z) = (x+y)\cdot(x+z)$ | $x \cdot (y+z) = (x \cdot y)+(x \cdot z)$   |
| Elemento neutro | $x+0 = x$                         | $x \cdot 1 = x$                             |
| Complementario  | $x + x' = 1$                      | $x \cdot x' = 0$                            |

```{important}
A diferencia del álgebra de números reales, en el álgebra de Boole **la suma también distribuye sobre
el producto** ($x+(y\cdot z) = (x+y)\cdot(x+z)$), no solo el producto sobre la suma. Esta simetría entre
$+$ y $\cdot$ es la base del **principio de dualidad** (sección 5): toda identidad booleana sigue siendo
válida si se intercambian simultáneamente $+ \leftrightarrow \cdot$ y $0 \leftrightarrow 1$.
```

## 4. Teoremas derivados

Los siguientes teoremas no son axiomas independientes: se pueden **demostrar** a partir de los cinco
axiomas de la sección anterior.

| Teorema        | Forma con "+" (OR)     | Forma con "·" (AND)      |
| -------------- | ---------------------- | ------------------------ |
| Idempotencia   | $x+x = x$              | $x \cdot x = x$          |
| Absorción      | $x+1 = 1$              | $x \cdot 0 = 0$          |
| Complementario | $1' = 0$               | $0' = 1$                 |
| Involución     | $(x')' = x$            | $(x')' = x$              |
| **De Morgan**  | $(x+y)' = x' \cdot y'$ | $(x \cdot y)' = x' + y'$ |

Las **leyes de De Morgan** son especialmente importantes en el diseño digital porque permiten convertir
entre expresiones basadas en AND/OR y expresiones basadas en NAND/NOR, algo fundamental al sintetizar
circuitos con una única familia de compuertas (ver [Compuertas Lógicas](05-compuertas-logicas.md),
sección 5).

### 4.1 Demostración: idempotencia

$$
\begin{aligned}
x+x &= (x+x)\cdot 1 &&\text{(elemento neutro del producto)}\\
    &= (x+x)\cdot(x+x') &&\text{(complementario: } x+x'=1\text{)}\\
    &= x+(x\cdot x') &&\text{(distributividad)}\\
    &= x+0 &&\text{(complementario: } x\cdot x'=0\text{)}\\
    &= x &&\text{(elemento neutro de la suma)}
\end{aligned}
$$

### 4.2 Demostración: absorción ($x+1=1$)

$$
\begin{aligned}
x+1 &= x+(x+x') &&\text{(complementario: } x+x'=1\text{)}\\
    &= (x+x)+x' &&\text{(asociatividad)}\\
    &= x+x' &&\text{(idempotencia, ya demostrada)}\\
    &= 1 &&\text{(complementario)}
\end{aligned}
$$

```{tip}
Casi todos los teoremas de la tabla se demuestran con el mismo recurso: "inflar" la expresión usando el
elemento neutro o el complementario, aplicar distributividad, y luego "deshinchar" con idempotencia o
complementario. Vale la pena practicar la demostración de $x \cdot 0 = 0$ (dual de la de $x+1=1$) como
ejercicio.
```

## 5. Principio de dualidad

El **principio de dualidad** establece que toda identidad booleana válida sigue siendo válida si se
intercambian simultáneamente:

- $+ \leftrightarrow \cdot$
- $0 \leftrightarrow 1$

(las variables y los complementos no se tocan). Esto explica por qué en las tablas de axiomas y
teoremas de este apunte cada fila viene en pares: cada identidad de la columna "+" es la **dual** de la
correspondiente en la columna "·".

**Ejemplo.** Partiendo del axioma de distributividad

$$x+(y \cdot z) = (x+y)\cdot(x+z)$$

al aplicar dualidad ($+\to\cdot$, $\cdot\to+$) se obtiene exactamente el otro axioma de distributividad:

$$x \cdot (y+z) = (x \cdot y)+(x \cdot z)$$

```{note}
La dualidad es una herramienta práctica: si ya se demostró un teorema, su dual queda demostrado "gratis"
—simplemente se dualiza cada paso de la demostración original—. No hace falta rehacer todo el trabajo.
```

## 6. Simplificación algebraica de expresiones

Los axiomas y teoremas anteriores permiten simplificar ecuaciones booleanas sin necesidad de recurrir a
un método gráfico o tabular. Tres ejemplos trabajados:

**Ejemplo 1.** Simplificar $F = x \cdot y + x \cdot y'$.

$$F = x \cdot y + x \cdot y' = x \cdot (y+y') = x \cdot 1 = x$$

**Ejemplo 2 (absorción extendida).** Simplificar $F = x + x' \cdot y$.

$$
\begin{aligned}
F = x + x' \cdot y &= (x+x') \cdot (x+y) &&\text{(distributividad de la suma sobre el producto)}\\
    &= 1 \cdot (x+y) &&\text{(complementario)}\\
    &= x+y &&\text{(elemento neutro)}
\end{aligned}
$$

```{important}
Este segundo ejemplo es exactamente el caso en el que la distributividad de la suma sobre el producto
—la que **no existe** en el álgebra de números reales— resulta indispensable. Sin ella no habría forma
de "sacar factor común" en una expresión de la forma $x + x' \cdot y$.
```

**Ejemplo 3 (factoreo inverso).** Simplificar $F = (x+y) \cdot (x+y')$.

$$F = (x+y)\cdot(x+y') = x + (y \cdot y') = x + 0 = x$$

Estos tres ejemplos son manipulaciones puntuales; para funciones con más variables, "ver" la
simplificación óptima a simple vista se vuelve difícil. El
[capítulo de Redundancias](08-redundancias.md) presenta un método gráfico sistemático (mapas de
Karnaugh) para resolver ese problema de forma ordenada.

Antes de eso, el [próximo capítulo](07-formas-canonicas.md) muestra cómo pasar de **cualquier** tabla de
verdad a una ecuación booleana de forma mecánica, sin necesidad de "adivinar" ni simplificar: las formas
canónicas.

## 7. Resumen

- El álgebra de Boole es una estructura algebraica sobre un conjunto $\{0,1\}$ con operaciones $+$,
  $\cdot$ y $'$, gobernada por cinco axiomas (conmutatividad, asociatividad, distributividad, elemento
  neutro, complementario).
- A partir de esos axiomas se demuestran teoremas útiles para simplificar circuitos: idempotencia,
  absorción, involución y las leyes de De Morgan.
- El principio de dualidad permite obtener automáticamente la identidad "espejo" de cualquier teorema
  ya demostrado, intercambiando $+\leftrightarrow\cdot$ y $0\leftrightarrow1$.
- La manipulación algebraica directa permite simplificar expresiones puntuales, pero no escala bien a
  funciones de muchas variables; para eso existen métodos sistemáticos como los mapas de Karnaugh.

## 8. Ejercicios propuestos

```{exercise}
:label: ex-boole-1
Demostrar el teorema dual de la absorción, $x \cdot 0 = 0$, a partir de los axiomas.
```

```{solution} ex-boole-1
:class: dropdown
$$
\begin{aligned}
x \cdot 0 &= x \cdot (x \cdot x') &&\text{(complementario: } x\cdot x'=0\text{)}\\
          &= (x \cdot x) \cdot x' &&\text{(asociatividad)}\\
          &= x \cdot x' &&\text{(idempotencia)}\\
          &= 0 &&\text{(complementario)}
\end{aligned}
$$
```

```{exercise}
:label: ex-boole-2
Obtener el dual de la expresión $x \cdot (y+z') + w$.
```

```{solution} ex-boole-2
:class: dropdown
Intercambiando $+\leftrightarrow\cdot$: $\;x + (y \cdot z') \cdot w$. (Las variables y sus
complementos no cambian.)
```

```{exercise}
:label: ex-boole-3
Simplificar algebraicamente $F = x \cdot y + x \cdot y \cdot z + x'$.
```

```{solution} ex-boole-3
:class: dropdown
Primero, $x \cdot y + x \cdot y \cdot z = x \cdot y \cdot (1+z) = x \cdot y \cdot 1 = x \cdot y$ (usando
absorción $1+z=1$). Luego $F = x \cdot y + x'$, y por el Ejemplo 2 de la sección 6 (con $x\to x'$,
$y\to y$) esto es $F = x' + y$.
```

```{exercise}
:label: ex-boole-4
Demostrar la ley de De Morgan $(x \cdot y)' = x' + y'$ verificando que ambos lados coinciden en las
cuatro combinaciones de $x,y$ (demostración por tabla de verdad).
```

```{solution} ex-boole-4
:class: dropdown

| $x$ | $y$ | $x \cdot y$ | $(x\cdot y)'$ | $x'$ | $y'$ | $x'+y'$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

Las columnas $(x\cdot y)'$ y $x'+y'$ coinciden fila a fila, por lo tanto las expresiones son
equivalentes.
```

## 9. Bibliografía

```{bibliography}
:filter: docname in docnames
```
