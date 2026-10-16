---
title: "Codificadores y Decodificadores"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Codificadores y Decodificadores

```{admonition} Sobre este apunte
:class: note
La sección de **decodificadores** de este capítulo reconstruye el material de
propio/presentaciones/01-introduccion-a-los-sistemas-digitales.md (el mismo origen de
`muestra-de-formato.md`), que desarrolla el decodificador DECODE3 y su relación con el
demultiplexor. La sección de **codificadores** no está cubierta en las presentaciones de la
cátedra y se completa con bibliografía estándar de la materia ({cite}`tocci2007`,
{cite}`floyd2000`).
```

## 1. Decodificador

Un **decodificador** es un circuito combinacional con $n$ entradas y $2^n$ salidas, que activa
(pone en 1) **exactamente una** de sus salidas según el valor binario presente en la entrada;
todas las demás salidas quedan en 0. La salida es, por lo tanto, una codificación **"one-hot"**
(un único bit en 1, en la posición indicada por el valor de entrada).

```text
        ┌───────────┐
 x2..0 ─►│  DECODE3  ├─► o7..0
  (3)   │           │  (8)
        └───────────┘
```

### 1.1 Ejemplo: decodificador de 3 a 8 (DECODE3)

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

Cada salida $o_i$ es, en términos de la entrada, exactamente el minterm correspondiente al
valor $i$: por ejemplo $o_5 = x_2\cdot x_1'\cdot x_0$ (fila $101$). Un decodificador de $n$ a
$2^n$ es, entonces, un circuito que genera **los $2^n$ minterms** de $n$ variables como salidas
físicas independientes — la conexión con las formas canónicas del capítulo
[Formas canónicas](07-formas-canonicas.md) es directa.

### 1.2 Relación entre decodificador y demultiplexor

El decodificador se puede implementar directamente con un **demultiplexor** (ver
[Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md)): basta con conectar la
entrada de datos $x$ del demultiplexor a una constante lógica **1**. Toda la información que
"viaja" es la selección, y el demultiplexor se limita a enrutar ese 1 fijo hacia la salida
indicada.

Por ejemplo, un `DECODE2` (2 entradas → 4 salidas) se arma con un `DEMUX4_1` cuya entrada de
datos está atada a 1 y cuyas entradas de selección son las 2 entradas del decodificador:

```text
        ┌───────────┐
   1 ──►│           ├─► o0
        │  DEMUX4_1 ├─► o1
 x1,x0─►│  (s1,s0)  ├─► o2
        │           ├─► o3
        └───────────┘
```

```{note}
Esta dualidad decodificador↔demultiplexor es la misma que existe entre codificador y
multiplexor en el sentido inverso: el multiplexor "elige qué entrada mostrar", el decodificador
"elige qué salida activar". Son circuitos estructuralmente relacionados, aunque se usan con
propósitos distintos.
```

## 2. Decodificadores con entrada de habilitación (enable)

En la práctica, los decodificadores comerciales incluyen una o más entradas de
**habilitación** (**enable**, a veces activas en bajo): mientras la habilitación no esté
activa, todas las salidas permanecen en su valor inactivo, sin importar el valor de las
entradas de selección. Esto permite:

- **Apagar** el decodificador cuando no se lo necesita (por ejemplo, para no interferir con
  otro dispositivo que comparte el mismo bus de salidas).
- **Expandir** decodificadores pequeños para construir uno más grande, usando bits adicionales
  de dirección para habilitar el bloque correcto.

### 2.1 Ejemplo: decodificador de 4 a 16 con dos DECODE3 y una entrada extra

```text
                         ┌───────────┐
                  x3 ──┬─►EN        ├─► o0..o7
                       │  │ DECODE3  │
              x2,x1,x0 ├─►│  (x2..0) │
                       │  └───────────┘
                       │
                       │  ┌───────────┐
                       └─►EN'        ├─► o8..o15
                          │ DECODE3  │
              x2,x1,x0 ──►│  (x2..0) │
                          └───────────┘
```

El bit más significativo $x_3$ selecciona cuál de los dos bloques DECODE3 está habilitado (uno
mediante $x_3$ directo, el otro mediante $x_3'$); los tres bits restantes ($x_2,x_1,x_0$) se
comparten como entrada de selección de ambos bloques.

## 3. Aplicaciones de decodificadores

### 3.1 Selección de dispositivos (chip select)

En un sistema con varios dispositivos de memoria o periféricos conectados al mismo bus de
direcciones, un decodificador conectado a los bits más significativos de la dirección genera
las señales individuales de **selección de chip** (*chip select*, CS), activando un único
dispositivo por vez según el rango de direcciones al que pertenece.

### 3.2 Decodificador BCD a 7 segmentos

Un caso particular muy usado es el decodificador que traduce un dígito en **BCD** (ver
[Códigos numéricos](12-codigos-numericos.md)) a las señales necesarias para encender los 7
segmentos de un display de 7 segmentos, de manera que se visualice el dígito decimal
correspondiente.

| BCD ($x_3x_2x_1x_0$) | Dígito | $a$ | $b$ | $c$ | $d$ | $e$ | $f$ | $g$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0000 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0001 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0010 | 2 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 0011 | 3 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 0100 | 4 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 0101 | 5 | 1 | 0 | 1 | 1 | 0 | 1 | 1 |
| 0110 | 6 | 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| 0111 | 7 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1000 | 8 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1001 | 9 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |

Cada segmento ($a$ a $g$) es, en definitiva, una función booleana de 4 variables que puede
obtenerse mediante los métodos de los capítulos [Formas canónicas](07-formas-canonicas.md) y
[Redundancias](08-redundancias.md), tomando como "no importa" (don't care) las combinaciones
$1010$ a $1111$ que no representan dígitos BCD válidos.

## 4. Codificador (encoder)

Un **codificador** realiza la operación **inversa** a la de un decodificador: tiene $2^n$
entradas y $n$ salidas; cuando **una** de las entradas está activa, la salida entrega el código
binario correspondiente a esa entrada.

```text
        ┌───────────┐
 i7..0 ─►│ ENCODER   ├─► o2..0
  (8)   │  8 a 3     │  (3)
        └───────────┘
```

### 4.1 Ejemplo: codificador de 8 a 3

| Entrada activa | $o_2 o_1 o_0$ |
|:---:|:---:|
| $i_0$ | 000 |
| $i_1$ | 001 |
| $i_2$ | 010 |
| $i_3$ | 011 |
| $i_4$ | 100 |
| $i_5$ | 101 |
| $i_6$ | 110 |
| $i_7$ | 111 |

Cada salida se obtiene como el OR de las entradas cuyo índice tiene ese bit en 1, por ejemplo:

$$o_0 = i_1 + i_3 + i_5 + i_7 \qquad o_1 = i_2+i_3+i_6+i_7 \qquad o_2 = i_4+i_5+i_6+i_7$$

```{warning}
Este codificador simple asume que **una sola** entrada está activa a la vez; si dos o más
entradas se activan simultáneamente, la salida no representa correctamente ninguna de ellas
(por ejemplo, si $i_3$ e $i_5$ están ambas en 1, el circuito de arriba entrega $o=111$, que
corresponde a $i_7$, una entrada que ni siquiera está activa). Ese problema lo resuelve el
codificador de prioridad.
```

## 5. Codificador de prioridad (priority encoder)

El **codificador de prioridad** resuelve el problema de entradas simultáneas asignando una
**prioridad** a cada entrada (típicamente, a mayor índice, mayor prioridad): cuando varias
entradas están activas, la salida codifica **la de mayor prioridad entre las activas**, e
ignora al resto.

### 5.1 Ejemplo: codificador de prioridad de 8 a 3 (análogo al 74148 comercial)

| $i_7$ | $i_6$ | $i_5$ | $i_4$ | $i_3$ | $i_2$ | $i_1$ | $i_0$ | $o_2 o_1 o_0$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | X | X | X | X | X | X | X | 111 |
| 0 | 1 | X | X | X | X | X | X | 110 |
| 0 | 0 | 1 | X | X | X | X | X | 101 |
| 0 | 0 | 0 | 1 | X | X | X | X | 100 |
| 0 | 0 | 0 | 0 | 1 | X | X | X | 011 |
| 0 | 0 | 0 | 0 | 0 | 1 | X | X | 010 |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | X | 001 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 000 |

(donde `X` indica "no importa": una entrada de menor prioridad puede estar en cualquier valor
sin afectar el resultado, ya que la de mayor prioridad presente domina la salida).

```{tip}
El circuito integrado comercial 74148 es un codificador de prioridad de 8 a 3 con entradas y
salidas activas en bajo, y agrega además una salida adicional (GS, *group select*) que indica si
alguna entrada estaba activa, y una entrada de habilitación en cascada (EI/EO) para encadenar
varios 74148 y construir codificadores de prioridad de más entradas (por ejemplo, 16 a 4).
```

### 5.2 Aplicación típica

Un uso clásico del codificador de prioridad es el manejo de **interrupciones** en un procesador:
cada línea de entrada representa una posible interrupción (de distintos periféricos), y el
codificador de prioridad determina cuál atender primero cuando ocurren varias simultáneamente.

## 6. Resumen

- Un **decodificador** de $n$ a $2^n$ activa una única salida (one-hot) según el valor binario
  de entrada; cada salida es, de hecho, un minterm de las variables de entrada.
- Un decodificador puede implementarse con un **demultiplexor** cuya entrada de datos está fija
  en 1.
- Las entradas de **habilitación** permiten apagar el decodificador o expandirlo en bloques más
  grandes.
- Aplicaciones típicas: selección de dispositivos (chip select) y decodificación BCD a 7
  segmentos.
- Un **codificador** realiza la operación inversa: de $2^n$ entradas (una activa) a $n$ salidas
  con el código correspondiente.
- El **codificador de prioridad** resuelve el caso de múltiples entradas activas
  simultáneamente, entregando el código de la entrada de mayor prioridad.

## 7. Ejercicios propuestos

```{exercise}
:label: ex-decod-1
Diseñar (dar la tabla de verdad y la ecuación de cada salida) un decodificador de 2 a 4 sin
entrada de habilitación.
```

```{solution} ex-decod-1
:class: dropdown
Con entradas $x_1,x_0$: $o_0=x_1'x_0'$, $o_1=x_1'x_0$, $o_2=x_1x_0'$, $o_3=x_1x_0$. Cada salida
es el minterm correspondiente a su índice, análogo al DECODE3 pero con 2 variables.
```

```{exercise}
:label: ex-decod-2
Explicar cómo se implementaría un decodificador de 3 a 8 usando únicamente un `DEMUX8_1` (ver
[Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md)).
```

```{solution} ex-decod-2
:class: dropdown
Se conecta la entrada de datos del `DEMUX8_1` a una constante lógica 1, y las 3 líneas de
selección del demultiplexor pasan a ser las 3 entradas del decodificador. Cada salida del
demultiplexor reproduce el 1 fijo únicamente cuando la selección coincide con su índice, que es
exactamente el comportamiento de un decodificador.
```

```{exercise}
:label: ex-decod-3
Usando la tabla BCD a 7 segmentos de la sección 3.2, escribir la expresión booleana del
segmento $g$ como suma de minterms (usar $x_3x_2x_1x_0$).
```

```{solution} ex-decod-3
:class: dropdown
El segmento $g$ vale 1 para los dígitos 2,3,4,5,6,8,9. En minterms:
$g = \sum m(2,3,4,5,6,8,9)$, es decir
$g = x_3'x_2'x_1x_0' + x_3'x_2'x_1x_0 + x_3'x_2x_1'x_0' + x_3'x_2x_1'x_0 + x_3'x_2x_1x_0' +
x_3x_2'x_1'x_0' + x_3x_2'x_1'x_0$. En un caso real se simplificaría con Karnaugh (capítulo
[Redundancias](08-redundancias.md)) antes de implementarlo.
```

```{exercise}
:label: ex-decod-4
En el codificador de prioridad de la sección 5.1, indicar la salida si $i_2=1$, $i_5=1$ y el
resto de las entradas están en 0.
```

```{solution} ex-decod-4
:class: dropdown
Entre las entradas activas ($i_2$ e $i_5$), $i_5$ tiene mayor prioridad (mayor índice). La
salida es $o_2o_1o_0 = 101$, ignorando a $i_2$.
```

## 8. Bibliografía

```{bibliography}
:filter: docname in docnames
```
