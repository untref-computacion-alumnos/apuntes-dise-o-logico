---
title: "Introducción a los sistemas digitales"
subject: "Diseño Lógico"
---

# Introducción a los sistemas digitales

```{admonition} Sobre este apunte
:class: note
Este apunte cubre el contexto histórico que llevó del cálculo mecánico a la computación electrónica,
y cierra con la idea de Shannon que conecta los circuitos de conmutadores con el álgebra de Boole.
El desarrollo formal del álgebra de Boole se retoma en [Funciones de
Boole](06-funciones-de-boole.md), y el concepto de función lógica en [Funciones
lógicas](04-funciones-logicas.md).
```

## 1. Motivación histórica: la necesidad de contar y calcular

La historia de la computación está fuertemente ligada a la necesidad humana de **contar y
calcular**. A principios del siglo XX existía una motivación muy fuerte para crear dispositivos de
cálculo, principalmente para uso **militar:** balística, cohetería, criptoanálisis, etc. Estas
aplicaciones requerían resolver ecuaciones muy complejas mediante un uso intensivo de cálculos,
tarea que originalmente realizaban equipos completos de personas dedicadas exclusivamente a
calcular a mano.

Esta demanda de cálculo intensivo es el hilo conductor que explica, en pocas décadas, el salto
desde las primeras calculadoras mecánicas de engranajes hasta los circuitos integrados actuales.

### 1.1. Dispositivos mecánicos (basados en ruedas dentadas)

| Año       | Dispositivo             | Autor                         | Aporte                                                                                                                            |
| --------- | ----------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1642      | **Pascalina**           | Blaise Pascal (1623–1662)     | Considerada la primera calculadora. Resolvía adiciones y sustracciones.                                                           |
| 1674      | **Máquina de Leibniz**  | Gottfried Leibniz (1646–1716) | Permitía multiplicación y división; capaz de resolver ecuaciones algebraicas.                                                     |
| 1820–1822 | **Máquina diferencial** | Charles Babbage (1791–1871)   | Automatizaba la creación de tablas matemáticas usadas para cálculos.                                                              |
| 1842      | **Máquina analítica**   | Charles Babbage               | Incorporaba tarjetas perforadas y los conceptos de _almacén_ (memoria) y _molino_ (unidad de cálculo). Nunca se llegó a fabricar. |

```{note} Nota
La Máquina Analítica de Babbage (1842) se conserva conceptualmente en el Science Museum de Londres,
y anticipó ideas centrales de la arquitectura de computadoras modernas: separación entre memoria
(*almacén*), unidad de procesamiento (*molino*), y programación mediante tarjetas perforadas. Esta
separación entre almacenamiento y procesamiento es, en esencia, la misma que se distingue entre los
capítulos de [Memoria](21-memoria.md) y los de circuitos combinacionales/secuenciales de este
apunte.
```

Todos estos dispositivos comparten una limitación estructural: son **mecánicos**. Su velocidad está
acotada por la inercia de ruedas dentadas y engranajes, y su "programación" (cuando existe, como en
la máquina analítica) depende de medios físicos como tarjetas perforadas. El siguiente salto
tecnológico requiere abandonar la mecánica pura y pasar a dispositivos **electrónicos**.

## 2. Dispositivos electrónicos (basados en conmutadores)

Entre **1930 y 1950** transcurre la etapa pionera de la computación moderna. En este período se
consolidan conceptos clave:

- Aplicación del **álgebra de Boole** a circuitos digitales mediante conmutadores.
- Uso del **sistema binario** para las operaciones aritméticas.
- El concepto de **programa almacenado**.

Investigadores relevantes de esta etapa: **John von Neumann** (1903–1957), **Alan Turing**
(1912–1954), **John Atanasoff** (1903–1995) y **Claude Shannon** (1916–2001), entre otros.

Dispositivos representativos de la época: **Colossus** (1943), **ABC** (1937–1942), **ENIAC**
(1946), las calculadoras **Mark I, II, III, IV** (1945) y **EDVAC** (1949).

### 2.1. Harvard–IBM Mark I (1944)

Ordenador electromecánico basado en ideas de H. Aiken y R. Stibitz.

- Dimensiones: $15.5 \text{ m} \times 2.4 \text{ m} \times 0.6 \text{ m}$.
- Aproximadamente **800 km** de cableado interno.
- Utilizaba relés, interruptores y una secuencia de instrucciones definida mediante **cintas
  perforadas de papel**.

### 2.2. ENIAC (Electronic Numerical Integrator and Computer, 1946)

Construida por J. Mauchly y J. Eckert.

- Poseía **17.468 válvulas de vacío**.
- Ocupaba una superficie de **$167 \text{ m}^{2}$**.
- Podía almacenar **20 números**.
- Alcanzaba temperaturas de hasta **50 °C**.
- Para "programarla" era necesario **reconfigurar físicamente sus circuitos**.
- Se estima que, en diez años de operación, realizó más cálculos matemáticos que los que había
  realizado toda la historia de la humanidad hasta ese momento.

### 2.3. EDVAC (Electronic Discrete Variable Automatic Computer, 1949)

- Incorpora la **arquitectura de Von Neumann** con programa almacenado: a diferencia de ENIAC, ya
  no hace falta recablear el circuito para cambiar de programa.
- Alcanzaba **20.000 operaciones por segundo**, frente a las 333 operaciones por segundo de ENIAC.

```{important} Importante
El salto de ENIAC a EDVAC no es solo de velocidad (60 veces más rápida). Es sobre todo un salto
**conceptual:** la idea de programa almacenado en la misma memoria que los datos (arquitectura de
Von Neumann) es la que hace posible reprogramar una máquina sin modificar su hardware, y sigue
siendo la base de las computadoras actuales.
```

### 2.4. Generaciones de computadoras (1951 – actualidad)

La evolución posterior a EDVAC está directamente relacionada con la **miniaturización de los
conmutadores:** de las válvulas de vacío (superficie aproximada $3 \text{ cm}^{2}$, año 1904) se
pasa a la tecnología actual de escala nanométrica, con cientos de millones de transistores
integrados en un solo chip.

| Generación | Período         | Características principales                                                                                                                       |
| ---------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primera    | 1951–1958       | Válvulas de vacío. Tarjetas perforadas. Tambores giratorios con marcas magnéticas como almacenamiento primario.                                   |
| Segunda    | 1959–1963       | Transistores en circuitos impresos. Redes de núcleos magnéticos para almacenamiento. Se amplían las aplicaciones (tráfico aéreo, empresas, etc.). |
| Tercera    | 1964–1970       | Circuitos integrados con miles de componentes electrónicos. Multiprogramación. Aparecen las minicomputadoras.                                     |
| Cuarta     | 1971–actualidad | Microminiaturización de los circuitos electrónicos. Microprocesadores y chips de memoria. Integración **VLSI** y **GLSI**. Desarrollo de las PC.  |

### 2.5. La actualidad: integración a gran escala

- **VLSI** (_Very Large Scale Integration_), **ULSI** (_Ultra Large Scale Integration_) y **GLSI**
  (_Giga Large Scale Integration_) describen niveles crecientes de densidad de integración.
- Los circuitos **GLSI** actuales contienen **cientos de millones de transistores** en un único
  chip.

Este eje de miniaturización creciente es el mismo que retoma el capítulo de
[Lógica programable](23-logica-programable.md) al comparar dispositivos discretos, ASIC y FPGA.

## 3. Conmutadores

Un **conmutador** (_switch_) es un dispositivo que se utiliza para interrumpir o permitir la
conexión de un circuito eléctrico o electrónico. Se maneja eléctricamente y es la pieza fundamental
sobre la que se construyen las computadoras digitales.

Evolución tecnológica de los conmutadores utilizados en el diseño de computadoras:

1. **Relés electromagnéticos:** Primeros conmutadores usados en calculadoras electromecánicas (por
   ejemplo, Mark I).
2. **Válvulas de vacío (1904):** Funcionan como un diodo controlado; permitieron la primera
   generación de computadoras electrónicas (ENIAC).
3. **Transistores (1947):** Conmutadores de estado sólido, base de toda la electrónica digital
   moderna, desde la segunda generación en adelante.

```{tip} Misma lógica, distinta tecnología
Toda la evolución de la computación digital puede leerse, en el fondo, como la búsqueda de un
conmutador cada vez más pequeño, rápido y barato: relé $\rightarrow$ válvula de vacío $\rightarrow$
transistor $\rightarrow$ transistor integrado (VLSI/GLSI). El comportamiento *lógico* que implementa
el conmutador (abierto o cerrado) no cambió; lo que cambió es la tecnología física que lo realiza.
```

## 4. De los conmutadores al álgebra de Boole: el aporte de Shannon

En **1938**, Claude Shannon publica su tesis de maestría _"Análisis simbólico de los relés y los
circuitos conmutadores"_ (_A Symbolic Analysis of Relay and Switching Circuits_), considerada uno
de los trabajos fundacionales del diseño digital moderno.

```{admonition} Claude Shannon (1916–2001)
:class: tip
Matemático e Ingeniero Eléctrico, fundador de la **Teoría de la Información**. Su tesis de maestría
demostró que las operaciones booleanas **NOT**, **AND** y **OR** podían representarse mediante
circuitos de conmutadores electrónicos, uniendo por primera vez el álgebra de Boole (una teoría
puramente matemática de 1854) con el diseño físico de circuitos.
```

Shannon modela un circuito entre dos terminales ($a$ y $b$) con solo dos estados posibles:

- **Abierto:** Impedancia infinita (no circula corriente).
- **Cerrado:** Impedancia cero (circula corriente sin restricción).

A este circuito se lo denota con el símbolo $X_{ab}$ (o, simplificado, simplemente $X$), y se le
asocia un valor lógico:

- $X = 0$ $\rightarrow$ el circuito está **cerrado**.
- $X = 1$ $\rightarrow$ el circuito está **abierto**.

A partir de esta convención, Shannon analiza las dos formas básicas de combinar dos conmutadores
$X$ e $Y$:

- **Conmutadores en serie:** El circuito combinado está **abierto** (vale 1) cuando **$X$ o $Y$**
  están abiertos. Esto corresponde exactamente a la operación booleana **OR:** $X + Y$.

```{image} ../../imagenes/serie-or.png
:alt: Serie (OR)
:width: 50%
:align: center
```

- **Conmutadores en paralelo:** El circuito combinado está **abierto** (vale 1) únicamente cuando
  **$X$ e $Y$** están abiertos simultáneamente. Esto corresponde a la operación booleana **AND:**
  $X \cdot Y$.

```{image} ../../imagenes/paralelo-and.png
:alt: Paralelo (AND)
:width: 50%
:align: center
```

De esta forma, la topología física de un circuito de conmutadores (serie/paralelo) queda traducida
directamente a una expresión del álgebra de Boole, lo que permite **diseñar y simplificar circuitos
mediante manipulación algebraica** en lugar de prueba y error.

```{important} Importante
La idea de Shannon es el puente entre este capítulo y el resto del apunte: a partir de acá, "diseñar
un circuito digital" y "escribir/simplificar una expresión booleana" son, en esencia, la misma
actividad. El capítulo [Funciones lógicas](04-funciones-logicas.md) retoma esta idea para definir
formalmente qué es una función lógica y cómo se describe con una tabla de verdad, mientras que
[Funciones de Boole](06-funciones-de-boole.md) desarrolla el álgebra de Boole como estructura
matemática (axiomas y teoremas) que sustenta esa manipulación algebraica.
```

## 5. Resumen

- La computación digital moderna nace de la confluencia de dos líneas históricas: la búsqueda de
  dispositivos mecánicos/electrónicos cada vez más rápidos para calcular (Pascal $\rightarrow$
  Babbage $\rightarrow$ Mark I $\rightarrow$ ENIAC $\rightarrow$ EDVAC), y el desarrollo matemático
  del álgebra de Boole, que Shannon conecta por primera vez con los circuitos físicos en 1938.
- Las cuatro generaciones de computadoras (1951 – hoy) están gobernadas por la miniaturización
  creciente del conmutador: válvulas de vacío $\rightarrow$ transistores discretos $\rightarrow$
  circuitos integrados $\rightarrow$ VLSI/GLSI.
- Un **conmutador** es un dispositivo de dos estados (abierto/cerrado) que se usa para interrumpir o
  permitir el paso de corriente. Su evolución tecnológica es relés $\rightarrow$ válvulas de vacío
  $\rightarrow$ transistores.
- Shannon demostró que un circuito de conmutadores en **serie** implementa la operación **OR**, y un
  circuito en **paralelo** implementa la operación **AND**, sentando las bases del diseño lógico
  moderno.

## 6. Ejercicios propuestos

```{exercise}
:label: ex-intro-1
Ordená cronológicamente los siguientes hitos y para cada uno indicá si se trata de un dispositivo
mecánico o electrónico: Pascalina, ENIAC, máquina analítica de Babbage, EDVAC, Mark I.
```

```{solution} ex-intro-1
:class: dropdown
1642 Pascalina (mecánico) → 1842 Máquina analítica de Babbage (mecánico, nunca construida) → 1944
Mark I (electromecánico) → 1946 ENIAC (electrónico) → 1949 EDVAC (electrónico).
```

```{exercise}
:label: ex-intro-2
¿Por qué se dice que EDVAC representa un salto *conceptual* y no solo de velocidad respecto de
ENIAC?
```

```{solution} ex-intro-2
:class: dropdown
Porque incorpora la arquitectura de Von Neumann con programa almacenado: el programa se guarda en
la misma memoria que los datos y puede cambiarse sin recablear físicamente el circuito, a diferencia
de ENIAC, donde "programar" implicaba reconfigurar conexiones físicas.
```

```{exercise}
:label: ex-intro-3
Dibujá (con ASCII art o en papel) un circuito de tres conmutadores $X$, $Y$, $Z$ tal que esté
abierto únicamente cuando **las tres** están abiertas simultáneamente. ¿Qué operación booleana
representa?
```

````{solution} ex-intro-3
:class: dropdown
Un circuito con los tres conmutadores en **paralelo** (los tres deben estar abiertos a la vez para
que el conjunto lo esté) representa la operación $X \cdot Y \cdot Z$ (AND de tres variables).

```text
──┬─[X]─┬──
  ├─[Y]─┤
  └─[Z]─┘
```
````

```{exercise}
:label: ex-intro-4
Un circuito combina dos conmutadores $X$ e $Y$ en serie, y ese conjunto en paralelo con un tercer
conmutador $Z$. Escribí la expresión booleana correspondiente.
```

```{solution} ex-intro-4
:class: dropdown
El bloque en serie $X$–$Y$ implementa $X \cdot Y$. Ese bloque en paralelo con $Z$ implementa
$(X \cdot Y) + Z$.
```

```{exercise}
:label: ex-intro-5
Investigá qué otro dispositivo electrónico de la época (además de ENIAC, Colossus y ABC) se
menciona en este capítulo, y a qué generación de computadoras pertenecería si tuviera que
clasificarse con el criterio de la tabla de generaciones.
```

```{solution} ex-intro-5
:class: dropdown
Las calculadoras **Mark I, II, III y IV** (1945) son electromecánicas y, estrictamente, son
anteriores a la "Primera Generación" tal como se la define en la tabla (1951–1958, basada en
válvulas de vacío), ya que todavía usan relés en lugar de válvulas. Se las suele ubicar como parte
de la etapa pionera (1930–1950) que antecede a la clasificación por generaciones.
```
