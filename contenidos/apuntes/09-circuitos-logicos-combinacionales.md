---
title: "Circuitos Lógicos Combinacionales"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Circuitos Lógicos Combinacionales

```{admonition} Sobre este apunte
:class: note
La definición de circuito combinacional que abre este apunte está tomada textualmente de la
clase de **Circuitos Secuenciales I** (Prof. Dr. Martín Vázquez), donde se la introduce por
oposición a los circuitos secuenciales. El resto del capítulo —metodología de diseño,
circuitos de dos niveles vs. multinivel, retardo de propagación y riesgos— se completa con
bibliografía estándar de la materia {cite}`tocci2007,harris2012`.
```

## 1. Definición

En palabras del profesor: "hasta aquí en el curso estudiamos circuitos combinacionales".

```{admonition} Circuito combinacional
:class: important
Un **circuito combinacional** es aquel cuyas salidas dependen **exclusivamente** de la
combinación de sus entradas en el instante presente. Ante la misma combinación de las mismas
entradas, el circuito siempre se estabiliza con las mismas salidas.
```

Formalmente, si $I=(i_1,\dots,i_n)$ es el vector de entradas y $O=(o_1,\dots,o_m)$ el de
salidas, un circuito combinacional implementa una función

$$O = f(I)$$

sin ningún tipo de realimentación interna ni elemento de memoria: el circuito no "recuerda"
nada de su historia pasada. Todos los bloques vistos hasta ahora en este apunte —compuertas
([Compuertas lógicas](05-compuertas-logicas.md)), y las formas canónicas que los generan
([Formas canónicas](07-formas-canonicas.md))— son combinacionales.

```{note}
Esto se contrapone a los **circuitos secuenciales**, en los que la salida depende tanto de las
entradas actuales como del **estado interno** del circuito (es decir, poseen memoria). Los
circuitos secuenciales se desarrollan en detalle en
[Circuitos secuenciales asincrónicos y sincrónicos](17-circuitos-secuenciales-asincronicos-y-sincronicos.md).
Por ahora alcanza con tener clara la distinción: en un circuito combinacional nunca hace falta
preguntar "¿en qué estado estaba antes?" para saber cuál va a ser la salida.
```

## 2. Metodología de diseño

El diseño de un circuito combinacional a partir de una especificación en palabras sigue,
típicamente, el siguiente flujo, que resume buena parte de los capítulos anteriores de este
apunte:

```{mermaid}
flowchart TD
    A[Especificación en palabras] --> B[Tabla de verdad]
    B --> C["Ecuación canónica (SOP/POS)"]
    C --> D["Simplificación (Karnaugh, algebraica)"]
    D --> E["Implementación con compuertas u otras técnicas"]
```

1. **Especificación**: se traduce el problema (por ejemplo, "una alarma que suena si la puerta
   está abierta y el sistema está armado") en variables de entrada y salida bien definidas.
2. **Tabla de verdad**: se enumeran todas las combinaciones posibles de entrada y se determina
   la salida correspondiente para cada una (ver [Funciones lógicas](04-funciones-logicas.md)).
3. **Ecuación booleana canónica**: se obtiene la forma disyuntiva o conjuntiva canónica
   directamente de la tabla de verdad (ver [Formas canónicas](07-formas-canonicas.md)).
4. **Simplificación**: se elimina la redundancia de la expresión canónica mediante álgebra de
   Boole o mapas de Karnaugh (ver [Redundancias](08-redundancias.md)).
5. **Implementación**: se traduce la expresión simplificada a un circuito físico, ya sea con
   compuertas discretas, multiplexores, PLA, ROM u otra tecnología (ver
   [Implementación](10-implementacion.md)).

Este mismo flujo es el que se usa, más adelante, para diseñar los bloques combinacionales de
uso frecuente que se estudian en los próximos capítulos: decodificadores y codificadores
([Codificadores y decodificadores](14-codificadores-y-decodificadores.md)), multiplexores y
demultiplexores ([Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md)) y
sumadores, restadores y comparadores
([Sumadores, restadores y comparadores](16-sumadores-restadores-y-comparadores.md)).

## 3. Circuitos de dos niveles y circuitos multinivel

Las formas canónicas SOP y POS dan lugar, naturalmente, a circuitos de **dos niveles**: un
primer nivel de compuertas AND (u OR) y un segundo nivel con una única compuerta OR (o AND) que
combina las salidas del primer nivel. Este es el estilo de implementación que se vio en
[Formas canónicas](07-formas-canonicas.md).

Una alternativa es permitir **más de dos niveles** de compuertas, mezclando AND, OR y NOT (o
directamente NAND/NOR) en cadenas más profundas, generalmente obtenidas por factoreo algebraico
de la expresión simplificada.

| Aspecto | Dos niveles (AND-OR / OR-AND) | Multinivel |
|---|---|---|
| Retardo de propagación | Mínimo y predecible (2 niveles de compuerta) | Mayor, depende de la profundidad de la red |
| Cantidad de compuertas | Puede ser mayor (compuertas con muchas entradas) | Generalmente menor (se reutilizan subexpresiones) |
| Entradas por compuerta | Puede requerir compuertas de muchas entradas, poco prácticas físicamente | Compuertas de pocas entradas, más realistas |
| Facilidad de diseño | Directa a partir de la tabla de verdad | Requiere factoreo/manipulación algebraica adicional |

```{tip}
En la práctica ninguna de las dos familias es "mejor" en abstracto: el diseño de dos niveles
prioriza **velocidad** (menos niveles de compuerta implica menos retardo acumulado), mientras
que el multinivel prioriza **costo/área**, a costa de mayor retardo. La elección depende de los
requisitos del sistema {cite}`tocci2007`.
```

## 4. Retardo de propagación y camino crítico

Cada compuerta física introduce un pequeño retardo entre el instante en que cambian sus
entradas y el instante en que su salida refleja ese cambio: el **retardo de propagación**
($t_{pd}$). Ya se usó esta idea de manera informal en este apunte al calcular, por ejemplo, el
tiempo de un multiplexor jerárquico como $T_{MUX2\_1} = T_{AND}+T_{OR}$ (ver
[Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md)).

En un circuito de varios niveles, el retardo total desde que cambia una entrada hasta que se
estabiliza la salida es la suma de los retardos de las compuertas atravesadas por el
**camino más largo** entre esa entrada y esa salida: el llamado **camino crítico**. El camino
crítico determina la máxima velocidad de operación del circuito, y es uno de los criterios
centrales al comparar dos implementaciones (por ejemplo, dos niveles vs. multinivel, o las
distintas técnicas de síntesis de [Implementación](10-implementacion.md)).

## 5. Riesgos (*hazards*)

Un **riesgo** o *hazard* es un cambio momentáneo y no deseado en la salida de un circuito
combinacional, producido durante una transición de entrada, aun cuando la salida final
—una vez estabilizado el circuito— sea la correcta. Se origina porque distintas trayectorias
dentro del circuito pueden tener retardos de propagación distintos, de modo que la salida
puede pasar transitoriamente por un valor incorrecto antes de asentarse en el valor esperado.

```{note}
El estudio detallado de los riesgos (estáticos, dinámicos, cómo detectarlos en un mapa de
Karnaugh y cómo eliminarlos agregando términos redundantes a propósito) es un tema avanzado de
diseño digital que excede el alcance de este curso introductorio; se menciona aquí porque es
la razón principal por la cual, en ciertos casos, se agregan deliberadamente términos que
parecen "redundantes" según el criterio del capítulo de
[Redundancias](08-redundancias.md). Ver {cite}`tocci2007,harris2012` para un desarrollo
completo.
```

## 6. Resumen

- Un circuito combinacional es aquel cuya salida depende únicamente de la combinación actual de
  entradas, sin memoria ni realimentación: $O=f(I)$.
- El diseño sigue un flujo estándar: especificación → tabla de verdad → ecuación canónica →
  simplificación → implementación.
- Los circuitos de dos niveles (AND-OR/OR-AND) priorizan velocidad; los multinivel priorizan
  costo/área, a costa de mayor retardo.
- El retardo de propagación de cada compuerta se acumula a lo largo del camino crítico, que
  determina la velocidad máxima del circuito.
- Los riesgos (*hazards*) son cambios transitorios no deseados en la salida durante una
  transición de entrada, causados por diferencias de retardo entre trayectorias.

## 7. Ejercicios propuestos

```{exercise}
:label: ex-comb-1
Explicar, con un ejemplo propio, por qué un sumador de 1 bit (ver
[Sumadores, restadores y comparadores](16-sumadores-restadores-y-comparadores.md)) es un
circuito combinacional y no uno secuencial.
```

```{solution} ex-comb-1
:class: dropdown
Un sumador de 1 bit calcula su suma y su acarreo de salida únicamente a partir de sus dos bits
de entrada y el acarreo de entrada del instante actual; ante la misma terna de entradas,
siempre entrega la misma salida, sin depender de sumas anteriores. No hay ningún elemento que
almacene información entre una operación y la siguiente, por lo tanto es combinacional.
```

```{exercise}
:label: ex-comb-2
Dado un circuito de dos niveles AND-OR con compuertas AND de 4 entradas ($t_{AND}=3\,ns$) y una
compuerta OR de salida ($t_{OR}=2\,ns$), calcular el retardo de propagación total del camino
crítico.
```

```{solution} ex-comb-2
:class: dropdown
El camino crítico atraviesa una compuerta AND y luego la compuerta OR: $t_{pd} = t_{AND} +
t_{OR} = 3\,ns + 2\,ns = 5\,ns$.
```

```{exercise}
:label: ex-comb-3
¿Por qué, en general, un circuito multinivel tiene mayor retardo de propagación que su
equivalente de dos niveles, aun usando menos compuertas en total?
```

```{solution} ex-comb-3
:class: dropdown
Porque el retardo depende de la **profundidad** del camino más largo (cantidad de niveles
atravesados), no de la cantidad total de compuertas. Un circuito multinivel factoriza la
expresión reutilizando subexpresiones en cascada, lo que reduce el número de compuertas pero
aumenta la cantidad de niveles que debe atravesar la señal en el peor caso.
```

## 8. Bibliografía

```{bibliography}
:filter: docname in docnames
```
