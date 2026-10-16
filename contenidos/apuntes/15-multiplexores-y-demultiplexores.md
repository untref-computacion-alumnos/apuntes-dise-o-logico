---
title: "Multiplexores y Demultiplexores"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Multiplexores y Demultiplexores

```{admonition} Sobre este apunte
:class: note
Este capítulo reconstruye y desarrolla en detalle el material de
propio/presentaciones/01-introduccion-a-los-sistemas-digitales.md sobre multiplexores y
demultiplexores (el mismo origen de `muestra-de-formato.md`), incluyendo sus fórmulas de costo
y tiempo de propagación, y agrega los ejercicios propuestos originales de la clase.
```

## 1. Multiplexor (MUX)

Un **multiplexor** es un selector: a partir de $n$ señales de entrada y una señal de
**selección** $s$, entrega en la salida el valor de **una sola** de las entradas, la indicada
por $s$.

### 1.1 Multiplexor de 2 entradas de 1 bit (MUX2_1)

```text
        ┌─────────┐
   x ──►│         │
   y ──►│ MUX2_1  ├──► o
   s ──►│         │
        └─────────┘
```

$$o = \begin{cases} x & s = 0 \\ y & s = 1 \end{cases} \qquad\Longrightarrow\qquad o = x \cdot s' + y \cdot s$$

| $s$ | $o$ |
|:---:|:---:|
| 0 | $x$ |
| 1 | $y$ |

Cuando $s=0$ el término $x \cdot s'$ queda activo y $y \cdot s$ se anula, por lo que $o=x$;
cuando $s=1$ ocurre lo simétrico y $o=y$. Se implementa con dos compuertas AND, una OR y un
inversor para generar $s'$ (ver [Compuertas lógicas](05-compuertas-logicas.md)).

### 1.2 Multiplexor de 4 entradas de 1 bit (MUX4_1)

Tiene 4 entradas de datos ($x_1,x_2,x_3,x_4$) y **2 bits de selección** ($s = s_1 s_0$), ya que
se necesitan $\log_2 4 = 2$ bits para distinguir 4 entradas.

**Implementación jerárquica usando MUX2_1:** se arman tres MUX2_1 en forma de árbol — dos en el
primer nivel (seleccionan entre $x_1,x_2$ y entre $x_3,x_4$ usando $s_0$) y uno en el segundo
nivel (selecciona entre los dos resultados anteriores usando $s_1$):

```text
x1 ─┐
    ├─[MUX2_1]s0─┐
x2 ─┘             │
                  ├─[MUX2_1]s1── o
x3 ─┐             │
    ├─[MUX2_1]s0─┘
x4 ─┘
```

Costo y tiempo de propagación, en función del costo/tiempo de un MUX2_1:

$$T_{MUX4\_1} = 2 \cdot T_{MUX2\_1} = 2 \cdot (T_{AND}+T_{OR})$$

$$C_{MUX4\_1} = 3 \cdot C_{MUX2\_1} = 3 \cdot C_{OR} + 6 \cdot C_{AND}$$

(3 bloques MUX2_1 en total: 2 en el primer nivel + 1 en el segundo).

### 1.3 Multiplexor de 8 entradas de 1 bit (MUX8_1)

Con 8 entradas se necesitan **3 bits de selección** ($s = s_2 s_1 s_0$). Extendiendo el árbol
anterior un nivel más (4 + 2 + 1 = 7 bloques MUX2_1 en total):

$$T_{MUX8\_1} = 3 \cdot T_{MUX2\_1} = 3 \cdot (T_{AND}+T_{OR})$$

$$C_{MUX8\_1} = 7 \cdot C_{MUX2\_1} = 7 \cdot C_{OR} + 14 \cdot C_{AND}$$

### 1.4 Caso general: $MUX_{m\_1}$ con $m = 2^i$

Generalizando el patrón anterior, un multiplexor de $m=2^i$ entradas de 1 bit construido en
árbol a partir de bloques MUX2_1 requiere $i$ niveles de propagación y $m-1$ bloques MUX2_1 en
total:

$$T_{MUX_{m\_1}} = i \cdot T_{MUX2\_1} = i \cdot (T_{AND}+T_{OR})$$

$$C_{MUX_{m\_1}} = (2^i - 1) \cdot C_{MUX2\_1} = (2^i - 1) \cdot C_{OR} + (2^{i+1} - 2) \cdot C_{AND}$$

```{important}
El **tiempo de propagación crece logarítmicamente** con la cantidad de entradas
($i = \log_2 m$), mientras que el **costo (área) crece linealmente** con $m$. Este patrón —
árbol binario de bloques de 2 vías, tiempo $O(\log m)$ y costo $O(m)$— va a repetirse en el
capítulo de [Circuitos contadores](19-circuitos-contadores.md) y en otros bloques jerárquicos.
```

### 1.5 Multiplexor de $n$ bits (buses): MUX2_8

Cuando cada entrada no es un único bit sino un **bus de $n$ bits** (por ejemplo $n=8$), se
replica un MUX2_1 por cada bit del bus, todos comandados por la **misma** señal de selección
$s$:

```text
 s ──┬───────────┬───────────┬──── ... ──┬───────────┐
     │           │           │           │           │
x0,y0│      x1,y1│           │      x7,y7│           │
 ►[MUX2_1]► o0  ►[MUX2_1]► o1   ...   ►[MUX2_1]► o7
```

Como los 8 bloques operan **en paralelo** (no en cascada), el tiempo de propagación **no
aumenta** respecto de un único MUX2_1, pero el costo sí se multiplica por 8:

$$T_{MUX2\_8} = T_{MUX2\_1} = T_{AND}+T_{OR}$$

$$C_{MUX2\_8} = 8 \cdot C_{MUX2\_1} = 8 \cdot C_{OR} + 16 \cdot C_{AND}$$

```{note}
En general, para un multiplexor de $n$ bits por entrada ($MUX_{m\_n}$), el tiempo de
propagación depende solo de $m$ (cantidad de entradas a seleccionar, que determina la
profundidad del árbol), mientras que el costo depende del producto $m \cdot n$ (cada bit del bus
necesita su propio árbol de selección, replicado $n$ veces).
```

## 2. Demultiplexor (DEMUX)

Un **demultiplexor** realiza la operación inversa a la del multiplexor: toma **una** entrada de
datos $x$ y la enruta hacia **una** de varias salidas posibles, según indique la señal de
selección $s$; el resto de las salidas queda en 0.

### 2.1 Demultiplexor de 1 entrada y 2 salidas (DMUX2_1)

```text
        ┌──────────┐
   x ──►│          ├──► o1
   s ──►│ DMUX2_1  ├──► o2
        └──────────┘
```

$$o_1 = \begin{cases} x & s=0 \\ 0 & s=1 \end{cases} \qquad o_2 = \begin{cases} x & s=1 \\ 0 & s=0 \end{cases}$$

$$o_1 = x \cdot s' \qquad\qquad o_2 = x \cdot s$$

### 2.2 Demultiplexor de 1 entrada y 4 salidas (DMUX4_1)

Requiere **2 bits de selección** ($s = s_1 s_0$) y se puede construir jerárquicamente a partir
de tres bloques DMUX2_1, de manera dual al MUX4_1: un primer DMUX2_1 (controlado por $s_1$)
separa la entrada hacia dos ramas, y en cada rama un segundo DMUX2_1 (controlado por $s_0$)
termina de distribuir la señal entre las 4 salidas finales $o_1, o_2, o_3, o_4$:

```text
                  ┌─[DMUX2_1]s0─► o1
        ┌─[DMUX2_1]s1┤
        │           └─[DMUX2_1]s0─► o2
   x ───┤
        │           ┌─[DMUX2_1]s0─► o3
        └─[DMUX2_1]s1┤
                     └─[DMUX2_1]s0─► o4
```

Igual que en el caso del MUX, la construcción en árbol de un $DMUX_{1\_m}$ con $m=2^i$ requiere
$i$ niveles ($T = i \cdot T_{DMUX2\_1}$) y $m-1$ bloques DMUX2_1 ($C=(2^i-1)\cdot C_{DMUX2\_1}$).

## 3. Dualidad entre MUX y DEMUX

```{admonition} MUX y DEMUX son operaciones duales
:class: tip
El multiplexor **selecciona cuál de varias entradas mostrar** en una única salida; el
demultiplexor **selecciona hacia cuál de varias salidas enrutar** una única entrada. Ambos
usan la misma señal de selección con el mismo significado (qué "vía" de las $2^i$ posibles
está activa), y por eso comparten exactamente la misma estructura de árbol, las mismas fórmulas
de costo/tiempo, y la misma relación logarítmica entre profundidad del árbol y cantidad de
vías.
```

Esta dualidad también conecta con el capítulo de
[Codificadores y decodificadores](14-codificadores-y-decodificadores.md): un decodificador es un
demultiplexor con la entrada de datos fija en 1.

## 4. Aplicación: síntesis de funciones lógicas con multiplexores

Los multiplexores no solo sirven para enrutar señales: también pueden usarse para **implementar
directamente cualquier función booleana**, conectando cada entrada de datos del MUX a la
constante 0 o 1 según la fila correspondiente de la tabla de verdad, y usando las variables de
la función como líneas de selección. Esta técnica de síntesis se desarrolla en detalle, con un
ejemplo completo, en el capítulo de [Implementación](10-implementacion.md).

## 5. Resumen

- El **multiplexor** ($MUX_{m\_1}$) selecciona una de $m=2^i$ entradas de 1 bit según $i$ líneas
  de selección; construido en árbol de bloques MUX2_1, tiene tiempo $O(\log m)$ y costo $O(m)$.
- El **multiplexor de buses** ($MUX_{2\_n}$) replica un MUX2_1 por cada bit del bus: mismo
  tiempo que un MUX2_1, costo multiplicado por $n$.
- El **demultiplexor** ($DEMUX_{1\_m}$) enruta una entrada hacia una de $m$ salidas; es
  estructuralmente dual al multiplexor, con las mismas fórmulas de costo y tiempo.
- Un **decodificador** es un caso particular de demultiplexor con la entrada de datos fija en 1
  (capítulo 14).
- Los multiplexores se usan también como bloque de **síntesis universal** de funciones lógicas
  (capítulo 10).

## 6. Ejercicios propuestos

Estos ejercicios estaban planteados en la clase original como práctica de construcción
jerárquica de componentes; se recomienda resolverlos dibujando el circuito y verificando la
fórmula de costo/tiempo resultante.

```{exercise}
:label: ex-mux-1
Implementar un **multiplexor de 8 entradas de 1 bit (MUX8_1)** utilizando exclusivamente
bloques **MUX2_1**. Verificar que resulten 7 bloques en total y 3 niveles de propagación.
```

```{solution} ex-mux-1
:class: dropdown
Se arma un árbol de 3 niveles: 4 bloques MUX2_1 en el primer nivel (combinan las 8 entradas de
a pares con $s_0$), 2 bloques en el segundo nivel (con $s_1$) y 1 bloque en el tercer nivel (con
$s_2$). Total: $4+2+1=7$ bloques, con $i=\log_2 8=3$ niveles, tal como predice la fórmula
general $C=(2^i-1)$ y $T=i \cdot T_{MUX2\_1}$ de la sección 1.4.
```

```{exercise}
:label: ex-mux-2
Implementar un **multiplexor de 8 entradas de 8 bits (MUX8_8)** utilizando bloques **MUX2_8**.
```

```{solution} ex-mux-2
:class: dropdown
Se replica exactamente la estructura en árbol del ejercicio anterior (7 bloques, 3 niveles),
pero usando MUX2_8 en lugar de MUX2_1 en cada nodo del árbol, ya que cada "vía" ahora transporta
un bus de 8 bits en lugar de 1 bit.
```

```{exercise}
:label: ex-mux-3
Determinar el **tiempo de cálculo y el costo (área)** de un MUX8_8 implementado directamente con
bloques **MUX2_1** (es decir, sin pasar por MUX2_8 como bloque intermedio).
```

```{solution} ex-mux-3
:class: dropdown
Un MUX8_8 tiene 8 entradas de 8 bits y necesita 3 líneas de selección. Implementado directo con
MUX2_1, se requiere un árbol de 3 niveles por cada uno de los 8 bits del bus: $7$ bloques
MUX2_1 por bit $\times$ 8 bits $= 56$ bloques MUX2_1 en total. El tiempo sigue siendo el de un
árbol de 3 niveles ($T=3\cdot T_{MUX2\_1}$), porque los 8 árboles (uno por bit) operan en
paralelo.
```

```{exercise}
:label: ex-mux-4
Hallar la **expresión genérica** de tiempo y área de un $MUX_{m\_n}$ (multiplexor de $m$
entradas de $n$ bits cada una) utilizando bloques MUX2_1, con $m = 2^i$.
```

```{solution} ex-mux-4
:class: dropdown
$$T_{MUX_{m\_n}} = i \cdot T_{MUX2\_1} = \log_2 m \cdot (T_{AND}+T_{OR})$$
$$C_{MUX_{m\_n}} = n \cdot (2^i-1) \cdot C_{MUX2\_1} = n\cdot(m-1)\cdot C_{MUX2\_1}$$
El tiempo depende solo de $m$ (profundidad del árbol); el costo depende del producto $n\cdot m$
(un árbol completo replicado por cada uno de los $n$ bits).
```

```{exercise}
:label: ex-mux-5
Implementar un **DMUX4_1** utilizando bloques **DMUX2_1**.
```

```{solution} ex-mux-5
:class: dropdown
Ver el diagrama de árbol de la sección 2.2: un DMUX2_1 controlado por $s_1$ en el primer nivel,
y dos DMUX2_1 controlados por $s_0$ en el segundo nivel, uno por cada rama del primero. Total: 3
bloques, 2 niveles.
```

```{exercise}
:label: ex-mux-6
Implementar un **DMUX8_1** utilizando bloques **DMUX2_1**.
```

```{solution} ex-mux-6
:class: dropdown
Se extiende el árbol del ejercicio anterior un nivel más: 1 bloque controlado por $s_2$, 2
bloques controlados por $s_1$, y 4 bloques controlados por $s_0$. Total: $1+2+4=7$ bloques, 3
niveles — igual estructura y fórmulas que el MUX8_1, por dualidad.
```

```{exercise}
:label: ex-mux-7
Implementar un **DMUX2_8** (demultiplexor de un bus de 8 bits, 2 salidas) utilizando bloques
**DMUX2_1**.
```

```{solution} ex-mux-7
:class: dropdown
Se replica un DMUX2_1 por cada uno de los 8 bits del bus de entrada, todos comandados por la
misma señal de selección $s$ (misma idea que el MUX2_8 de la sección 1.5, pero en sentido
inverso).
```

```{exercise}
:label: ex-mux-8
Implementar un **DMUX8_8** utilizando bloques **DMUX2_8**.
```

```{solution} ex-mux-8
:class: dropdown
Se arma el mismo árbol de 3 niveles y 7 bloques del DMUX8_1 (ejercicio 6), pero reemplazando
cada bloque DMUX2_1 por un DMUX2_8, ya que cada "vía" del árbol ahora transporta un bus de 8
bits en lugar de 1 bit.
```

## 7. Bibliografía

```{bibliography}
:filter: docname in docnames
```
