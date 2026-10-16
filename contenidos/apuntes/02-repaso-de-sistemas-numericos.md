---
title: "Repaso de sistemas numéricos"
subject: "Diseño Lógico"
---

# Repaso de sistemas numéricos

```{admonition} Sobre este apunte
:class: note
Este capítulo repasa contenido de base (asumido como prerrequisito del curso) siguiendo el
tratamiento estándar de la bibliografía de Diseño Lógico {cite}`tocci2007,floyd2000,mandado1998`. Es
la base para [Representación de números enteros, fraccionarios y
negativos](03-representacion-de-numeros-enteros-fraccionarios-y-negativos.md), donde se aborda cómo
representar signo y parte fraccionaria.
```

## 1. Sistemas de numeración posicionales

Un **sistema de numeración posicional** representa una cantidad como una secuencia de dígitos, en
la que cada dígito aporta un valor que depende tanto de su símbolo como de la **posición** que ocupa
dentro de la secuencia. Todo sistema posicional queda definido por su **base** (o _radix_) $b$: la
cantidad de símbolos distintos disponibles para representar dígitos.

Dado un número con dígitos $d_{n-1} d_{n-2} \ldots d_1 d_0 . d_{-1} d_{-2} \ldots d_{-m}$ en base
$b$, su valor decimal equivalente es:

$$
N = \sum_{i=-m}^{n-1} d_i \cdot b^i
$$

Es decir, cada dígito $d_i$ aporta $d_i \cdot b^i$ al valor total: $b^i$ es el **peso** posicional
de esa posición. El punto que separa la parte entera de la fraccionaria se llama, según la base,
punto decimal (base 10), punto binario (base 2), etc.

```{note} Nota
El sistema decimal que se usa a diario (base 10, dígitos 0–9) es solo un caso particular. La
elección de base 10 es una convención histórica (contamos con diez dedos), no una necesidad
matemática: cualquier base entera mayor que 1 permite representar cualquier cantidad.
```

## 2. Los sistemas usados en diseño digital

En el diseño de sistemas digitales se trabaja fundamentalmente con cuatro sistemas de numeración:

| Sistema     | Base | Dígitos válidos                                |
| ----------- | :--: | ---------------------------------------------- |
| Decimal     |  10  | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9                   |
| Binario     |  2   | 0, 1                                           |
| Octal       |  8   | 0, 1, 2, 3, 4, 5, 6, 7                         |
| Hexadecimal |  16  | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F |

### 2.1. Sistema binario

El **sistema binario** es el sistema natural de los circuitos digitales, porque un conmutador (ver
[Introducción a los sistemas digitales](01-introduccion-a-los-sistemas-digitales.md)) solo puede
estar en dos estados: abierto o cerrado, que se identifican con los dígitos **0** y **1**. Cada
dígito binario se llama **bit** (_binary digit_). Un grupo de 4 bits se llama **nibble**, y un grupo
de 8 bits se llama **byte**.

Ejemplo: el número binario $1011_2$ vale, en decimal:

$$
1011_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 8+0+2+1 = 11_{10}
$$

### 2.2. Sistema octal y hexadecimal

El sistema **octal** (base 8) y el **hexadecimal** (base 16) se usan como una notación abreviada del
binario: como $8=2^3$ y $16=2^4$, cada dígito octal representa exactamente 3 bits, y cada dígito
hexadecimal representa exactamente 4 bits. Esto hace que la conversión binario $\leftrightarrow$
octal y binario $\leftrightarrow$ hexadecimal sea puramente mecánica (agrupar bits), sin necesidad
de pasar por decimal.

```{tip} A tener en cuenta
El hexadecimal es el que más se usa en la práctica (direcciones de memoria, volcados de datos,
colores en diseño web, etc.) porque un byte completo (8 bits) se escribe con exactamente **dos**
dígitos hexadecimales: por ejemplo, $11111111_2 = FF_{16} = 255_{10}$.
```

### 2.3. Tabla de equivalencias (0 a 15)

| Decimal | Binario | Octal | Hexadecimal |
| :-----: | :-----: | :---: | :---------: |
|    0    |  0000   |   0   |      0      |
|    1    |  0001   |   1   |      1      |
|    2    |  0010   |   2   |      2      |
|    3    |  0011   |   3   |      3      |
|    4    |  0100   |   4   |      4      |
|    5    |  0101   |   5   |      5      |
|    6    |  0110   |   6   |      6      |
|    7    |  0111   |   7   |      7      |
|    8    |  1000   |  10   |      8      |
|    9    |  1001   |  11   |      9      |
|   10    |  1010   |  12   |      A      |
|   11    |  1011   |  13   |      B      |
|   12    |  1100   |  14   |      C      |
|   13    |  1101   |  15   |      D      |
|   14    |  1110   |  16   |      E      |
|   15    |  1111   |  17   |      F      |

## 3. Conversión entre bases

### 3.1. De base $b$ a decimal

Se aplica directamente la definición posicional: se multiplica cada dígito por su peso $b^i$ y se
suman los resultados.

$$
3A2_{16} = 3 \cdot 16^2 + 10 \cdot 16^1 + 2 \cdot 16^0 = 768 + 160 + 2 = 930_{10}
$$

### 3.2. De decimal a base $b$: método de las divisiones sucesivas

Para convertir la **parte entera** de un número decimal a base $b$, se divide sucesivamente por $b$
y se van registrando los restos; el número en la nueva base se lee tomando los restos **del último
al primero**.

Ejemplo: convertir $45_{10}$ a binario.

| División | Cociente | Resto |
| -------- | :------: | :---: |
| 45 ÷ 2   |    22    |   1   |
| 22 ÷ 2   |    11    |   0   |
| 11 ÷ 2   |    5     |   1   |
| 5 ÷ 2    |    2     |   1   |
| 2 ÷ 2    |    1     |   0   |
| 1 ÷ 2    |    0     |   1   |

Leyendo los restos de abajo hacia arriba: $45_{10} = 101101_2$.

Para convertir la **parte fraccionaria**, se multiplica sucesivamente por $b$ y se van tomando las
partes enteras que van resultando, esta vez **de la primera a la última**. Por ejemplo, $0,625_{10}$
a binario:

| Multiplicación | Resultado | Parte entera |
| -------------- | :-------: | :----------: |
| 0,625 × 2      |   1,25    |      1       |
| 0,25 × 2       |    0,5    |      0       |
| 0,5 × 2        |    1,0    |      1       |

Por lo tanto $0,625_{10} = 0,101_2$ (el proceso termina cuando la parte fraccionaria da 0; en
general, puede no terminar nunca, dando una representación periódica).

### 3.3. Binario $leftrightarrow$ Octal y binario $\leftrightarrow$ hexadecimal (agrupación de bits)

Como $8=2^3$, para pasar de binario a octal se agrupan los bits de a **3**, empezando desde el punto
binario hacia ambos lados, completando con ceros si hace falta:

$$
10\,110\,101_2 = \underbrace{010}_{2}\,\underbrace{110}_{6}\,\underbrace{101}_{5} \Rightarrow 265_8
$$

Como $16=2^4$, para pasar de binario a hexadecimal se agrupan los bits de a **4:**

$$
10\,1101\,01_2 = \underbrace{0010}_{2}\,\underbrace{1101}_{D}\Rightarrow 2D_{16}
$$

Para el sentido inverso (octal $\leftrightarrow$ binario o hexadecimal $\leftrightarrow$ binario) se
hace lo opuesto: cada dígito se expande a su grupo de 3 o 4 bits respectivamente.

### 3.4. Decimal $\leftrightarrow$ hexadecimal

Se puede convertir directamente por divisiones sucesivas por 16 (igual que en la sección 3.2., pero
usando $b=16$ y traduciendo los restos mayores a 9 con las letras A–F), o bien pasando por binario
como paso intermedio si resulta más cómodo mentalmente.

## 4. Aritmética binaria

Las reglas de la aritmética binaria son análogas a las de la aritmética decimal, pero con una tabla
de sumar mucho más simple al tener solo dos dígitos.

### 4.1. Suma binaria

| $a$ | $b$ | Acarreo de entrada | Suma | Acarreo de salida |
| :-: | :-: | :----------------: | :--: | :---------------: |
|  0  |  0  |         0          |  0   |         0         |
|  0  |  1  |         0          |  1   |         0         |
|  1  |  0  |         0          |  1   |         0         |
|  1  |  1  |         0          |  0   |         1         |

Ejemplo de suma de dos números de varios bits, con propagación de acarreo:

```text
  1 1 1 1   (acarreos)
  0 1 1 1   (7)
+ 0 1 0 1   (5)
 ---------
  1 1 0 0   (12)
```

```{note} Nota
Esta tabla de suma con acarreo es exactamente la que se usa para construir el **sumador completo**
(*full adder*), el bloque combinacional que se estudia en detalle en [Sumadores, restadores y
comparadores](16-sumadores-restadores-y-comparadores.md).
```

### 4.2. Resta binaria

La resta binaria bit a bit sigue la regla usual, pidiendo **préstamo** (_borrow_) cuando el
minuendo es menor que el sustraendo:

```text
  0         (préstamo)
  1 0 1 1   (11)
- 0 1 0 1   (5)
 ---------
  0 1 1 0   (6)
```

En la práctica, los circuitos digitales casi nunca implementan un restador "directo" bit a bit como
el de arriba: en cambio, la resta se realiza sumando el **complemento a 2** del sustraendo, tal como
se explica en
[Representación de números enteros, fraccionarios y negativos](03-representacion-de-numeros-enteros-fraccionarios-y-negativos.md).

### 4.3. Multiplicación y división binaria

La multiplicación binaria se realiza igual que la multiplicación decimal "en columna", con la
ventaja de que cada producto parcial es simplemente el multiplicando (si el dígito del multiplicador
es 1) o cero (si es 0):

```text
      1 0 1 1   (11)
    ×   1 0 1   (5)
    ---------
      1 0 1 1
    0 0 0 0
  1 0 1 1
  ---------
  1 1 0 1 1 1   (55)
```

La división binaria sigue el mismo algoritmo de "restas sucesivas" que la división decimal larga.
En la práctica, los circuitos de multiplicación y división rara vez se implementan de forma directa
con estos algoritmos "a mano"; se usan estructuras dedicadas construidas a partir de sumadores (que
se estudian en el capítulo de sumadores) y desplazamientos (ver
[Registros](20-registros.md), registro de desplazamiento).

## 5. Bibliografía

```{bibliography}
:filter: docname in docnames
```

## 6. Resumen

- Un sistema de numeración posicional queda definido por su base $b$; el valor de un número es la
  suma de cada dígito multiplicado por su peso posicional $b^i$.
- Diseño Lógico trabaja principalmente con decimal (base 10), binario (base 2), octal (base 8) y
  hexadecimal (base 16). Octal y hexadecimal son taquigrafías del binario porque $8=2^3$ y
  $16=2^4$.
- Convertir de base $b$ a decimal es aplicar la definición posicional; convertir de decimal a base
  $b$ se hace con divisiones sucesivas (parte entera) y multiplicaciones sucesivas (parte
  fraccionaria).
- Convertir entre binario y octal/hexadecimal es puramente mecánico: agrupar o expandir bits de a 3
  o de a 4, sin pasar por decimal.
- La aritmética binaria (suma, resta, multiplicación, división) sigue las mismas reglas que la
  decimal, adaptadas a solo dos dígitos; la tabla de suma binaria con acarreo es la base del sumador
  completo que se ve más adelante en el apunte.

## 7. Ejercicios propuestos

```{exercise}
:label: ex-numeros-1
Convertí $101101_2$ a decimal, octal y hexadecimal.
```

```{solution} ex-numeros-1
:class: dropdown
Decimal: $101101_2 = 32+0+8+4+0+1 = 45_{10}$.
Octal: agrupando de a 3 desde la derecha, $101\,101_2 = 55_8$.
Hexadecimal: agrupando de a 4 desde la derecha, $0010\,1101_2 = 2D_{16}$.
```

```{exercise}
:label: ex-numeros-2
Convertí $173_{10}$ a binario usando el método de las divisiones sucesivas.
```

```{solution} ex-numeros-2
:class: dropdown
173 ÷ 2 = 86 resto 1; 86 ÷ 2 = 43 resto 0; 43 ÷ 2 = 21 resto 1; 21 ÷ 2 = 10 resto 1; 10 ÷ 2 = 5
resto 0; 5 ÷ 2 = 2 resto 1; 2 ÷ 2 = 1 resto 0; 1 ÷ 2 = 0 resto 1.
Leyendo de abajo hacia arriba: $173_{10} = 10101101_2$.
```

```{exercise}
:label: ex-numeros-3
Convertí $0,8125_{10}$ a binario con el método de las multiplicaciones sucesivas.
```

```{solution} ex-numeros-3
:class: dropdown
0,8125×2=1,625→1; 0,625×2=1,25→1; 0,25×2=0,5→0; 0,5×2=1,0→1.
$0,8125_{10} = 0,1101_2$.
```

```{exercise}
:label: ex-numeros-4
Sumá en binario $01011011_2 + 00110110_2$ y verificá el resultado convirtiendo ambos operandos y el
resultado a decimal.
```

```{solution} ex-numeros-4
:class: dropdown
$01011011_2 = 91_{10}$, $00110110_2 = 54_{10}$, $91+54=145_{10}$.
En binario: $01011011 + 00110110 = 10010001_2$, que efectivamente equivale a $145_{10}$.
```

```{exercise}
:label: ex-numeros-5
Convertí directamente (sin pasar por binario) $2F3_{16}$ a decimal, y luego $500_{10}$ a
hexadecimal.
```

```{solution} ex-numeros-5
:class: dropdown
$2F3_{16} = 2\cdot16^2+15\cdot16^1+3\cdot16^0 = 512+240+3 = 755_{10}$.
$500_{10}$: 500÷16=31 resto 4; 31÷16=1 resto 15(F); 1÷16=0 resto 1. Leyendo al revés:
$500_{10}=1F4_{16}$.
```
