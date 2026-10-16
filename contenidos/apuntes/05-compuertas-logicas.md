---
title: "Compuertas lógicas"
subject: "Diseño Lógico"
---

# Compuertas lógicas

```{admonition} Sobre este apunte
:class: note
Las tablas de verdad y ecuaciones de las seis compuertas básicas (NOT, AND, OR, XOR, NAND, NOR)
provienen directamente de la presentación "Introducción a los sistemas digitales" de la cátedra. El
resto del capítulo (símbolos, compuertas universales, XNOR, familias lógicas) se completa con
bibliografía estándar de la materia ({cite}`tocci2007`, {cite}`floyd2000`, {cite}`mandado1998`).
```

## 1. De la función a la compuerta

Una **compuerta lógica** (_logic gate_) es la implementación física de una función booleana básica.
Mientras que el [capítulo anterior](04-funciones-logicas.md) mostró que existen 16 funciones
posibles de dos variables, solo un puñado de ellas se fabrica como dispositivo dedicado, porque
alcanzan para construir (combinándolas) cualquiera de las 16 (y, en general, cualquier función de
cualquier cantidad de variables). Ese subconjunto es: **NOT**, **AND**, **OR** (las básicas) y
**NAND**, **NOR**, **XOR** (derivadas de uso frecuente).

## 2. Compuertas básicas

### 2.1. Compuerta NOT (negación)

$$
o = x'
$$

```{image} ../../imagenes/not.svg
:alt: NOT
:width: 50%
:align: center
```

| $x$ | $o$ |
| :-: | :-: |
|  0  |  1  |
|  1  |  0  |

### 2.2. Compuerta AND (conjunción)

$$
o = x \cdot y
$$

```{image} ../../imagenes/and.svg
:alt: AND
:width: 50%
:align: center
```

| $x$ | $y$ | $o$ |
| :-: | :-: | :-: |
|  0  |  0  |  0  |
|  0  |  1  |  0  |
|  1  |  0  |  0  |
|  1  |  1  |  1  |

### 2.3. Compuerta OR (disyunción)

$$
o = x + y
$$

```{image} ../../imagenes/or.svg
:alt: OR
:width: 50%
:align: center
```

| $x$ | $y$ | $o$ |
| :-: | :-: | :-: |
|  0  |  0  |  0  |
|  0  |  1  |  1  |
|  1  |  0  |  1  |
|  1  |  1  |  1  |

## 3. Compuertas derivadas

### 3.1. Compuerta XOR (disyunción exclusiva)

$$
o = x \oplus y
$$

```{image} ../../imagenes/xor.svg
:alt: XOR
:width: 50%
:align: center
```

| $x$ | $y$ | $o$ |
| :-: | :-: | :-: |
|  0  |  0  |  0  |
|  0  |  1  |  1  |
|  1  |  0  |  1  |
|  1  |  1  |  0  |

La salida vale 1 únicamente cuando las entradas son **distintas** entre sí.

### 3.2. Compuerta NAND (NOT - AND)

$$
o = (x \cdot y)'
$$

```{image} ../../imagenes/nand.svg
:alt: NAND
:width: 50%
:align: center
```

| $x$ | $y$ | $o$ |
| :-: | :-: | :-: |
|  0  |  0  |  1  |
|  0  |  1  |  1  |
|  1  |  0  |  1  |
|  1  |  1  |  0  |

### 3.3. Compuerta NOR (NOT - OR)

$$
o = (x + y)'
$$

```{image} ../../imagenes/nor.svg
:alt: NOR
:width: 50%
:align: center
```

| $x$ | $y$ | $o$ |
| :-: | :-: | :-: |
|  0  |  0  |  1  |
|  0  |  1  |  0  |
|  1  |  0  |  0  |
|  1  |  1  |  0  |

### 3.4. Compuerta XNOR (disyunción exclusiva negada, o compuerta de equivalencia)

$$
o = (x \oplus y)'
$$

```{image} ../../imagenes/xnor.svg
:alt: XNOR
:width: 50%
:align: center
```

| $x$ | $y$ | $o$ |
| :-: | :-: | :-: |
|  0  |  0  |  1  |
|  0  |  1  |  0  |
|  1  |  0  |  0  |
|  1  |  1  |  1  |

La salida vale 1 únicamente cuando las entradas son **iguales** entre sí; por eso también se la
llama "compuerta de coincidencia" o de equivalencia lógica.

```{note} Nota
Todas las compuertas anteriores se extienden naturalmente a más de dos entradas: una AND de $n$
entradas vale 1 solo si **todas** sus entradas valen 1, una OR de $n$ entradas vale 1 si **al menos
una** de sus entradas vale 1, y análogamente para NAND y NOR (con la salida invertida respecto de
AND/OR). XOR de $n$ entradas vale 1 cuando la cantidad de entradas en 1 es **impar**, por eso se la
usa como base de los circuitos generadores/verificadores de paridad.
```

## 4. Símbolos y representación gráfica

Además de la tabla de verdad y la ecuación, cada compuerta tiene un símbolo gráfico normalizado que
se usa para dibujar esquemáticos de circuitos. La norma más difundida es la **ANSI/IEEE Std 91**
(símbolos "clásicos": forma de D para AND, forma curva para OR, triángulo con círculo para NOT),
aunque también existen los símbolos rectangulares de la norma IEC/CEI usados en algunos entornos de
diseño {cite}`tocci2007`.

## 5. NAND y NOR: compuertas universales

```{important} Importante
NAND y NOR se llaman **compuertas universales:** cualquier función booleana, sin importar cuántas
variables tenga, puede implementarse usando **exclusivamente** compuertas NAND, o **exclusivamente**
compuertas NOR. Esta propiedad (sumada a que son las compuertas más simples y baratas de fabricar en
silicio) es la razón por la que son tan usadas en la fabricación real de circuitos integrados.
```

### 5.1. NOT, AND y OR a partir de NAND

Basta con atar ambas entradas de una NAND para obtener un inversor, y luego usar De Morgan para
derivar AND y OR:

NOT a partir de NAND

```{image} ../../imagenes/not-with-nand.svg
:alt: NOT WITH NAND
:width: 50%
:align: center
```

AND a partir de NAND

```{image} ../../imagenes/and-with-nand.svg
:alt: AND WITH NAND
:width: 50%
:align: center
```

OR a partir de NAND

```{image} ../../imagenes/or-with-nand.svg
:alt: OR WITH NAND
:width: 50%
:align: center
```

### 5.2 NOT, OR y AND a partir de NOR

De manera dual, atando las entradas de una NOR se obtiene un inversor, y con De Morgan se derivan OR
y AND:

NOT a partir de NOR:

```{image} ../../imagenes/not-with-nor.svg
:alt: NOT WITH NOR
:width: 50%
:align: center
```

AND a partir de NOR:

```{image} ../../imagenes/and-with-nor.svg
:alt: AND WITH NOR
:width: 50%
:align: center
```

OR a partir de NOR:

```{image} ../../imagenes/or-with-nor.svg
:alt: OR WITH NOR
:width: 50%
:align: center
```

## 6. Niveles lógicos y familias lógicas

Hasta acá se trabajó con las compuertas como bloques abstractos que solo conocen $0$ y $1$.
Físicamente, esos dos valores se representan con dos rangos de tensión eléctrica bien separados (por
ejemplo, cerca de 0V para el "0" y cerca de la tensión de alimentación para el "1"). Las familias
lógicas más difundidas históricamente son:

- **TTL** (_Transistor-Transistor Logic_): basada en transistores bipolares, alimentación típica de 5V.
- **CMOS** (_Complementary Metal-Oxide-Semiconductor_): basada en transistores de efecto de campo,
  menor consumo, es la base de casi toda la electrónica digital actual (incluidas las FPGAs que se
  ven en [Lógica programable](23-logica-programable.md)) {cite}`mandado1998`.

Cada compuerta física, además, tarda un tiempo finito y no nulo en propagar un cambio de sus
entradas a su salida: el **tiempo de propagación** ($T_{AND}$, $T_{OR}$, etc.). Este concepto,
apenas mencionado acá, se vuelve central cuando se analiza el costo y la velocidad de circuitos más
grandes, por ejemplo en el capítulo de [Multiplexores y
demultiplexores](15-multiplexores-y-demultiplexores.md), donde se calculan tiempos y costos de
bloques construidos jerárquicamente a partir de compuertas.

El marco algebraico formal que rige a todas estas compuertas (de dónde "salen" las reglas que
permiten simplificarlas y combinarlas) es el tema del [próximo capítulo](06-funciones-de-boole.md).

## 7. Resumen

- Una compuerta lógica es la implementación física de una función booleana; de las 16 funciones
  posibles de dos variables, solo NOT, AND, OR (básicas) y NAND, NOR, XOR, XNOR (derivadas) se
  fabrican como dispositivos dedicados.
- NAND y NOR son compuertas **universales:** alcanzan, cada una por sí sola, para construir
  cualquier función booleana.
- Las compuertas se agrupan en familias lógicas (TTL, CMOS) según la tecnología con la que se
  fabrican, y cada una introduce un tiempo de propagación no nulo.

## 8. Ejercicios propuestos

```{exercise}
:label: ex-compuertas-1
Construir una compuerta XOR de dos entradas utilizando únicamente compuertas NAND.
```

```{solution} ex-compuertas-1
:class: dropdown
Usando la equivalencia $x \oplus y = x \cdot y' + x' \cdot y = (x \cdot (x \cdot y)') \cdot (y \cdot
(x \cdot y)'){}'$ (derivada aplicando De Morgan dos veces), se puede construir con 4 compuertas
NAND: una primera NAND calcula $z=(x \cdot y)'$; dos NAND calculan $x \cdot z$ y $y \cdot z$
negados; y una NAND final combina esos resultados. Es el circuito clásico de "4 NAND" para XOR.
```

```{exercise}
:label: ex-compuertas-2
¿Cuántas compuertas NOR se necesitan, como mínimo, para implementar $o = x \cdot y \cdot z$ (AND de
3 entradas)?
```

```{solution} ex-compuertas-2
:class: dropdown
4: tres NOR atadas como inversores para obtener $x'$, $y'$, $z'$, y una NOR final de 3 entradas que
calcule $(x'+y'+z')' = x \cdot y \cdot z$ (De Morgan generalizado).
```

```{exercise}
:label: ex-compuertas-3
Completar la tabla de verdad de una compuerta XNOR de 3 entradas, sabiendo que la XNOR de $n$
entradas vale 1 cuando la cantidad de entradas en 1 es **par** (incluyendo cero entradas en 1).
```

```{solution} ex-compuertas-3
:class: dropdown

| $x$ | $y$ | $z$ | $o$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |
```

```{exercise}
:label: ex-compuertas-4
¿Por qué NAND y NOR son universales pero XOR, por ejemplo, no lo es?
```

```{solution} ex-compuertas-4
:class: dropdown
Porque a partir de NAND (o de NOR) sola se puede construir un inversor (atando sus entradas) y, con
De Morgan, también AND y OR — y el conjunto {NOT, AND, OR} es funcionalmente completo (permite
escribir la forma canónica de cualquier función, ver [Formas canónicas](07-formas-canonicas.md)).
XOR, en cambio, no permite construir un inversor de una sola entrada sin usar una constante auxiliar
($x \oplus 1 = x'$ requiere ya tener la constante 1 disponible como señal), por lo que {XOR} sola no
es un conjunto funcionalmente completo.
```

## 9. Bibliografía

```{bibliography}
:filter: docname in docnames
```
