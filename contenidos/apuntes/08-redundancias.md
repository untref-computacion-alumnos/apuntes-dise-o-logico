---
title: "Redundancias"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Redundancias

```{admonition} Sobre este apunte
:class: note
Este apunte desarrolla la parte de simplificación de funciones lógicas de la clase de
**Síntesis Lógica** (Prof. Dr. Martín Vázquez), centrada en los **mapas de Karnaugh**. Se
completa con bibliografía estándar de la materia {cite}`tocci2007,floyd2000` para la
mención de los métodos tabulares (Quine–McCluskey, Espresso) que exceden el alcance gráfico
de Karnaugh.
```

## 1. El problema de la redundancia

En el capítulo de [Formas canónicas](07-formas-canonicas.md) se mostró que toda función
lógica admite una expresión disyuntiva canónica (suma de minterms) y una conjuntiva canónica
(producto de maxterms). Estas expresiones tienen una ventaja enorme —se obtienen
mecánicamente a partir de la tabla de verdad, sin necesidad de razonar sobre el circuito— pero
casi nunca son la implementación más **económica**: suelen contener términos **redundantes**,
en el sentido de que parte de la información que codifican ya está contenida en otros
términos de la misma expresión.

```{important}
Simplificar una función lógica significa encontrar una expresión **equivalente** (misma
tabla de verdad) que utilice la menor cantidad posible de literales y de términos, ya que
esto se traduce directamente en menos compuertas, menos entradas por compuerta y, en
general, menor costo y menor retardo de propagación del circuito.
```

## 2. Simplificación algebraica

La primera herramienta para eliminar redundancia es el álgebra de Boole misma (ver
[Funciones de Boole](06-funciones-de-boole.md)): aplicando reiteradamente los teoremas de
idempotencia, absorción, distributividad y De Morgan es posible reducir una expresión. El
problema práctico es que este método depende de la "inspiración" para saber qué agrupar en
cada paso, no ofrece un criterio de cuándo detenerse, y se vuelve inmanejable a mano para
funciones de más de 4 o 5 variables. Los mapas de Karnaugh son, en esencia, una
**representación gráfica** que hace mecánico un caso particular —pero extremadamente
frecuente— de simplificación algebraica.

## 3. Mapas de Karnaugh

### 3.1 Fundamento

Toda la simplificación que permiten los mapas de Karnaugh se apoya en una única identidad
algebraica:

$$A \cdot B \cdot C + A \cdot B \cdot C' = A \cdot B \cdot (C + C') = A \cdot B$$

Es decir: si una variable ($C$) aparece negada en un término y sin negar en otro, y el resto
de las variables son iguales en ambos términos, esa variable puede eliminarse por completo.
Un mapa de Karnaugh es una disposición especial de las celdas de la tabla de verdad tal que
los términos que cumplen esta condición quedan **físicamente adyacentes**, y por lo tanto son
fáciles de detectar a simple vista.

### 3.2 Construcción del mapa

- Es un método manual y gráfico, útil hasta 5 o 6 variables.
- Las variables se ordenan según el **código Gray** (00, 01, 11, 10, ...), de manera que entre
  dos columnas o dos filas adyacentes cambia el valor de **una sola variable**. Esto es lo que
  garantiza que celdas adyacentes en el mapa correspondan a minterms que difieren en un único
  bit.
- El mapa también es adyacente en sus bordes: la primera y la última columna (o fila) se
  consideran adyacentes entre sí, como si el mapa estuviera dibujado sobre un cilindro (o un
  toroide, para 4 o más variables).

Mapa de Karnaugh genérico de 4 variables ($x_3 x_2 x_1 x_0$), con los índices de minterm en
cada celda:

| $x_3x_2 \backslash x_1x_0$ | 00 | 01 | 11 | 10 |
|:---:|:---:|:---:|:---:|:---:|
| **00** | 0 | 1 | 3 | 2 |
| **01** | 4 | 5 | 7 | 6 |
| **11** | 12 | 13 | 15 | 14 |
| **10** | 8 | 9 | 11 | 10 |

```{note}
Nótese que tanto las filas como las columnas están ordenadas en código Gray (00, 01, 11, 10)
y no en orden binario natural (00, 01, 10, 11). Es precisamente ese orden el que hace que
celdas vecinas —incluso entre la primera y la última columna/fila— difieran en un solo bit.
```

### 3.3 Reglas de agrupamiento

Para obtener la expresión minimizada a partir del mapa:

1. Se agrupan los 1's del mapa en rectángulos (horizontales, verticales, o que "envuelven" los
   bordes) que contengan **potencias de 2** de unos: 1, 2, 4, 8, 16, ...
2. Los grupos deben ser lo más **grandes** posible (un grupo de 8 elimina 3 variables, uno de
   4 elimina 2, uno de 2 elimina 1).
3. Cada celda con un 1 debe quedar cubierta **al menos una vez**; es válido —y habitual— que
   un mismo 1 pertenezca a más de un grupo.
4. Se seleccionan los grupos necesarios y suficientes para cubrir todos los 1's (idealmente,
   la menor cantidad de grupos, cada uno lo más grande posible).
5. Cada grupo se traduce en un término producto: se conservan solo las variables que **no
   cambian** dentro del grupo (sin negar si valen 1 en todo el grupo, negadas si valen 0).

### 3.4 Ejemplo de 3 variables

Retomemos la función $o = f(x,y,z)$ usada en los capítulos de
[Funciones lógicas](04-funciones-logicas.md) y [Formas canónicas](07-formas-canonicas.md),
con minterms en $(x,y,z) = (0,0,0),\ (0,1,1),\ (1,0,1),\ (1,1,0)$:

$$o = x'y'z' + x'yz + xy'z + xyz'$$

Mapa de Karnaugh de 3 variables:

| $x \backslash yz$ | 00 | 01 | 11 | 10 |
|:---:|:---:|:---:|:---:|:---:|
| **0** | 1 | 0 | 1 | 0 |
| **1** | 0 | 1 | 0 | 1 |

```{warning}
Este mapa queda en un patrón de "tablero de ajedrez": ningún 1 tiene un vecino que también
sea 1. No existe ningún grupo posible de tamaño 2, 4 u 8. Esto significa que **la expresión
canónica ya es la mínima**: no se puede simplificar más. No es casualidad: esta función es la
función de **paridad** de 3 variables (vale 1 cuando la cantidad de unos entre $x,y,z$ es
par), y las funciones de paridad son, junto con XOR, el ejemplo clásico de funciones que los
mapas de Karnaugh no pueden simplificar.
```

### 3.5 Ejemplo de 4 variables

Sea ahora la función de 4 variables $f(x_3,x_2,x_1,x_0)$ cuya tabla de verdad vale 1 en los
minterms $\{0,1,8,9,10,11,12,14\}$:

| $x_3x_2 \backslash x_1x_0$ | 00 | 01 | 11 | 10 |
|:---:|:---:|:---:|:---:|:---:|
| **00** | 1 | 1 | 0 | 0 |
| **01** | 0 | 0 | 0 | 0 |
| **11** | 1 | 0 | 0 | 1 |
| **10** | 1 | 1 | 1 | 1 |

Se pueden identificar tres grupos de 4 celdas (cada uno elimina 2 variables):

- **Grupo A** — fila $x_3x_2=00$ y fila $x_3x_2=10$, columnas $x_1x_0 \in \{00,01\}$: minterms
  $\{0,1,8,9\}$, todos con $x_2=0,\ x_1=0$ → término $x_2'x_1'$.
- **Grupo B** — fila $x_3x_2=10$ completa: minterms $\{8,9,11,10\}$, todos con $x_3=1,\
  x_2=0$ → término $x_3x_2'$.
- **Grupo C** — columna $x_1x_0=00$ (filas $11$ y $10$): minterms $\{12,14,8,10\}$, todos con
  $x_3=1,\ x_0=0$ → término $x_3x_0'$.

Los tres grupos comparten la celda 8, lo cual es perfectamente válido (regla 3). Sumando los
tres términos y verificando que cubren exactamente los 8 minterms de la función, se obtiene la
expresión minimizada:

$$f = x_2'x_1' + x_3x_0' + x_3x_2'$$

Esta expresión utiliza 3 términos de 2 literales cada uno (6 literales en total), frente a los
8 términos de 4 literales (32 literales) de la expresión canónica disyuntiva equivalente: una
reducción sustancial en la cantidad de compuertas y de entradas por compuerta.

## 4. Uso de valores indefinidos (*don't cares*)

En muchos diseños existen combinaciones de entrada que **nunca ocurren** en la práctica (por
ejemplo, códigos no utilizados de un teclado, o combinaciones inválidas de un código BCD —ver
[Códigos numéricos](12-codigos-numericos.md)). Para esas combinaciones, el valor de salida es
indiferente, y se anota con un guion o una $d$ en la tabla de verdad y en el mapa.

```{tip}
Los don't cares pueden tomarse como 0 **o** como 1 según convenga: se los usa para **agrandar
o completar grupos** ya existentes, nunca para crear un grupo que solo contenga don't cares
(eso no simplificaría nada, porque no cubriría ningún 1 real de la función). El criterio es
simple: "los tomo como 1 si eso me permite hacer un grupo más grande; si no ayudan, los dejo
como si fueran 0 y los ignoro".
```

Por ejemplo, si en el mapa de la sección 3.5 la celda 13 ($x_3x_2x_1x_0=1101$) fuera un don't
care en lugar de un 0, podría incorporarse al grupo B para extenderlo, o usarse para formar un
grupo adicional con la celda 15, dependiendo de qué resulte más conveniente para el resto del
mapa.

## 5. Limitaciones de Karnaugh y métodos tabulares

Los mapas de Karnaugh son un método **manual y gráfico**, y como tal tienen límites claros:

- Son prácticamente inmanejables para funciones de **más de 5 o 6 variables** (un mapa de 6
  variables ya tiene 64 celdas y adyacencias difíciles de visualizar; más allá de eso, el
  método deja de ser viable a mano).
- **No es determinístico**: distintas personas pueden agrupar los mismos 1's de maneras
  distintas y llegar a expresiones distintas (aunque equivalentes en costo, o no).
- No garantiza automáticamente encontrar el **mínimo absoluto** si no se aplican las reglas de
  cobertura con cuidado (por ejemplo, eligiendo grupos que parecen convenientes localmente pero
  dejan afuera una cobertura más económica en conjunto).

Para funciones de más variables, o para automatizar la simplificación dentro de una
herramienta de síntesis (ver [Implementación](10-implementacion.md)), se recurre a métodos
**tabulares**, que son algorítmicos y no dependen de la inspección visual:

- **Algoritmo de Quine–McCluskey** (1956): genera sistemáticamente todos los implicantes
  primos de la función mediante comparaciones tabulares de los minterms, y luego resuelve un
  problema de cobertura mínima para seleccionar el conjunto de implicantes primos que cubre
  todos los minterms con el menor costo. Es exacto (encuentra el mínimo), pero su costo
  computacional crece muy rápido con el número de variables.
- **Espresso** {cite}`tocci2007`: un minimizador **heurístico** desarrollado por Brayton et al.
  en 1984, todavía usado en herramientas de síntesis lógica actuales. Sacrifica la garantía de
  encontrar el mínimo absoluto a cambio de poder simplificar funciones de decenas de variables
  en tiempos razonables.

Ambos métodos exceden el alcance manual de este curso, pero es importante saber que existen y
que son la base de cómo las herramientas de síntesis lógica automática (mencionadas en
[Implementación](10-implementacion.md)) simplifican funciones reales de muchas variables.

## 6. Resumen

- Las expresiones canónicas (SOP/POS) casi nunca son la implementación más económica; suelen
  contener redundancia que puede eliminarse.
- La simplificación algebraica es posible pero poco sistemática; los mapas de Karnaugh
  mecanizan el caso más común de simplificación mediante una disposición en código Gray que
  hace que los términos combinables queden adyacentes.
- El procedimiento es: agrupar 1's en potencias de 2, priorizando grupos grandes, cubriendo
  todos los 1's al menos una vez.
- No todas las funciones se simplifican: las funciones de paridad/XOR son el ejemplo clásico de
  función ya mínima en su forma canónica.
- Los don't cares se aprovechan para agrandar grupos, nunca para crear grupos propios.
- Karnaugh es inviable a mano más allá de 5-6 variables; Quine–McCluskey y Espresso son los
  métodos tabulares/algorítmicos usados en esos casos y en herramientas de síntesis automática.

## 7. Ejercicios propuestos

```{exercise}
:label: ex-redun-1
Simplificar mediante mapas de Karnaugh la función de 3 variables cuyos minterms son
$\{1,2,3,7\}$.
```

```{solution} ex-redun-1
:class: dropdown
Ubicando los minterms en el mapa de 3 variables se forman dos grupos de 2: $\{2,3\}$ (con
$x=0,\ y=1$, término $x'y$) y $\{3,7\}$ (con $y=1,\ z=1$, término $yz$); el minterm 1 no tiene
vecinos con 1 salvo el 3, que ya está cubierto, así que se agrupa con él formando $\{1,3\}$
($x'z$). Una cobertura mínima válida es $f = x'y + yz + x'z$, aunque también puede
verificarse que $\{1,3\}$ y $\{2,3\}$ junto con $\{3,7\}$ cubren todo: la expresión resultante
usa 3 términos de 2 literales.
```

```{exercise}
:label: ex-redun-2
Demostrar algebraicamente, sin usar Karnaugh, que $A \cdot B \cdot C + A \cdot B \cdot C' = A
\cdot B$, justificando cada paso con un axioma o teorema del álgebra de Boole.
```

```{solution} ex-redun-2
:class: dropdown
$A B C + A B C' = AB(C+C')$ por distributividad; $C+C'=1$ por el axioma del complementario;
$AB \cdot 1 = AB$ por el axioma del elemento neutro del producto.
```

```{exercise}
:label: ex-redun-3
Repetir el ejemplo de 4 variables de la sección 3.5 suponiendo que, además, el minterm 13 es
un don't care. ¿Cambia la expresión mínima obtenida? ¿Por qué?
```

```{solution} ex-redun-3
:class: dropdown
El minterm 13 ($x_3x_2x_1x_0=1101$) es adyacente al grupo B ($\{8,9,11,10\}$, $x_3x_2'$) solo
si se extiende ese grupo a $x_1x_0 \in \{00,01,11,10\}$ con $x_2$ variable, lo cual no es
posible sin incluir también celdas en 0. En este caso particular no ayuda a formar un grupo
más grande que los ya obtenidos, así que la expresión mínima no cambia: sigue siendo
$f = x_2'x_1' + x_3x_0' + x_3x_2'$. El ejercicio ilustra que no todo don't care resulta útil.
```

```{exercise}
:label: ex-redun-4
Investigar (bibliografía sugerida) en qué se diferencia un implicante primo de un implicante
primo **esencial**, y explicar por qué el algoritmo de Quine–McCluskey necesita distinguir
ambos conceptos para resolver el problema de cobertura mínima.
```

```{solution} ex-redun-4
:class: dropdown
Un implicante primo es un término producto que no puede agrandarse (eliminar otra variable)
sin dejar de ser un subconjunto de la función. Un implicante primo es además **esencial** si
existe al menos un minterm que solo él cubre (ningún otro implicante primo lo cubre). Los
esenciales deben incluirse obligatoriamente en cualquier cobertura mínima; el resto de los
minterms (no cubiertos por ningún esencial) requieren resolver un problema de cobertura de
conjuntos para elegir, entre los implicantes primos no esenciales restantes, el subconjunto
más económico que los cubra. Ver {cite}`tocci2007` para el desarrollo completo del algoritmo.
```

## 8. Bibliografía

```{bibliography}
:filter: docname in docnames
```
