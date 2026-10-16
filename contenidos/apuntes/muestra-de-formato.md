---
title: "Introducción a los Sistemas Digitales"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Introducción a los Sistemas Digitales

```{admonition} Sobre este apunte
:class: note
Este apunte reorganiza y desarrolla el material de la clase introductoria de **Diseño Lógico**
(Prof. Dr. Martín Vázquez). Cubre tres bloques temáticos que están fuertemente conectados entre sí:

1. El contexto histórico que llevó del cálculo mecánico a la computación electrónica.
2. El álgebra de Boole como herramienta matemática para describir y simplificar circuitos.
3. Los primeros componentes lógicos combinacionales construidos a partir de compuertas: multiplexores, demultiplexores y decodificadores.
```

## 1. Reseña histórica de la computación

La historia de la computación está fuertemente ligada a la necesidad humana de **contar y calcular**.
A principios del siglo XX existía una motivación muy fuerte para crear dispositivos de cálculo,
principalmente para uso **militar**: balística, cohetería, criptoanálisis, etc. Estas aplicaciones
requerían resolver ecuaciones muy complejas mediante un uso intensivo de cálculos, tarea que
originalmente realizaban equipos completos de personas.

### 1.1 Dispositivos mecánicos (basados en ruedas dentadas)

| Año | Dispositivo | Autor | Aporte |
|---|---|---|---|
| 1642 | **Pascalina** | Blaise Pascal (1623–1662) | Considerada la primera calculadora. Resolvía adiciones y sustracciones. |
| 1674 | **Máquina de Leibniz** | Gottfried Leibniz (1646–1716) | Permitía multiplicación y división; capaz de resolver ecuaciones algebraicas. |
| 1820–1822 | **Máquina diferencial** | Charles Babbage (1791–1871) | Automatizaba la creación de tablas matemáticas usadas para cálculos. |
| 1842 | **Máquina analítica** | Charles Babbage | Incorporaba tarjetas perforadas y los conceptos de *almacén* (memoria) y *molino* (unidad de cálculo). Nunca se llegó a fabricar. |

```{note}
La Máquina Analítica de Babbage (1842) se conserva conceptualmente en el Science Museum de Londres,
y anticipó ideas centrales de la arquitectura de computadoras modernas: separación entre memoria
(*almacén*) y unidad de procesamiento (*molino*), y programación mediante tarjetas perforadas.
```

### 1.2 Dispositivos electrónicos (basados en conmutadores)

Entre **1930 y 1950** transcurre la etapa pionera de la computación moderna. En este período se
consolidan conceptos clave:

- Aplicación del **álgebra de Boole** a circuitos digitales mediante conmutadores.
- Uso del **sistema binario** para las operaciones aritméticas.
- El concepto de **programa almacenado**.

Investigadores relevantes de esta etapa: **John von Neumann** (1903–1957), **Alan Turing**
(1912–1954), **John Atanasoff** (1903–1995) y **Claude Shannon** (1916–2001), entre otros.

Dispositivos representativos: **Colossus** (1943), **ABC** (1937–1942), **ENIAC** (1946), las
calculadoras **Mark I, II, III, IV** (1945) y **EDVAC** (1949).

#### Harvard–IBM Mark I (1944)

Ordenador electromecánico basado en ideas de H. Aiken y R. Stibitz.

- Dimensiones: 15,5 m × 2,4 m × 0,6 m.
- Aproximadamente **800 km** de cableado interno.
- Utilizaba relés, interruptores y una secuencia de instrucciones definida mediante **cintas
  perforadas de papel**.

#### ENIAC (Electronic Numerical Integrator and Computer, 1946)

Construida por J. Mauchly y J. Eckert.

- Poseía **17.468 válvulas de vacío**.
- Ocupaba una superficie de **167 m²**.
- Podía almacenar **20 números**.
- Alcanzaba temperaturas de hasta **50 °C**.
- Para "programarla" era necesario **reconfigurar físicamente sus circuitos**.
- Se estima que, en diez años de operación, realizó más cálculos matemáticos que los que había
  realizado toda la historia de la humanidad hasta ese momento.

#### EDVAC (Electronic Discrete Variable Automatic Computer, 1949)

- Incorpora la **arquitectura de Von Neumann** con programa almacenado.
- Alcanzaba **20.000 operaciones por segundo**, frente a las 333 operaciones por segundo de ENIAC.

### 1.3 Generaciones de computadoras (1951–actualidad)

La evolución posterior a EDVAC está directamente relacionada con la **miniaturización de los
conmutadores**: de las válvulas de vacío (superficie aproximada 3 cm², año 1904) se pasa a la
tecnología actual de escala nanométrica, con cientos de millones de transistores integrados en un
solo chip.

| Generación | Período | Características principales |
|---|---|---|
| Primera | 1951–1958 | Válvulas de vacío. Tarjetas perforadas. Tambores giratorios con marcas magnéticas como almacenamiento primario. |
| Segunda | 1959–1963 | Transistores en circuitos impresos. Redes de núcleos magnéticos para almacenamiento. Se amplían las aplicaciones (tráfico aéreo, empresas, etc.). |
| Tercera | 1964–1970 | Circuitos integrados con miles de componentes electrónicos. Multiprogramación. Aparecen las minicomputadoras. |
| Cuarta | 1971–actualidad | Microminiaturización de los circuitos electrónicos. Microprocesadores y chips de memoria. Integración **VLSI** y **GLSI**. Desarrollo de las PC. |

### 1.4 La actualidad: integración a gran escala

- **VLSI** (*Very Large Scale Integration*), **ULSI** (*Ultra Large Scale Integration*) y **GLSI**
  (*Giga Large Scale Integration*) describen niveles crecientes de densidad de integración.
- Los circuitos **GLSI** actuales contienen **cientos de millones de transistores** en un único chip.

## 2. Conmutadores

Un **conmutador** (*switch*) es un dispositivo que se utiliza para interrumpir o permitir la
conexión de un circuito eléctrico o electrónico. Se maneja eléctricamente y es la pieza fundamental
sobre la que se construyen las computadoras digitales.

Evolución tecnológica de los conmutadores utilizados en el diseño de computadoras:

1. **Relés electromagnéticos** — primeros conmutadores usados en calculadoras electromecánicas (p. ej. Mark I).
2. **Válvulas de vacío** (1904) — funcionan como un diodo controlado; permitieron la primera generación de computadoras electrónicas (ENIAC).
3. **Transistores** (1947) — conmutadores de estado sólido, base de toda la electrónica digital moderna, desde la segunda generación en adelante.

## 3. De los conmutadores al álgebra de Boole: el aporte de Shannon

En **1938**, Claude Shannon publica su tesis de maestría *"Análisis simbólico de los relés y los
circuitos conmutadores"* (*A Symbolic Analysis of Relay and Switching Circuits*), considerada uno de
los trabajos fundacionales del diseño digital moderno.

```{admonition} Claude Shannon (1916–2001)
:class: tip
Matemático e Ingeniero Eléctrico, fundador de la **Teoría de la Información**. Su tesis de maestría
demostró que las operaciones booleanas **NOT**, **AND** y **OR** podían representarse mediante
circuitos de conmutadores electrónicos, uniendo por primera vez el álgebra de Boole (una teoría
puramente matemática de 1854) con el diseño físico de circuitos.
```

Shannon modela un circuito entre dos terminales ($a$ y $b$) con solo dos estados posibles:

- **Abierto**: impedancia infinita (no circula corriente).
- **Cerrado**: impedancia cero (circula corriente sin restricción).

A este circuito se lo denota con el símbolo $X_{ab}$ (o, simplificado, simplemente $X$), y se le
asocia un valor lógico:

- $X = 0$ &nbsp;→&nbsp; el circuito está **cerrado**.
- $X = 1$ &nbsp;→&nbsp; el circuito está **abierto**.

A partir de esta convención, Shannon analiza las dos formas básicas de combinar dos conmutadores
$X$ e $Y$:

- **Conmutadores en serie**: el circuito combinado está **abierto** (vale 1) cuando **$X$ o $Y$**
  están abiertos. Esto corresponde exactamente a la operación booleana **OR**: $X + Y$.
- **Conmutadores en paralelo**: el circuito combinado está **abierto** (vale 1) únicamente cuando
  **$X$ e $Y$** están abiertos simultáneamente. Esto corresponde a la operación booleana **AND**:
  $X \cdot Y$.

De esta forma, la topología física de un circuito de conmutadores (serie/paralelo) queda traducida
directamente a una expresión del álgebra de Boole, lo que permite **diseñar y simplificar circuitos
mediante manipulación algebraica** en lugar de prueba y error.

## 4. Álgebra de la lógica y álgebra de Boole

### 4.1 George Boole y el nacimiento del álgebra de la lógica

En **1847**, George Boole (1815–1864), matemático y lógico autodidacta británico, publica *"Análisis
matemático de la lógica, ensayo de un cálculo de razonamiento deductivo"*. Sus ideas centrales son:

- La **lógica** puede tratarse como una rama de las matemáticas.
- Los razonamientos lógicos están sujetos a leyes matemáticas y pueden representarse y analizarse
  como **ecuaciones matemáticas**.
- Esta álgebra no opera sobre números en el sentido usual, sino sobre **clases de objetos**, y
  cumple la propiedad particular $x^2 = x$ (idempotencia).

Más adelante surge la **lógica booleana de los silogismos**, que representa cada silogismo y su
conclusión mediante una ecuación matemática.

### 4.2 El álgebra de Boole como estructura algebraica

En **1860**, en trabajos posteriores de **Charles S. Peirce** (1839–1914) y **William Stanley
Jevons** (1835–1882), aparece el concepto más general de **"álgebra de Boole"** como estructura
algebraica abstracta.

Formalmente, un álgebra de Boole es:

- Un conjunto $B$ con (al menos) dos elementos distinguibles: $0$ y $1$.
- Dados dos elementos $x, y \in B$, se definen dos operaciones binarias: $x + y$ (suma / OR) y
  $x \cdot y$ (producto / AND).
- Se define además una operación unaria de **negación** (complemento): $x'$, $y'$.

El **álgebra de conjuntos** y el **cálculo proposicional** son ejemplos clásicos de álgebras de
Boole: ambos satisfacen los axiomas y teoremas que caracterizan esta estructura.

### 4.3 Axiomas

| Propiedad | Forma con "+" (OR) | Forma con "·" (AND) |
|---|---|---|
| Conmutatividad | $x+y = y+x$ | $x \cdot y = y \cdot x$ |
| Asociatividad | $x+(y+z) = (x+y)+z$ | $x \cdot (y \cdot z) = (x \cdot y) \cdot z$ |
| Distributividad | $x+(y \cdot z) = (x+y)\cdot(x+z)$ | $x \cdot (y+z) = (x \cdot y)+(x \cdot z)$ |
| Elemento neutro | $x+0 = x$ | $x \cdot 1 = x$ |
| Complementario | $x + x' = 1$ | $x \cdot x' = 0$ |

```{important}
A diferencia del álgebra de números reales, en el álgebra de Boole **la suma también distribuye
sobre el producto** ($x+(y\cdot z) = (x+y)\cdot(x+z)$), no solo el producto sobre la suma. Esta
simetría entre $+$ y $\cdot$ es la base del **principio de dualidad**: toda identidad booleana
sigue siendo válida si se intercambian simultáneamente $+ \leftrightarrow \cdot$ y $0
\leftrightarrow 1$.
```

### 4.4 Teoremas derivados

| Teorema | Forma con "+" (OR) | Forma con "·" (AND) |
|---|---|---|
| Idempotencia | $x+x = x$ | $x \cdot x = x$ |
| Absorción | $x+1 = 1$ | $x \cdot 0 = 0$ |
| Complementario | $1' = 0$ | $0' = 1$ |
| Involución | $(x')' = x$ | $(x')' = x$ |
| **De Morgan** | $(x+y)' = x' \cdot y'$ | $(x \cdot y)' = x' + y'$ |

Las **leyes de De Morgan** son especialmente importantes en el diseño digital porque permiten
convertir entre expresiones basadas en AND/OR y expresiones basadas en NAND/NOR, algo fundamental
al sintetizar circuitos con una única familia de compuertas.

## 5. Funciones booleanas básicas y compuertas lógicas

Para el diseño de circuitos digitales se requieren **compuertas lógicas** (*logic gates*), que son
la implementación física de las funciones booleanas.

- **Funciones booleanas básicas**: negación (**NOT**), conjunción (**AND**) y disyunción (**OR**).
- **Otras funciones derivadas**: negación de la disyunción (**NOR**), negación de la conjunción
  (**NAND**) y disyunción exclusiva (**XOR**).

### 5.1 Compuerta NOT

$$o = x'$$

| $x$ | $o$ |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

### 5.2 Compuerta AND

$$o = x \cdot y$$

| $x$ | $y$ | $o$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### 5.3 Compuerta OR

$$o = x + y$$

| $x$ | $y$ | $o$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### 5.4 Compuerta XOR

$$o = x \oplus y$$

| $x$ | $y$ | $o$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

La salida vale 1 únicamente cuando las entradas son **distintas** entre sí.

### 5.5 Compuerta NAND

$$o = (x \cdot y)'$$

| $x$ | $y$ | $o$ |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

### 5.6 Compuerta NOR

$$o = (x + y)'$$

| $x$ | $y$ | $o$ |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

```{note}
NAND y NOR se llaman **compuertas universales**: cualquier función booleana puede implementarse
usando exclusivamente compuertas NAND, o exclusivamente compuertas NOR. Esta propiedad, junto con
las leyes de De Morgan, es una de las razones por las que son tan utilizadas en la fabricación real
de circuitos integrados.
```

## 6. Funciones lógicas y tablas de verdad

Existe una equivalencia total entre tres formas de describir una función lógica:

$$\text{Tabla de verdad} \;\Longleftrightarrow\; \text{Ecuación booleana} \;\Longleftrightarrow\; \text{Circuito de compuertas}$$

- Cualquier función lógica puede describirse mediante una **tabla de verdad**.
- Cualquier tabla de verdad puede describirse mediante una **ecuación booleana**.
- Cualquier ecuación booleana puede implementarse como un **circuito de compuertas lógicas**.

### 6.1 Ejemplo de trabajo: función de tres variables

Sea la función booleana de tres variables $o = f(x, y, z)$ definida por la siguiente tabla de
verdad (orden estándar de $x,y,z$ de $000$ a $111$):

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

Esta misma tabla se usa a continuación para obtener las dos formas canónicas de $f(x,y,z)$.

### 6.2 Forma canónica disyuntiva (suma de minterms / SOP)

**Estrategia:** se consideran todas las filas en las que la función **vale 1**. Para cada una de
esas filas se construye un producto (**minterm**) que toma cada variable sin complementar si vale 1,
y complementada si vale 0. La función es la **suma (OR)** de todos esos minterms.

Filas donde $o=1$: $(x,y,z) = (0,0,0),\ (0,1,1),\ (1,0,1),\ (1,1,0)$.

$$o = \underbrace{x' \cdot y' \cdot z'}_{\text{minterm}} + x' \cdot y \cdot z + x \cdot y' \cdot z + x \cdot y \cdot z'$$

Esta expresión —suma de minterms— se llama **expresión (o forma) disyuntiva canónica**.

#### Implementación mediante compuertas lógicas

Cada minterm se implementa con una compuerta **AND de 3 entradas** (usando las entradas
complementadas donde corresponda mediante compuertas NOT), y los cuatro minterms se combinan con
una compuerta **OR de 4 entradas**:

```text
x,y,z ─┬─[NOT]──┐
       │        │
x' y' z' ──[AND3]──┐
x' y  z  ──[AND3]──┤
x  y' z  ──[AND3]──┼─[OR4]── o
x  y  z' ──[AND3]──┘
```

Esta estructura de dos niveles — **AND (nivel 1) seguido de OR (nivel 2)** — es la forma canónica de
implementación conocida como **suma de productos** (*Sum of Products*, SOP), y es directamente
sintetizable a partir de cualquier tabla de verdad sin necesidad de simplificación previa.

### 6.3 Forma canónica conjuntiva (producto de maxterms / POS)

**Estrategia alternativa:** se consideran todas las filas en las que la función **no se cumple**
(vale 0), y se trabaja sobre el complemento $o' = f(x,y,z)'$.

Filas donde $o=0$: $(x,y,z) = (0,0,1),\ (0,1,0),\ (1,0,0),\ (1,1,1)$.

$$o' = x' \cdot y' \cdot z + x' \cdot y \cdot z' + x \cdot y' \cdot z' + x \cdot y \cdot z$$

Esta es la **expresión disyuntiva** de $o'$ (suma de los minterms de $o'$). Para obtener $o$, se
niega toda la expresión y se aplican las leyes de De Morgan paso a paso:

$$o = \left(x' y' z + x' y z' + x y' z' + x y z\right)'$$

Aplicando De Morgan a la negación de una suma —se convierte en producto de negaciones—:

$$o = (x' y' z)' \cdot (x' y z')' \cdot (x y' z')' \cdot (x y z)'$$

Aplicando De Morgan nuevamente a cada término —la negación de un producto se convierte en suma de
negaciones—:

$$o = (x + y + z') \cdot (x + y' + z) \cdot (x' + y + z) \cdot (x' + y' + z')$$

Cada uno de estos factores es un **maxterm**, y el resultado —producto de maxterms— es la
**expresión (o forma) conjuntiva canónica**:

$$o = \underbrace{(x+y+z')}_{\text{maxterm}} \cdot (x+y'+z) \cdot (x'+y+z) \cdot (x'+y'+z')$$

```{admonition} Relación minterm ↔ maxterm
:class: tip
Cada maxterm es el **complemento del minterm correspondiente a la misma combinación de variables**
(vía De Morgan): la fila $(x,y,z)=(0,0,1)$, cuyo minterm sería $x'y'z$, da origen al maxterm
$(x+y+z')$. La forma conjuntiva se construye con las filas donde $o=0$, exactamente al revés que la
forma disyuntiva.
```

Esta estructura de dos niveles —**OR (nivel 1) seguido de AND (nivel 2)**— se conoce como
**producto de sumas** (*Product of Sums*, POS), y es la implementación dual de la forma SOP vista
en la sección anterior.

## 7. Componentes lógicos combinacionales

A partir de las compuertas básicas se construyen bloques combinacionales de uso frecuente:
**multiplexores**, **demultiplexores** y **decodificadores**. Estos bloques son, a su vez, los
ladrillos con los que luego se arman circuitos más complejos (unidades aritméticas, memorias,
unidades de control, etc.).

### 7.1 Multiplexor (MUX)

Un **multiplexor** es un selector: a partir de $n$ señales de entrada y una señal de **selección**
$s$, entrega en la salida el valor de **una sola** de las entradas, la indicada por $s$.

#### Multiplexor de 2 entradas de 1 bit (MUX2\_1)

```text
        ┌─────────┐
   x ──►│         │
   y ──►│ MUX2_1  ├──► o
   s ──►│         │
        └─────────┘
```

$$o = \begin{cases} x & s = 0 \\ y & s = 1 \end{cases} \qquad\Longrightarrow\qquad o = x \cdot s' + y \cdot s$$

Es decir: cuando $s=0$ el término $x \cdot s'$ queda activo y $y \cdot s$ se anula, por lo que
$o=x$; cuando $s=1$ ocurre lo simétrico y $o=y$. Se implementa con dos compuertas AND, una OR y un
inversor para generar $s'$.

#### Multiplexor de 4 entradas de 1 bit (MUX4\_1)

Tiene 4 entradas de datos ($x_1,x_2,x_3,x_4$) y **2 bits de selección** ($s = s_1 s_0$), ya que se
necesitan $\log_2 4 = 2$ bits para distinguir 4 entradas.

**Implementación jerárquica usando MUX2\_1:** se arman tres MUX2\_1 en forma de árbol — dos en el
primer nivel (seleccionan entre $x_1,x_2$ y entre $x_3,x_4$ usando $s_0$) y uno en el segundo nivel
(selecciona entre los dos resultados anteriores usando $s_1$):

```text
x1 ─┐
    ├─[MUX2_1]s0─┐
x2 ─┘             │
                  ├─[MUX2_1]s1── o
x3 ─┐             │
    ├─[MUX2_1]s0─┘
x4 ─┘
```

Costo y tiempo de propagación, en función del costo/tiempo de un MUX2\_1:

$$T_{MUX4\_1} = 2 \cdot T_{MUX2\_1} = 2 \cdot (T_{AND}+T_{OR})$$

$$C_{MUX4\_1} = 3 \cdot C_{MUX2\_1} = 3 \cdot C_{OR} + 6 \cdot C_{AND}$$

(3 bloques MUX2\_1 en total: 2 en el primer nivel + 1 en el segundo).

#### Multiplexor de 8 entradas de 1 bit (MUX8\_1)

Con 8 entradas se necesitan **3 bits de selección** ($s = s_2 s_1 s_0$). Extendiendo el árbol
anterior un nivel más (4 + 2 + 1 = 7 bloques MUX2\_1 en total):

$$T_{MUX8\_1} = 3 \cdot T_{MUX2\_1} = 3 \cdot (T_{AND}+T_{OR})$$

$$C_{MUX8\_1} = 7 \cdot C_{MUX2\_1} = 7 \cdot C_{OR} + 14 \cdot C_{AND}$$

#### Caso general: $MUX_{m\_1}$ con $m = 2^i$

Generalizando el patrón anterior, un multiplexor de $m=2^i$ entradas de 1 bit construido en árbol a
partir de bloques MUX2\_1 requiere $i$ niveles de propagación y $m-1$ bloques MUX2\_1 en total:

$$T_{MUX_{m\_1}} = i \cdot T_{MUX2\_1} = i \cdot (T_{AND}+T_{OR})$$

$$C_{MUX_{m\_1}} = (2^i - 1) \cdot C_{MUX2\_1} = (2^i - 1) \cdot C_{OR} + (2^{i+1} - 2) \cdot C_{AND}$$

Es decir: el **tiempo de propagación crece logarítmicamente** con la cantidad de entradas
($i = \log_2 m$), mientras que el **costo (área) crece linealmente** con $m$.

#### Multiplexor de $n$ bits (buses): MUX2\_8

Cuando cada entrada no es un único bit sino un **bus de $n$ bits** (por ejemplo $n=8$), se replica
un MUX2\_1 por cada bit del bus, todos comandados por la **misma** señal de selección $s$:

```text
 s ──┬───────────┬───────────┬──── ... ──┬───────────┐
     │           │           │           │           │
x0,y0│      x1,y1│           │      x7,y7│           │
 ►[MUX2_1]► o0  ►[MUX2_1]► o1   ...   ►[MUX2_1]► o7
```

Como los 8 bloques operan **en paralelo** (no en cascada), el tiempo de propagación **no aumenta**
respecto de un único MUX2\_1, pero el costo sí se multiplica por 8:

$$T_{MUX2\_8} = T_{MUX2\_1} = T_{AND}+T_{OR}$$

$$C_{MUX2\_8} = 8 \cdot C_{MUX2\_1} = 8 \cdot C_{OR} + 16 \cdot C_{AND}$$

### 7.2 Demultiplexor (DEMUX)

Un **demultiplexor** realiza la operación inversa a la del multiplexor: toma **una** entrada de
datos $x$ y la enruta hacia **una** de varias salidas posibles, según indique la señal de selección
$s$; el resto de las salidas queda en 0.

#### Demultiplexor de 1 entrada y 2 salidas (DMUX2\_1)

```text
        ┌──────────┐
   x ──►│          ├──► o1
   s ──►│ DMUX2_1  ├──► o2
        └──────────┘
```

$$o_1 = \begin{cases} x & s=0 \\ 0 & s=1 \end{cases} \qquad o_2 = \begin{cases} x & s=1 \\ 0 & s=0 \end{cases}$$

$$o_1 = x \cdot s' \qquad\qquad o_2 = x \cdot s$$

#### Demultiplexor de 1 entrada y 4 salidas (DMUX4\_1)

Requiere **2 bits de selección** ($s = s_1 s_0$) y se puede construir jerárquicamente a partir de
tres bloques DMUX2\_1, de manera dual al MUX4\_1: un primer DMUX2\_1 (controlado por $s_1$) separa
la entrada hacia dos ramas, y en cada rama un segundo DMUX2\_1 (controlado por $s_0$) termina de
distribuir la señal entre las 4 salidas finales $o_1, o_2, o_3, o_4$.

### 7.3 Decodificador (DECODER)

Un **decodificador** de $n$ entradas tiene $2^n$ salidas, y activa (pone en 1) **exactamente una**
de ellas según el valor binario presente en la entrada; todas las demás salidas quedan en 0. Es,
conceptualmente, un demultiplexor cuya entrada de datos $x$ está fijada permanentemente en 1: lo
único que "viaja" es la selección.

#### Decodificador de 3 a 8 (DECODE3)

```text
        ┌───────────┐
 x2..0 ─►│  DECODE3  ├─► o7..0
  (3)   │           │  (8)
        └───────────┘
```

| $x_2 x_1 x_0$ | $o_7 o_6 o_5 o_4 o_3 o_2 o_1 o_0$ |
|:---:|:---:|
| 000 | 00000001 |
| 001 | 00000010 |
| 010 | 00000100 |
| 011 | 00001000 |
| 100 | 00010000 |
| 101 | 00100000 |
| 110 | 01000000 |
| 111 | 10000000 |

Nótese que la salida es siempre una codificación **"one-hot"**: un único bit en 1, en la posición
indicada por el valor binario de la entrada.

#### Relación entre decodificador y demultiplexor

El decodificador se puede implementar directamente con un demultiplexor: basta con conectar la
entrada de datos $x$ del demultiplexor a una constante lógica **1**. Por ejemplo, un `DECODE2` (2
entradas → 4 salidas) se arma con un `DEMUX4_1` cuya entrada de datos está atada a 1 y cuyas
entradas de selección son las 2 entradas del decodificador.

## 8. Resumen

- La computación digital moderna nace de la confluencia de dos líneas históricas: la búsqueda de
  dispositivos mecánicos/electrónicos cada vez más rápidos para calcular (Pascal → Babbage → Mark I
  → ENIAC → EDVAC), y el desarrollo matemático del **álgebra de Boole** (Boole → Peirce/Jevons →
  Shannon), que permitió describir formalmente el comportamiento de circuitos de conmutadores.
- El **álgebra de Boole** es una estructura algebraica sobre un conjunto $\{0,1\}$ con operaciones
  $+$, $\cdot$ y $'$, gobernada por axiomas (conmutatividad, asociatividad, distributividad,
  elemento neutro, complementario) de los que se derivan teoremas útiles para simplificar circuitos
  (idempotencia, absorción, De Morgan, involución).
- Toda función lógica admite una **tabla de verdad**, y toda tabla de verdad admite dos formas
  canónicas equivalentes:
  - **Disyuntiva (SOP)**: suma de minterms (filas donde $o=1$), implementada como AND→OR.
  - **Conjuntiva (POS)**: producto de maxterms (filas donde $o=0$), implementada como OR→AND,
    obtenida aplicando De Morgan sobre la forma disyuntiva del complemento.
- Los **multiplexores**, **demultiplexores** y **decodificadores** son los primeros bloques
  combinacionales construidos a partir de compuertas. Su versión de $m=2^i$ vías se arma en forma de
  **árbol binario** a partir de bloques de 2 vías, logrando tiempo de propagación logarítmico
  ($O(\log m)$) y costo lineal ($O(m)$) en la cantidad de entradas/salidas.

## 9. Ejercicios propuestos

Estos ejercicios estaban planteados en la clase original como práctica de construcción jerárquica de
componentes; se recomienda resolverlos dibujando el circuito y verificando la fórmula de costo/tiempo
resultante.

1. Implementar un **multiplexor de 8 entradas de 1 bit (MUX8\_1)** utilizando exclusivamente
   bloques **MUX2\_1**. Verificar que resulten 7 bloques en total y 3 niveles de propagación.
2. Implementar un **multiplexor de 8 entradas de 8 bits (MUX8\_8)** utilizando bloques **MUX2\_8**.
3. Determinar el **tiempo de cálculo y el costo (área)** de un MUX8\_8 implementado directamente con
   bloques **MUX2\_1** (es decir, sin pasar por MUX2\_8 como bloque intermedio).
4. Hallar la **expresión genérica** de tiempo y área de un $MUX_{m\_n}$ (multiplexor de $m$ entradas
   de $n$ bits cada una) utilizando bloques MUX2\_1, con $m = 2^i$.
5. Implementar un **DMUX4\_1** utilizando bloques **DMUX2\_1**.
6. Implementar un **DMUX8\_1** utilizando bloques **DMUX2\_1**.
7. Implementar un **DMUX2\_8** (demultiplexor de un bus de 8 bits, 2 salidas) utilizando bloques
   **DMUX2\_1**.
8. Implementar un **DMUX8\_8** utilizando bloques **DMUX2\_8**.

```{admonition} Sugerencia para resolver los ejercicios de generalización
:class: tip
Para cualquier bloque de $m=2^i$ vías construido en árbol a partir de un bloque base de 2 vías, el
número de bloques base necesarios es siempre $m-1$, y la profundidad del árbol (y por lo tanto el
tiempo de propagación en múltiplos del bloque base) es $i = \log_2 m$. Esta misma relación aplica
tanto a multiplexores como a demultiplexores, por dualidad.
```
