---
title: "Códigos Alfanuméricos"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Códigos Alfanuméricos

```{admonition} Sobre este apunte
:class: note
Este capítulo no proviene de manera directa de las presentaciones de la cátedra: desarrolla,
a partir de bibliografía estándar de Diseño Lógico y de arquitectura de computadoras
({cite}`tocci2007`, {cite}`harris2012`), los códigos usados para representar texto (letras,
dígitos, signos de puntuación, caracteres de control) en sistemas digitales, aplicando los
conceptos generales de [Códigos binarios](11-codigos-binarios.md).
```

## 1. La necesidad de codificar texto

Los códigos numéricos del capítulo anterior alcanzan para representar cantidades, pero un
sistema digital también necesita intercambiar **texto**: letras mayúsculas y minúsculas,
dígitos como caracteres (no como cantidades), signos de puntuación, y **caracteres de
control** que no se imprimen pero cumplen una función (por ejemplo, salto de línea o fin de
transmisión). Un **código alfanumérico** asigna una palabra de bits a cada uno de estos
símbolos.

## 2. ASCII

El código **ASCII** (American Standard Code for Information Interchange, 1963) es el código
alfanumérico más influyente de la historia de la informática. Su versión original usa **7
bits** por carácter, es decir $2^7=128$ combinaciones posibles, suficientes para el alfabeto
inglés (mayúsculas y minúsculas), los 10 dígitos, signos de puntuación y un conjunto de
caracteres de control heredados de la telegrafía y las primeras terminales.

### 2.1 Estructura de la tabla ASCII

La tabla completa tiene 128 entradas; a modo de ejemplo:

| Carácter | Código binario (7 bits) | Decimal | Hexadecimal |
|:---:|:---:|:---:|:---:|
| NUL (nulo) | 0000000 | 0 | 00 |
| LF (salto de línea) | 0001010 | 10 | 0A |
| CR (retorno de carro) | 0001101 | 13 | 0D |
| Espacio | 0100000 | 32 | 20 |
| '0' | 0110000 | 48 | 30 |
| '9' | 0111001 | 57 | 39 |
| 'A' | 1000001 | 65 | 41 |
| 'Z' | 1011010 | 90 | 5A |
| 'a' | 1100001 | 97 | 61 |
| 'z' | 1111010 | 122 | 7A |

```{tip}
Una propiedad muy usada en programación: los dígitos '0'-'9' son consecutivos en la tabla
($0x30$ a $0x39$), igual que 'A'-'Z' ($0x41$ a $0x5A$) y 'a'-'z' ($0x61$ a $0x7A$). Esto permite,
por ejemplo, convertir un dígito ASCII a su valor numérico simplemente restando $0x30$, o pasar
de mayúscula a minúscula sumando $0x20$ (equivalente a poner en 1 el bit de posición 5).
```

### 2.2 ASCII extendido

Al trabajar con bytes de 8 bits (en lugar de 7), queda un bit libre que permite definir 128
combinaciones adicionales ($128$ a $255$): el llamado **ASCII extendido**. A diferencia del
ASCII original (estándar universal), existieron múltiples variantes de tabla extendida según el
fabricante o la página de códigos (por ejemplo, para incluir letras acentuadas y la letra "ñ"
del español), lo que generaba incompatibilidades al intercambiar texto entre sistemas distintos.

## 3. EBCDIC (mención histórica)

**EBCDIC** (Extended Binary Coded Decimal Interchange Code) es un código alfanumérico de 8 bits
desarrollado por IBM en la década de 1960 para sus computadoras centrales (mainframes),
anterior y en paralelo a la difusión de ASCII. A diferencia de ASCII, sus dígitos y letras no
están ordenados de forma estrictamente consecutiva en la tabla, lo que dificultaba ciertas
operaciones. Con el tiempo, ASCII (y sus sucesores) se impuso como estándar de facto en la
mayoría de los sistemas, y EBCDIC quedó relegado a sistemas heredados de IBM.

## 4. Unicode y UTF-8 (evolución moderna)

ASCII (128 símbolos) y sus extensiones (256 símbolos) resultan insuficientes para representar
todos los alfabetos y símbolos usados en el mundo (cirílico, árabe, chino, símbolos matemáticos,
emojis, etc.). **Unicode** es un estándar que asigna un número único (**punto de código**) a
prácticamente cualquier carácter de cualquier sistema de escritura, con más de un millón de
puntos de código posibles.

Unicode no define una única codificación en bits, sino varias; la más usada en la actualidad es
**UTF-8**, que:

- Es **compatible hacia atrás con ASCII**: los primeros 128 puntos de código de Unicode
  coinciden exactamente con la tabla ASCII, y se codifican en UTF-8 con un solo byte idéntico al
  ASCII original.
- Usa una cantidad **variable** de bytes (de 1 a 4) por carácter, según el punto de código:
  caracteres poco frecuentes (fuera del rango básico) ocupan más bytes, lo que hace que UTF-8
  sea eficiente para texto mayormente en inglés y a la vez universal.

```{note}
Esta sección es una referencia de cultura técnica general; el desarrollo detallado de esquemas
de codificación de longitud variable como UTF-8 corresponde a cursos de organización de
computadoras o de comunicaciones de datos, no al núcleo de Diseño Lógico.
```

## 5. Detección de errores en caracteres: repaso del bit de paridad

Al transmitir caracteres ASCII de 7 bits por un canal serie, es habitual agregar un **octavo bit
de paridad** (ver [Códigos binarios](11-codigos-binarios.md), sección 4) para detectar errores
de transmisión de un bit.

**Ejemplo:** transmitir la letra 'A' (`1000001`, tres unos) con paridad par:

- Como la cantidad de unos ya es impar (tres), se agrega un bit de paridad $p=1$ para llegar a
  una cantidad par de unos → byte transmitido: `11000001`.

Si en la recepción la cantidad de unos del byte completo resulta impar, se sabe que ocurrió un
error de transmisión en un número impar de bits.

## 6. Resumen

- Un código alfanumérico asigna palabras de bits a letras, dígitos (como caracteres),
  puntuación y caracteres de control.
- **ASCII** (7 bits, 128 combinaciones) es el código alfanumérico histórico y más difundido; sus
  rangos de dígitos y letras son consecutivos, lo que facilita ciertas operaciones aritméticas
  sobre caracteres.
- El **ASCII extendido** (8 bits) agrega 128 combinaciones, con variantes no estandarizadas
  entre fabricantes.
- **EBCDIC** es el código alfanumérico histórico de IBM, hoy limitado a sistemas heredados.
- **Unicode/UTF-8** extiende la idea de ASCII para representar todos los alfabetos del mundo,
  manteniendo compatibilidad con ASCII para los primeros 128 caracteres.
- El **bit de paridad** (capítulo 11) se aplica igual sobre caracteres codificados que sobre
  cualquier otra palabra binaria.

## 7. Ejercicios propuestos

```{exercise}
:label: ex-codalfa-1
Indicar el código ASCII en binario y en hexadecimal de la letra 'M', sabiendo que 'A' es
`1000001` (0x41) y que las letras mayúsculas son consecutivas en la tabla.
```

```{solution} ex-codalfa-1
:class: dropdown
'M' es la 13ª letra del alfabeto (A=1ª). Su código es el de 'A' más 12: $0x41+12=0x4D$, es
decir $1001101$ en binario (77 en decimal).
```

```{exercise}
:label: ex-codalfa-2
Convertir el carácter ASCII '7' (0x37) a su valor numérico entero usando la propiedad de
consecutividad de los dígitos en la tabla.
```

```{solution} ex-codalfa-2
:class: dropdown
Restando $0x30$ (código de '0'): $0x37 - 0x30 = 0x07 = 7$. El resultado es el entero 7.
```

```{exercise}
:label: ex-codalfa-3
Calcular el bit de paridad impar para el carácter ASCII '5' (`0110101`, cuatro unos) y dar el
byte completo transmitido.
```

```{solution} ex-codalfa-3
:class: dropdown
Como ya hay una cantidad par de unos (cuatro), para paridad impar se agrega $p=1$: byte
transmitido `10110101`.
```

## 8. Bibliografía

```{bibliography}
:filter: docname in docnames
```
