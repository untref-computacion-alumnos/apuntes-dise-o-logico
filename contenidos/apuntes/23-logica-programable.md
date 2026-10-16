---
title: "Lógica Programable"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Lógica Programable

```{admonition} Sobre este apunte
:class: note
Este capítulo retoma el contexto de "Materialización de Sistemas Digitales" de la presentación
**"Diseño de Sistemas Digitales"** (Prof. Dr. Martín Vázquez) — en particular la distinción entre
ASIC y dispositivos programables por el usuario, y el ejemplo de bloque configurable de FPGA (LUT-6
de Xilinx) ya desarrollado en detalle en [Implementación](10-implementacion.md), al que este
capítulo remite en vez de repetir. El resto —la taxonomía PROM/PLA/PAL/GAL/CPLD/FPGA y la
comparación ASIC vs. programable— se completa con bibliografía estándar de la materia
({cite}`tocci2007`, {cite}`harris2012`, {cite}`mandado1998`, {cite}`balch2003`,
{cite}`deschamps1989`).
```

## 1. Qué es la lógica programable

Un **ASIC** (*Application Specific Integrated Circuit*) es un circuito integrado cuya función queda
**fija en el momento de fabricarse**: cambiar su comportamiento implica fabricar una nueva pastilla.
La **lógica programable**, en cambio, agrupa a los dispositivos cuyo comportamiento interno se
**define después de fabricados**, mediante un proceso de programación o configuración que realiza el
propio usuario/diseñador (ver la comparación de niveles de conocimiento necesarios —electrónica vs.
diseño lógico— ya discutida en [Implementación](10-implementacion.md), sección de materialización de
sistemas digitales).

```{important}
La lógica programable no reemplaza al ASIC: son puntos distintos de una misma decisión de
ingeniería, que se desarrolla en la sección 7 de este capítulo (costo de ingeniería no recurrente
vs. volumen de producción).
```

## 2. Taxonomía por planos AND/OR fijos o programables

Los primeros dispositivos de lógica programable combinacional se clasifican según **cuál de los dos
planos** de una estructura AND-OR (ver [Formas canónicas](07-formas-canonicas.md) y la síntesis por
PLA/ROM de [Implementación](10-implementacion.md)) es fijo y cuál es programable:

| Dispositivo | Plano AND | Plano OR | Comentario |
|---|:---:|:---:|---|
| **PROM** | Fijo (actúa como decodificador) | Programable | Ya desarrollado como técnica de síntesis en el capítulo 10 — cada palabra de la memoria es, en esencia, un minterm. |
| **PLA** (*Programmable Logic Array*) | Programable | Programable | La más flexible de las tres; también desarrollada en el capítulo 10. |
| **PAL** (*Programmable Array Logic*) | Programable | **Fijo** | Cada salida es la OR de un número fijo y pequeño de términos producto programables — más simple y más rápida de fabricar/programar que una PLA completa. |

```{note}
No repetimos acá los ejemplos de programación bit a bit de PROM/PLA ya vistos en
[Implementación](10-implementacion.md); esta sección se enfoca en la taxonomía de dispositivos como
tales, no en la técnica de síntesis.
```

La **GAL** (*Generic Array Logic*) es, conceptualmente, una PAL cuyas conexiones se programan
**eléctricamente** y pueden **borrarse y reprogramarse** (a diferencia de la PAL clásica, programada
una sola vez mediante fusibles). Es el análogo, en lógica combinacional programable, de lo que la
EEPROM es respecto de la PROM (ver [Memoria](21-memoria.md)).

## 3. CPLD (Complex Programmable Logic Device)

Un **CPLD** agrupa **varios bloques tipo PAL/GAL** dentro de un mismo chip, interconectados entre sí
mediante una **matriz de interconexión programable**. Cada bloque conserva la estructura simple de
una PAL (rápida y predecible en tiempos), pero la posibilidad de interconectar varios bloques permite
implementar diseños bastante más grandes que los de una única PAL. Los CPLD son dispositivos **no
volátiles**: retienen su configuración al apagarse, sin necesidad de recargarla al encender.

## 4. FPGA (Field-Programmable Gate Array)

Una **FPGA** lleva la idea de la lógica programable a una escala mucho mayor. Su arquitectura se
organiza, típicamente, en:

- **Bloques lógicos configurables** (*CLB*, *Configurable Logic Block*), cada uno con una o más
  **LUT** (*Look-Up Table*) — memorias pequeñas que implementan cualquier función booleana de sus
  entradas por consulta directa de tabla, junto con uno o más flip-flops. El ejemplo concreto de un
  slice de CLB con LUT-6 de Xilinx (capaz de implementar funciones de hasta 8 variables combinando
  varias LUT) ya se desarrolló en [Implementación](10-implementacion.md), sección de síntesis
  ROM+MUX/FPGA — no se repite acá.
- Una **matriz de interconexión programable**, que conecta los CLB entre sí y con los bloques de
  entrada/salida, según lo que indique el archivo de configuración.
- **Bloques de entrada/salida** (*IOB*, *I/O Block*), que adaptan las señales externas a los niveles
  y estándares eléctricos usados dentro del chip.
- Opcionalmente, bloques **dedicados**: memoria embebida (*BRAM*, ver [Memoria](21-memoria.md)) y
  multiplicadores/DSP, que evitan tener que construir esas funciones con LUTs genéricas.

```{note}
La mayoría de las FPGA comerciales son **volátiles**: se basan en celdas de configuración tipo SRAM
(ver [Memoria](21-memoria.md)), por lo que **pierden su configuración al apagarse** y deben
recargarla desde una memoria no volátil externa (o interna) cada vez que se energizan. Existen
alternativas basadas en tecnología *antifuse*, no volátiles pero programables una sola vez, usadas
sobre todo en aplicaciones espaciales/militares donde la resistencia a la radiación es crítica.
```

## 5. Comparación PAL/CPLD vs. FPGA

| Característica | PAL / CPLD | FPGA |
|---|---|---|
| Densidad lógica | Baja a media | Media a muy alta (millones de compuertas equivalentes) |
| Volatilidad | No volátil | Típicamente volátil (SRAM); requiere recarga de configuración |
| Predictibilidad de tiempos | Alta (estructura simple, pocos niveles) | Menor y más dependiente del *place & route* |
| Costo por unidad (bajo volumen) | Bajo | Medio a alto |
| Flexibilidad / tamaño de diseño | Diseños chicos (lógica de control, decodificación) | Diseños grandes (procesadores, DSP, sistemas completos) |

## 6. Flujo de diseño sobre lógica programable

El camino típico desde una descripción de alto nivel hasta un dispositivo programable configurado
es:

```{mermaid}
flowchart LR
    A["Descripción en HDL (VHDL)"] --> B["Síntesis lógica"]
    B --> C["Mapeo tecnológico"]
    C --> D["Place & Route"]
    D --> E["Generación del bitstream"]
    E --> F["Programación del dispositivo"]
```

1. **Descripción en HDL**: el diseño se describe en VHDL (ver
   [Lenguajes de programación HDL](22-lenguajes-de-programacion-hdl.md)), típicamente en nivel RTL.
2. **Síntesis lógica**: se traduce la descripción RTL a una red de compuertas/LUTs, aplicando las
   técnicas vistas en [Implementación](10-implementacion.md).
3. **Mapeo tecnológico**: esa red se adapta a los recursos concretos del dispositivo elegido (LUTs
   de tamaño fijo, bloques PAL, etc.).
4. **Place & route**: se decide la ubicación física de cada bloque dentro del chip y cómo se
   conectan usando la matriz de interconexión programable.
5. **Generación del bitstream**: se produce el archivo binario de configuración.
6. **Programación**: el bitstream se descarga al dispositivo (o a una memoria no volátil que lo
   carga en él al encender).

## 7. ASIC vs. dispositivos programables: el trade-off de fondo

La decisión entre un ASIC y un dispositivo programable (PAL/CPLD/FPGA) es, en el fondo, un
trade-off económico y de tiempos de desarrollo {cite}`harris2012`:

- **Costo de ingeniería no recurrente (NRE)**: diseñar y fabricar máscaras para un ASIC tiene un
  costo inicial muy alto, independiente de cuántas unidades se produzcan después. Un dispositivo
  programable no tiene ese costo de fabricación por diseño: se compra "en blanco" y se programa.
- **Costo por unidad a gran volumen**: repartido entre millones de unidades, el costo de diseño de
  un ASIC se diluye y termina siendo más barato por chip que un dispositivo programable equivalente.
  A **bajo volumen**, en cambio, un dispositivo programable resulta más económico.
- **Tiempo de diseño y riesgo**: un ASIC no admite corregir errores sin fabricar de nuevo; un
  dispositivo programable permite reprogramar y corregir en minutos.
- **Rendimiento**: un ASIC, al estar optimizado a nivel de transistor para una única función, suele
  lograr mayor velocidad y menor consumo que la lógica equivalente sobre una FPGA.

```{tip}
La presentación de la materia ilustra este contraste con dos ejemplos reales: un ASIC aeroespacial
de Atmel (que exige un conocimiento profundo de electrónica y microelectrónica, ver
{cite}`millman1995` en el capítulo de bibliografía general) frente a una FPGA Stratix III de Altera
y un dispositivo PAL (que exigen, sobre todo, conocimiento de **diseño lógico digital** — el
contenido de este mismo apunte).
```

## 8. Aplicaciones típicas

- **PAL/GAL**: lógica de "pegamento" simple (decodificación de direcciones, combinación de señales
  de control) en placas ya diseñadas, donde no vale la pena una FPGA completa.
- **CPLD**: control de tamaño pequeño-mediano, donde interesa la no volatilidad y la predictibilidad
  de tiempos por sobre la densidad lógica.
- **FPGA**: prototipado de diseños que eventualmente pasarán a ASIC, procesamiento de señales de alto
  rendimiento, sistemas embebidos con requerimientos de paralelismo (por ejemplo, varios periféricos
  o unidades de cómputo funcionando simultáneamente), y producción de volumen bajo o medio donde el
  costo de un ASIC no se justifica.
- **ASIC**: producción masiva (procesadores de consumo, chips de teléfonos celulares) donde el
  volumen diluye el costo de ingeniería y donde el rendimiento/consumo son críticos.

## 9. Resumen

- La **lógica programable** agrupa dispositivos cuyo comportamiento se define después de
  fabricados, en contraste con el **ASIC**, de función fija.
- **PROM**, **PLA** y **PAL** se distinguen por qué plano (AND, OR, o ambos) es programable; la
  **GAL** es una PAL reprogramable eléctricamente.
- El **CPLD** interconecta varios bloques tipo PAL/GAL mediante una matriz programable, y es no
  volátil.
- La **FPGA** escala la idea a bloques lógicos configurables (LUTs) con matrices de interconexión
  programables, alcanzando densidades muy superiores, aunque típicamente a costa de ser volátil.
- El flujo de diseño típico va de HDL → síntesis → mapeo tecnológico → *place & route* → bitstream →
  programación del dispositivo.
- La elección entre ASIC y dispositivo programable es, en esencia, un trade-off entre **costo de
  ingeniería no recurrente**, **volumen de producción**, **tiempo de diseño** y **rendimiento**.

## 10. Bibliografía

```{bibliography}
:filter: docname in docnames
```

## 11. Ejercicios propuestos

```{exercise}
:label: ex-logprog-1
Explicar con tus palabras la diferencia entre una PROM, una PLA y una PAL en términos de qué plano
(AND u OR) es programable en cada una.
```

```{solution} ex-logprog-1
:class: dropdown
En la **PROM** el plano AND es fijo (actúa como un decodificador que genera todos los minterms
posibles) y el plano OR es programable. En la **PLA** ambos planos son programables, lo que permite
elegir tanto qué términos producto se generan como cómo se combinan en las salidas. En la **PAL** el
plano AND es programable pero el plano OR es fijo (cada salida suma un número fijo de términos
producto), lo que la hace más simple y rápida que una PLA a costa de flexibilidad.
```

```{exercise}
:label: ex-logprog-2
¿Por qué la mayoría de las FPGA comerciales necesitan recargar su configuración cada vez que se
energizan, mientras que un CPLD no?
```

```{solution} ex-logprog-2
:class: dropdown
Porque las FPGA suelen basar sus celdas de configuración en tecnología **SRAM**, que es volátil (ver
[Memoria](21-memoria.md)): pierde su contenido sin alimentación. Los CPLD, en cambio, suelen usar
tecnología de memoria no volátil (equivalente a EEPROM/Flash) para almacenar su configuración, por
lo que la retienen aun sin alimentación.
```

```{exercise}
:label: ex-logprog-3
Una empresa va a producir 200 unidades de un controlador digital simple. Otra va a producir
5.000.000 de unidades de un chip de audio. ¿Cuál de las dos convendría implementar sobre FPGA y
cuál sobre ASIC, y por qué?
```

```{solution} ex-logprog-3
:class: dropdown
Las 200 unidades del controlador conviene implementarlas sobre **FPGA** (o incluso CPLD si el diseño
es chico): el costo de ingeniería no recurrente de un ASIC no se justifica repartido entre tan pocas
unidades. Los 5.000.000 de chips de audio, en cambio, justifican un **ASIC**: a ese volumen, el
costo de diseño se diluye por unidad y se gana en rendimiento, consumo y costo unitario respecto de
una solución programable.
```

```{exercise}
:label: ex-logprog-4
Ordenar de menor a mayor densidad lógica típica: FPGA, PAL, CPLD.
```

```{solution} ex-logprog-4
:class: dropdown
PAL < CPLD < FPGA. La PAL es un único bloque simple de plano AND programable/OR fijo; el CPLD reúne
varios bloques tipo PAL interconectados; la FPGA multiplica esa idea a una escala mucho mayor con
miles o millones de LUTs interconectadas.
```

```{exercise}
:label: ex-logprog-5
¿Qué etapa del flujo de diseño (sección 6) es la responsable de decidir en qué LUT física de la
FPGA queda ubicada cada función lógica del diseño?
```

```{solution} ex-logprog-5
:class: dropdown
La etapa de **place & route**: el mapeo tecnológico ya decidió qué recursos (LUTs, flip-flops) usa
cada parte del diseño, pero es el *place & route* el que asigna la ubicación física concreta dentro
del chip y configura la matriz de interconexión para conectar esos recursos entre sí.
```
