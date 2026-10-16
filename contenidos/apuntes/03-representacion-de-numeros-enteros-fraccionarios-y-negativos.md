---
title: "Representación de números enteros, fraccionarios y negativos"
subject: "Diseño Lógico"
---

# Representación de números enteros, fraccionarios y negativos

```{admonition} Sobre este apunte
:class: note
Este capítulo desarrolla, con el tratamiento estándar de la bibliografía de Diseño Lógico
{cite}`tocci2007,harris2012,floyd2000`, cómo se representan en binario los números con signo y los
números fraccionarios. Es continuación directa de [Repaso de sistemas
numéricos](02-repaso-de-sistemas-numericos.md).
```

## 1. El problema de representar el signo

Los circuitos digitales solo manejan **bits** (0 y 1): no existe un símbolo físico para "+" o "−".
Por lo tanto, cualquier convención para representar números negativos debe codificar el signo
usando los mismos bits que codifican la magnitud. Existen tres convenciones clásicas para números
enteros con signo de $n$ bits: **signo-magnitud**, **complemento a 1** y **complemento a 2**.

En las tres, el bit más significativo (MSB) se reserva como **bit de signo:** 0 indica número
positivo y 1 indica número negativo. Lo que cambia entre las tres convenciones es cómo se codifican
los $n-1$ bits restantes cuando el número es negativo.

## 2. Signo-magnitud

En **signo-magnitud**, el bit de signo se antepone directamente a la magnitud del número, escrita en
binario puro. Por ejemplo, con $n=8$ bits:

$$
+5 = 0000\,0101_2 \qquad\qquad -5 = 1000\,0101_2
$$

```{warning} Atención
Signo-magnitud tiene dos representaciones distintas para el cero: $+0 = 00000000$ y
$-0 = 10000000$. Esto complica el diseño de los circuitos aritméticos (hay que tratar ambos casos
como "iguales" explícitamente) y es la razón principal por la que esta representación **no** se usa
en las unidades aritméticas de las computadoras actuales.
```

## 3. Complemento a 1

El **complemento a 1** (C1) de un número binario se obtiene invirtiendo todos sus bits ($0
\rightarrow 1$, $1 \rightarrow 0$).

Un número negativo se representa como el complemento a 1 de su magnitud positiva:

$$
+5 = 0000\,0101_2 \qquad\qquad -5 = 1111\,1010_2 \;(\text{C1 de } 0000\,0101_2)
$$

Complemento a 1 mejora la aritmética respecto de signo-magnitud (la resta puede hacerse sumando el
complemento), pero conserva el problema del **cero doble:** $+0 = 00000000$ y
$-0 = 11111111$. Además, la suma en C1 requiere un ajuste adicional llamado **acarreo circular**
(_end-around carry_): el acarreo de salida del bit más significativo debe volver a sumarse al bit
menos significativo del resultado.

## 4. Complemento a 2

El **complemento a 2** (C2) es la representación que efectivamente usan las computadoras actuales.
Se obtiene sumando 1 al complemento a 1:

$$
\text{C2}(N) = \text{C1}(N) + 1
$$

Ejemplo con $n=8$ bits:

$$
+5 = 0000\,0101_2
$$

$$
\text{C1}(5) = 1111\,1010_2 \qquad\Rightarrow\qquad \text{C2}(5) = 1111\,1011_2 = -5
$$

```{tip} Consejo
Atajo práctico para obtener el complemento a 2 sin pasar por el complemento a 1: partiendo desde el
bit menos significativo, se copian todos los bits tal cual hasta el primer 1 (inclusive), y a partir
de ahí se invierten todos los bits restantes. Para $0000\,0101$: se copia "1" y el "0" que le sigue
a la izquierda ya invertido en el resto... en la práctica alcanza con: invertir todo y sumar 1, que
es el método general y siempre funciona.
```

### 4.1. Por qué complemento a 2 es el estándar

- **Un único cero:** $\text{C2}(0) = 00000000$, no hay ambigüedad de "cero positivo" vs. "cero
  negativo".
- **Aritmética uniforme:** la suma de dos números en C2 (positivos, negativos o mixtos) se realiza
  con el **mismo circuito sumador binario** que para números sin signo, sin casos especiales ni
  acarreo circular. La resta $A-B$ se implementa como $A + \text{C2}(B)$.
- **Rango asimétrico pero simple:** con $n$ bits, el rango representable es
  $[-2^{n-1},\, 2^{n-1}-1]$ (un negativo más que positivos, precisamente porque no se "desperdicia"
  ningún patrón de bits en un segundo cero).

Esta es la razón por la que el sumador/restador que se estudia en
[Sumadores, restadores y comparadores](16-sumadores-restadores-y-comparadores.md) se construye
asumiendo operandos en complemento a 2.

### 4.2. Suma y resta en complemento a 2

La suma se realiza bit a bit igual que en binario sin signo, ignorando cualquier acarreo que salga
del bit de signo (ese acarreo se descarta, no indica error por sí solo). Ejemplo, $5 + (-3)$ con
$n=8$ bits:

```text
    0000 0101   (+5)
  + 1111 1101   (-3, complemento a 2 de 3)
  -----------
  1 0000 0010   (el acarreo de salida se descarta → resultado: 0000 0010 = +2)
```

### 4.3. Detección de desborde (_overflow_)

El **desborde** (_overflow_) ocurre cuando el resultado de sumar dos números de $n$ bits no entra en
el rango representable con $n$ bits en complemento a 2 (por ejemplo, sumar dos positivos grandes y
obtener un resultado que "se desborda" hacia el rango negativo).

```{important} Importante
**Regla práctica de detección de overflow:** hay desborde si y solo si el acarreo que **entra** al
bit de signo es distinto del acarreo que **sale** del bit de signo. Una forma equivalente, más
intuitiva: hay desborde si se suman dos números del **mismo signo** y el resultado tiene el **signo
opuesto**. Sumar dos números de signo distinto **nunca** produce desborde en complemento a 2.
```

### 4.4. Rango representable

| Representación  | Rango con $n$ bits            | Cantidad de ceros |
| --------------- | ----------------------------- | :---------------: |
| Signo-magnitud  | $[-(2^{n-1}-1),\, 2^{n-1}-1]$ |         2         |
| Complemento a 1 | $[-(2^{n-1}-1),\, 2^{n-1}-1]$ |         2         |
| Complemento a 2 | $[-2^{n-1},\, 2^{n-1}-1]$     |         1         |

### 4.5. Comparación de las tres representaciones (n = 4 bits)

| Decimal | Signo-magnitud | Complemento a 1 | Complemento a 2 |
| :-----: | :------------: | :-------------: | :-------------: |
|   +7    |      0111      |      0111       |      0111       |
|   +3    |      0011      |      0011       |      0011       |
|   +0    |      0000      |      0000       |      0000       |
|   −0    |      1000      |      1111       |  — (no existe)  |
|   −3    |      1011      |      1100       |      1101       |
|   −7    |      1111      |      1000       |      1001       |
|   −8    | — (no existe)  |  — (no existe)  |      1000       |

## 5. Números fraccionarios: punto fijo

En una representación de **punto fijo** (_fixed-point_), se reserva de antemano una cantidad fija
de bits para la parte entera y otra para la parte fraccionaria, separadas por un punto binario
implícito (no almacenado). Por ejemplo, con un formato de 4 bits enteros y 4 fraccionarios, el
patrón $0101.1100_2$ representa:

$$
0101.1100_2 = (0101_2) + (1100_2 \cdot 2^{-4}) = 5 + 0{,}75 = 5{,}75_{10}
$$

La parte fraccionaria se interpreta con pesos negativos de la base: el primer bit a la derecha del
punto pesa $2^{-1}=0{,}5$, el segundo $2^{-2}=0{,}25$, etc.

```{note} Nota
Convertir una fracción binaria a decimal es aplicar la misma fórmula posicional del capítulo
anterior, extendida a exponentes negativos: $0.101_2 = 1\cdot2^{-1}+0\cdot2^{-2}+1\cdot2^{-3} =
0{,}5+0+0{,}125 = 0{,}625_{10}$.
```

La ventaja de punto fijo es la simplicidad del hardware (los sumadores/restadores son los mismos que
para enteros, solo hay que recordar dónde está el punto). La desventaja es que el rango y la
precisión quedan fijos de antemano: no sirve para representar cómodamente números muy grandes y muy
pequeños con la misma cantidad de bits.

## 6. Números fraccionarios: punto flotante (IEEE 754)

El estándar **IEEE 754** resuelve la limitación de punto fijo permitiendo que la posición del punto
"flote", representando un número en notación similar a la notación científica:

$$
N = (-1)^S \cdot 1{,}M \cdot 2^{E - \text{sesgo}}
$$

En **precisión simple** (32 bits), el formato se organiza así:

| Campo            | Signo ($S$) | Exponente ($E$) | Mantisa ($M$) |
| ---------------- | :---------: | :-------------: | :-----------: |
| Cantidad de bits |      1      |        8        |      23       |

- **Signo ($S$):** 0 para positivo, 1 para negativo.
- **Exponente ($E$):** almacenado con un **sesgo** (_bias_) de 127, para poder representar
  exponentes negativos sin usar un bit de signo separado.
- **Mantisa ($M$):** la parte fraccionaria de la mantisa normalizada; el "1" entero se asume
  implícito y no se almacena (_bit oculto_).

### Ejemplo de codificación

Codificar $12{,}5_{10}$ en IEEE 754 simple precisión:

1. Convertir a binario: $12{,}5_{10} = 1100{,}1_2$.
2. Normalizar (notación científica en base 2): $1100{,}1_2 = 1{,}1001_2 \times 2^3$.
3. Signo: positivo $\rightarrow S=0$.
4. Exponente con sesgo: $E = 3 + 127 = 130 = 10000010_2$.
5. Mantisa (23 bits, se completa con ceros a la derecha): $M = 10010000000000000000000_2$.

$$
12{,}5_{10} = \underbrace{0}_{S}\;\underbrace{10000010}_{E}\;\underbrace{10010000000000000000000}_{M}
$$

```{tip} Nota
No hace falta memorizar el algoritmo de codificación IEEE 754 para este curso; lo importante es
entender la **idea:** separar el número en signo, exponente (que determina la "escala") y mantisa
(que determina la "precisión" dentro de esa escala), de forma análoga a la notación científica
decimal $1{,}25 \times 10^1$.
```

## 7. Bibliografía

```{bibliography}
:filter: docname in docnames
```

## 8. Resumen

- Todo esquema de números con signo reserva el bit más significativo como bit de signo; lo que
  cambia entre esquemas es cómo se codifica la magnitud de los negativos.
- **Signo-magnitud** y **complemento a 1** tienen dos representaciones del cero y requieren
  circuitería especial para la aritmética. **Complemento a 2** tiene un único cero y permite sumar
  con el mismo sumador binario que se usa para números sin signo — por eso es el estándar universal.
- La resta en complemento a 2 se implementa como una suma: $A-B = A+\text{C2}(B)$.
- El **desborde** (overflow) en complemento a 2 ocurre solo al sumar dos números del mismo signo y
  obtener un resultado de signo opuesto.
- Con $n$ bits en complemento a 2 el rango es $[-2^{n-1}, 2^{n-1}-1]$.
- Los números fraccionarios pueden representarse en **punto fijo** (simple, pero de rango y
  precisión fijos) o en **punto flotante** (norma IEEE 754: signo, exponente sesgado y mantisa),
  que permite un rango dinámico mucho mayor a costa de mayor complejidad de hardware.

## 9. Ejercicios propuestos

```{exercise}
:label: ex-repnum-1
Representá $-19_{10}$ en signo-magnitud, complemento a 1 y complemento a 2, usando 8 bits.
```

```{solution} ex-repnum-1
:class: dropdown
$19_{10} = 00010011_2$. Signo-magnitud: $10010011$. Complemento a 1 (invertir): $11101100$.
Complemento a 2 (C1 + 1): $11101101$.
```

```{exercise}
:label: ex-repnum-2
Sumá, en complemento a 2 con 8 bits, $(-45) + 30$ y verificá el resultado.
```

```{solution} ex-repnum-2
:class: dropdown
$45_{10}=00101101_2$, C2 de 45 = $11010011_2$. $30_{10}=00011110_2$.
$11010011 + 00011110 = 11110001_2$ (sin acarreo de salida en 8 bits).
Interpretando $11110001_2$ como C2: invertir y sumar 1 → $00001111_2 = 15$, con signo negativo →
$-15_{10}$, que coincide con $-45+30=-15$. Correcto.
```

```{exercise}
:label: ex-repnum-3
Con 8 bits en complemento a 2, sumá $(+100) + (+50)$. ¿Hay overflow? Justificá con la regla de los
signos.
```

```{solution} ex-repnum-3
:class: dropdown
$100_{10}=01100100_2$, $50_{10}=00110010_2$. Suma: $10010110_2$, que en C2 representa un número
negativo ($-106_{10}$). Como se sumaron dos positivos y el resultado dio negativo, **sí hay
overflow** (el resultado real, 150, no entra en el rango $[-128,127]$ de 8 bits con signo).
```

```{exercise}
:label: ex-repnum-4
Convertí $0{,}1875_{10}$ a binario en punto fijo con 4 bits fraccionarios.
```

```{solution} ex-repnum-4
:class: dropdown
$0{,}1875 \times 2 = 0{,}375\to0$; $0{,}375\times2=0{,}75\to0$; $0{,}75\times2=1{,}5\to1$;
$0{,}5\times2=1{,}0\to1$. Resultado: $0{,}0011_2$ (que efectivamente es exacto:
$2^{-3}+2^{-4}=0{,}125+0{,}0625=0{,}1875$).
```

```{exercise}
:label: ex-repnum-5
¿Cuántos números distintos se pueden representar con 4 bits en complemento a 2, y cuáles son el
máximo y el mínimo?
```

```{solution} ex-repnum-5
:class: dropdown
Con $n=4$ bits hay $2^4=16$ patrones distintos, y como hay un único cero, se representan 16 números
distintos: desde $-2^{3}=-8$ hasta $2^{3}-1=7$.
```
