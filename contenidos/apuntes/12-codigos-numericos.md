---
title: "Códigos Numéricos"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Códigos Numéricos

```{admonition} Sobre este apunte
:class: note
Este capítulo no proviene de manera directa de las presentaciones de la cátedra: desarrolla,
a partir de bibliografía estándar de Diseño Lógico ({cite}`tocci2007`, {cite}`floyd2000`,
{cite}`mandado1998`), los códigos numéricos más utilizados para representar dígitos decimales
en sistemas digitales, aplicando los conceptos generales de [Códigos binarios](11-codigos-binarios.md).
```

## 1. BCD (Binary Coded Decimal)

El código **BCD** (decimal codificado en binario) representa **cada dígito decimal por
separado** usando su equivalente en binario natural de 4 bits, en lugar de convertir el número
completo a binario. Es un código **ponderado** con pesos $8,4,2,1$ (por eso también se lo llama
BCD 8421).

| Dígito decimal | BCD (8-4-2-1) |
|:---:|:---:|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |

```{important}
Con 4 bits hay $2^4=16$ combinaciones posibles, pero BCD solo usa 10 (0000 a 1001). Las
combinaciones $1010$ a $1111$ se consideran **no usadas** (inválidas) en BCD puro: no
representan ningún dígito decimal válido. Esto es distinto del binario natural, donde las 16
combinaciones de 4 bits sí tienen significado (representan del 0 al 15).
```

### 1.1 Conversión decimal ↔ BCD

Para convertir un número decimal de varios dígitos a BCD, se codifica **cada dígito por
separado** con su grupo de 4 bits:

$$529_{10} = \underbrace{0101}_{5}\ \underbrace{0010}_{2}\ \underbrace{1001}_{9} \;\text{(BCD)}$$

Nótese que $529_{10}$ en binario natural sería $1000010001_2$ (10 bits), mientras que en BCD
ocupa 12 bits (4 por dígito): BCD es menos eficiente en cantidad de bits, pero mucho más simple
de convertir hacia y desde la representación decimal que usan las personas (displays,
teclados, etc.), lo cual es su principal ventaja práctica.

### 1.2 Aritmética en BCD (nota)

```{note}
Sumar dos números en BCD dígito a dígito con un sumador binario común puede dar un resultado
mayor a 9 en algún dígito (por ejemplo, $7+8=15$), que cae en una combinación no usada de BCD.
La corrección estándar es: si el resultado parcial de 4 bits supera 9, o si se generó acarreo
desde ese dígito, se le **suma 6 ($0110$)** para "saltar" las seis combinaciones no usadas y
volver a caer en el rango BCD válido, propagando el acarreo al dígito siguiente.
```

## 2. Otros códigos BCD ponderados

Además del BCD natural (8-4-2-1), existen otros códigos que también asignan 4 bits por dígito
decimal, pero con distintos pesos:

### 2.1 Código Aiken (2421)

Usa los pesos $2,4,2,1$. Es un código ponderado en el que más de una combinación de bits puede
sumar el mismo valor decimal (por ejemplo, con pesos 2421, tanto $0011$ como $1001$ podrían
sumar 3 según cómo se resuelva la ambigüedad); por convención se elige una única asignación por
dígito.

| Dígito | Aiken (2421) |
|:---:|:---:|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 1011 |
| 6 | 1100 |
| 7 | 1101 |
| 8 | 1110 |
| 9 | 1111 |

```{tip}
El código Aiken es **autocomplementario a 9**: el código del dígito $9-d$ se obtiene invirtiendo
(complementando) todos los bits del código de $d$. Por ejemplo, $2 = 0010$ y $9-2=7$ se
codifica como $1101$, que es exactamente el complemento bit a bit de $0010$. Esta propiedad
simplifica el cálculo del complemento a 9, útil en aritmética decimal por complemento.
```

### 2.2 Código exceso-3 (Excess-3)

Se obtiene sumando 3 (0011) al BCD natural de cada dígito. También es **autocomplementario a
9**, y su principal ventaja histórica fue simplificar ciertas operaciones aritméticas en
hardware decimal.

| Dígito | BCD natural | Exceso-3 |
|:---:|:---:|:---:|
| 0 | 0000 | 0011 |
| 1 | 0001 | 0100 |
| 2 | 0010 | 0101 |
| 3 | 0011 | 0110 |
| 4 | 0100 | 0111 |
| 5 | 0101 | 1000 |
| 6 | 0110 | 1001 |
| 7 | 0111 | 1010 |
| 8 | 1000 | 1011 |
| 9 | 1001 | 1100 |

## 3. Código Gray (código reflejado)

El **código Gray** es el código no ponderado más importante del curso: se construye de manera
que **entre dos valores consecutivos cambia un único bit**. Por eso se lo llama también código
de "distancia unitaria" o código reflejado (cada mitad de la tabla es un espejo de la otra con
el bit más significativo agregado).

| Decimal | Binario natural | Gray |
|:---:|:---:|:---:|
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| 9 | 1001 | 1101 |
| 10 | 1010 | 1111 |
| 11 | 1011 | 1110 |
| 12 | 1100 | 1010 |
| 13 | 1101 | 1011 |
| 14 | 1110 | 1001 |
| 15 | 1111 | 1000 |

```{note}
Este es exactamente el mismo criterio de ordenamiento (código Gray) que se usa para etiquetar
las filas y columnas de un mapa de Karnaugh, de manera que celdas físicamente adyacentes en el
mapa difieran en un solo bit. Ver [Redundancias](08-redundancias.md).
```

### 3.1 Conversión binario → Gray

Dado un número binario $b_{n-1}b_{n-2}\dots b_1 b_0$, el código Gray $g_{n-1}g_{n-2}\dots g_0$
se obtiene como:

$$g_{n-1} = b_{n-1} \qquad g_i = b_{i+1} \oplus b_i \;\; (0 \leq i < n-1)$$

Es decir, el bit más significativo se copia igual, y cada bit siguiente es el XOR entre el bit
binario correspondiente y el bit binario inmediatamente más significativo.

**Ejemplo:** convertir $1011_2$ a Gray.

$$g_3=b_3=1 \qquad g_2=b_3 \oplus b_2 = 1\oplus 0=1 \qquad g_1=b_2\oplus b_1=0\oplus 1=1 \qquad g_0=b_1\oplus b_0=1\oplus 1=0$$

Resultado: $1110$ (coincide con la fila 11 de la tabla).

### 3.2 Conversión Gray → binario

La conversión inversa se hace de manera acumulativa:

$$b_{n-1} = g_{n-1} \qquad b_i = b_{i+1} \oplus g_i \;\; (0 \leq i < n-1)$$

Cada bit binario se calcula como el XOR entre el bit binario ya calculado (posición
inmediatamente más significativa) y el bit Gray correspondiente.

### 3.3 Aplicaciones del código Gray

- **Codificadores de posición (encoders) mecánicos y ópticos:** cuando un disco codificado gira
  y se lee con sensores, un error de lectura simultánea de dos o más bits (por desalineación
  momentánea) en binario natural puede producir un salto grande e incorrecto en el valor leído
  (por ejemplo, de $0111$ a $1000$, cuatro bits cambian a la vez). En Gray, como solo cambia un
  bit entre posiciones consecutivas, el error máximo posible ante una lectura desalineada es de
  una unidad.
- **Mapas de Karnaugh:** el ordenamiento de filas/columnas en código Gray garantiza que celdas
  adyacentes en el mapa difieran en una sola variable, lo cual es la base del método de
  simplificación (ver [Redundancias](08-redundancias.md)).
- **Contadores Gray:** en diseños donde importa minimizar el consumo o los picos de conmutación
  simultánea de muchos bits, se usan contadores que recorren la secuencia Gray en lugar de la
  secuencia binaria natural.

## 4. Resumen

- **BCD** codifica cada dígito decimal por separado con 4 bits (pesos 8-4-2-1); es ponderado,
  fácil de convertir hacia/desde decimal, pero usa solo 10 de las 16 combinaciones de 4 bits.
- **Aiken (2421)** y **exceso-3** son códigos BCD alternativos, ambos **autocomplementarios a
  9**, útiles para simplificar la aritmética decimal en hardware.
- El **código Gray** es no ponderado y de distancia unitaria: cambia un solo bit entre valores
  consecutivos. Se convierte desde/hacia binario natural con operaciones XOR encadenadas.
- Gray se usa en codificadores de posición físicos y es la base del ordenamiento de los mapas de
  Karnaugh.

## 5. Ejercicios propuestos

```{exercise}
:label: ex-codnum-1
Codificar el número $307_{10}$ en BCD natural.
```

```{solution} ex-codnum-1
:class: dropdown
Cada dígito por separado: $3=0011$, $0=0000$, $7=0111$. Resultado: $0011\ 0000\ 0111$.
```

```{exercise}
:label: ex-codnum-2
Codificar el dígito 6 en exceso-3 y verificar la propiedad de autocomplemento a 9 comparándolo
con el código de 3.
```

```{solution} ex-codnum-2
:class: dropdown
$6$ en exceso-3 es $1001$. $3$ en exceso-3 es $0110$. Efectivamente, $1001$ es el complemento
bit a bit de $0110$, verificando que $6+3=9$ y que el código es autocomplementario.
```

```{exercise}
:label: ex-codnum-3
Convertir el número binario $10110_2$ a código Gray.
```

```{solution} ex-codnum-3
:class: dropdown
$g_4=b_4=1$; $g_3=b_4\oplus b_3=1\oplus0=1$; $g_2=b_3\oplus b_2=0\oplus1=1$;
$g_1=b_2\oplus b_1=1\oplus1=0$; $g_0=b_1\oplus b_0=1\oplus0=1$. Resultado: $11101$.
```

```{exercise}
:label: ex-codnum-4
Convertir el código Gray $1101$ a binario natural.
```

```{solution} ex-codnum-4
:class: dropdown
$b_3=g_3=1$; $b_2=b_3\oplus g_2=1\oplus1=0$; $b_1=b_2\oplus g_1=0\oplus0=0$;
$b_0=b_1\oplus g_0=0\oplus1=1$. Resultado: $1001$ (decimal 9), que coincide con la fila 9 de la
tabla de la sección 3.
```

## 6. Bibliografía

```{bibliography}
:filter: docname in docnames
```
