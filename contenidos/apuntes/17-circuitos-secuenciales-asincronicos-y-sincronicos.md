---
title: "Circuitos Secuenciales Asincrónicos y Sincrónicos"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Circuitos Secuenciales Asincrónicos y Sincrónicos

```{admonition} Sobre este apunte
:class: note
Este capítulo desarrolla íntegramente el contenido de la presentación "Circuitos Secuenciales I"
de la cátedra: elementos de memoria (latches y flip-flops), la configuración maestro-esclavo, los
flip-flops JK y T, y los tiempos característicos de conmutación. Se completa con precisiones de
bibliografía estándar {cite}`tocci2007,harris2012,floyd2000` donde la presentación es breve (por
ejemplo, el concepto de metaestabilidad).
```

## 1. De los circuitos combinacionales a los secuenciales

Como se vio en [Circuitos lógicos combinacionales](09-circuitos-logicos-combinacionales.md), en
un circuito **combinacional** las salidas dependen exclusivamente de la combinación de entradas: ante
la misma combinación, el circuito siempre se estabiliza con las mismas salidas.

En un **circuito secuencial**, en cambio, las salidas dependen de las entradas **y del estado** en
que se encuentra el circuito. Por eso se dice que los circuitos secuenciales **poseen memoria**: la
misma combinación de entradas puede producir salidas distintas según la historia previa del
circuito.

```{important}
La diferencia estructural clave es la **realimentación** (*feedback*): un circuito secuencial
tiene caminos que llevan una salida (o una señal interna) de vuelta hacia sus propias entradas.
Esa realimentación es lo que le permite "recordar" el estado. Un circuito puramente combinacional,
por definición, no tiene realimentación.
```

## 2. Elementos de memoria: biestables

La unidad básica de memoria de un circuito digital es el **biestable**: un circuito con dos
estados estables, capaz de mantener uno de ellos indefinidamente hasta que una entrada lo fuerce a
cambiar. Todos los elementos de memoria de este capítulo (latches y flip-flops) son variantes de
un biestable.

### 2.1 Latch SR (con compuertas NOR)

El latch SR (*Set-Reset*) es el biestable más simple. Se construye con dos compuertas NOR
realimentadas cruzadamente:

```text
        ┌─────┐
  S ───►│     │
        │ NOR ├──┬──► Q
    ┌──►│     │  │
    │   └─────┘  │
    │             │
    │   ┌─────┐  │
    └───┤     │◄─┘
        │ NOR ├──┬──► Q'
  R ───►│     │  │
        └─────┘  │
                  └──►(realimenta a la NOR de arriba)
```

| $S$ | $R$ | $Q^+$ | Comentario |
|:---:|:---:|:---:|---|
| 0 | 0 | $Q$ | Mantiene el estado anterior |
| 0 | 1 | 0 | *Reset*: pone $Q=0$ |
| 1 | 0 | 1 | *Set*: pone $Q=1$ |
| 1 | 1 | — | **Estado prohibido**: $Q=Q'=0$, viola $Q \ne Q'$ |

donde $Q^+$ denota el próximo estado de $Q$. La combinación $S=R=1$ se considera **prohibida**
porque fuerza $Q=Q'=0$, rompiendo la relación de complemento que debería existir siempre entre
$Q$ y $Q'$; además, si ambas entradas vuelven a 0 simultáneamente, el estado final es
impredecible (depende de diferencias de retardo entre las compuertas).

```{note}
Cuando $S=0$ y $R=0$, el latch **mantiene** su estado: si $Q=0$ lo mantiene en 0, y si $Q=1$ lo
mantiene en 1. Esta es precisamente la propiedad de "memoria" del biestable.
```

### 2.2 Latch SR (con compuertas NAND)

La misma función se puede construir con dos compuertas NAND realimentadas, pero en ese caso las
entradas quedan **negadas** ($S'$, $R'$, activas en bajo):

| $S'$ | $R'$ | $Q^+$ |
|:---:|:---:|:---:|
| 0 | 0 | — (prohibido) |
| 0 | 1 | 1 (*set*) |
| 1 | 0 | 0 (*reset*) |
| 1 | 1 | $Q$ (mantiene) |

Es la versión **dual** de la anterior (ver [Funciones de Boole](06-funciones-de-boole.md) para el
principio de dualidad): la tabla se invierte porque NAND y NOR son duales entre sí.

### 2.3 Latch D síncrono

El latch SR tiene el problema del estado prohibido y requiere manejar dos señales de control. El
**latch D** resuelve ambos problemas con una sola entrada de dato $D$ y una señal de habilitación
$E$ (*enable*):

| $E$ | $D$ | $Q^+$ |
|:---:|:---:|:---:|
| 0 | × | $Q$ (mantiene, sin importar $D$) |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

```text
        ┌──────────┐
  D ───►│          │
        │  Latch D │───► Q
  E ───►│          │───► Q'
        └──────────┘
```

Mientras $E=1$ el latch es **transparente**: $Q$ sigue el valor de $D$ en todo momento. Cuando
$E=0$, el latch retiene el último valor de $D$ que tenía cuando $E$ cayó a 0.

### 2.4 Latch D síncrono con preset y clear asíncronos

En la práctica es habitual agregar dos entradas adicionales que actúan **de inmediato**,
independientemente del valor de $E$: **preset** ($PR$), que fuerza $Q=1$, y **clear** ($CL$), que
fuerza $Q=0$. Son "asíncronas" porque no esperan a la habilitación: se usan típicamente para
inicializar el circuito a un estado conocido al encender el sistema.

```text
        ┌──────────┐
  D ───►│          │
  E ───►│  Latch D │───► Q
 PR ───►│  con PR  │───► Q'
 CL ───►│  y CL    │
        └──────────┘
```

## 3. Latch vs. flip-flop

Hasta acá todos los elementos vistos son **latches**: circuitos sensibles a **nivel** de la señal
de control ($E$ alto o bajo). El **flip-flop**, en cambio, es sensible a **flanco** (ascendente o
descendente) de la señal de reloj: solo puede cambiar de estado en el instante preciso de la
transición del reloj.

| | Latch | Flip-flop |
|---|---|---|
| Sensibilidad | Nivel (todo el tiempo que dura el pulso) | Flanco (un instante) |
| Área | Menor | Mayor (aprox. el doble, requiere dos latches) |
| Uso típico | Retenedores simples, memorias | Registros, contadores, máquinas de estado |

La elección entre uno y otro depende de la aplicación: cuando varios biestables deben cambiar de
estado en el mismo instante de manera predecible (como en un registro o un contador, ver
[Registros](20-registros.md) y [Circuitos contadores](19-circuitos-contadores.md)), se necesita la
precisión del flip-flop.

## 4. Configuración maestro-esclavo: construcción del flip-flop D

Un flip-flop D sensible a flanco ascendente se construye con **dos latches D** en cascada
(*maestro* y *esclavo*), controlados por la misma señal de reloj pero con el reloj del segundo
**invertido** respecto del primero:

```text
                clk
                 │
     ┌───────────┼────────────┐
     │           │            │
     ▼           │            ▼ (invertido)
┌─────────┐      │      ┌─────────┐
│ Latch D │      │      │ Latch D │
│ (maestro│──Q───┼─────►│(esclavo)│───► Q (del flip-flop)
│  DL-DE) │      │      │ DL-DE   │
└─────────┘      │      └─────────┘
      D ─────────┘
```

Mientras el reloj está en bajo, el maestro es transparente (sigue a $D$) y el esclavo está
retenido; cuando el reloj sube, el maestro se congela con el último valor de $D$ y el esclavo se
vuelve transparente, copiando ese valor congelado hacia la salida. El resultado neto es que la
salida **solo cambia en el flanco ascendente** del reloj, tomando el valor que tenía $D$ justo
antes de ese flanco.

```{tip}
Para seguir la secuencia paso a paso conviene armar una tabla temporal con columnas `clk`, `D`,
`Q(maestro)` y `Q(esclavo)`, y verificar que el esclavo (que es la salida del flip-flop) solo
actualiza su valor en el instante exacto en que `clk` pasa de 0 a 1.
```

## 5. Flip-flop JK

El flip-flop **JK** generaliza al SR pero sin estado prohibido: cuando ambas entradas están
activas, el flip-flop **conmuta** (*toggle*) su estado.

| $J$ | $K$ | $Q^+$ | Comentario |
|:---:|:---:|:---:|---|
| 0 | 0 | $Q$ | Mantiene |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | $Q'$ | Conmuta (*toggle*) |

```text
        ┌─────────┐
  J ───►│         │───► Q
        │   JK    │
  K ───►│         │───► Q'
        └────┬────┘
             │
            clk
```

### 5.1 Implementación de JK a partir de un flip-flop D

Un flip-flop JK puede construirse combinando un flip-flop D con lógica combinacional que calcule
$D$ en función de $J$, $K$ y el estado actual $Q$:

$$D = J \cdot Q' + K' \cdot Q$$

| $J$ | $K$ | $Q$ | $D$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Esta es una solución directa obtenida de la tabla de verdad; con los métodos del capítulo
[Redundancias](08-redundancias.md) podría simplificarse aún más o reexpresarse de otras formas
equivalentes.

## 6. Flip-flop T

El flip-flop **T** (*Toggle*) tiene una única entrada de control $T$: cuando $T=1$, conmuta en
cada flanco de reloj; cuando $T=0$, mantiene su estado.

| $T$ | $Q^+$ |
|:---:|:---:|
| 0 | $Q$ |
| 1 | $Q'$ |

Es exactamente el comportamiento del flip-flop JK cuando se conectan sus entradas juntas,
$T = J = K$. El flip-flop T es la base de los **contadores asincrónicos** (ver
[Circuitos contadores](19-circuitos-contadores.md)), porque conmutar en cada flanco es
precisamente lo que hace el bit menos significativo de un contador binario.

## 7. Registros de datos y la necesidad de usar flip-flops

Para almacenar una palabra de $m$ bits se puede usar tanto un banco de $m$ latches como de $m$
flip-flops (ver [Registros](20-registros.md) para el desarrollo completo de registros). Sin
embargo, hay situaciones en las que **solo** un flip-flop es válido.

Considérese la operación $R_i = F(R_j, R_k)$, típica de un procesador (por ejemplo, en una
operación con la ALU y el banco de registros), en el caso particular en que el registro destino
coincide con uno de los operandos de entrada ($R_i = R_j$ o $R_i = R_k$). Un ejemplo concreto es un
contador de 4 bits construido como `Register4 + Adder4` realimentado:

```text
        ┌───────────┐
   ┌───►│  Adder4   ├───┐
   │    │   (+1)    │   │
   │    └───────────┘   │
   │                     │
   │    ┌───────────┐   │
   └────┤ Register4 │◄──┘
  clk──►│           │
        └───────────┘
```

Supongamos que el reloj tiene un período de 20 ns (10 ns en alto, 10 ns en bajo) y que el sumador
combinacional `Adder4` tarda 4 ns en estabilizar su salida. Si el registro se implementara con
**latches**:

```{warning}
Mientras el reloj está en el nivel que habilita al latch (transparente), la nueva salida del
sumador —que depende de la salida actual del registro— vuelve a entrar inmediatamente al latch, que
la vuelve a copiar. Como el sumador tarda solo 4 ns y el nivel habilitado dura 10 ns, el valor
puede dar **más de una vuelta** por el lazo combinacional-latch durante un mismo semiciclo de
reloj: el contador no avanza de a uno por ciclo, sino un número impredecible de incrementos.
```

Esto no ocurre con **flip-flops**, porque estos solo capturan el valor de entrada en el instante
del flanco: aunque la salida del sumador realimente su propia entrada, el flip-flop ignora
cualquier cambio posterior hasta el próximo flanco de reloj. Por eso, siempre que el registro
destino sea también uno de los operandos de entrada del circuito combinacional que lo alimenta,
**deben usarse flip-flops**, nunca latches.

## 8. Tiempos característicos de un flip-flop

El funcionamiento correcto de un flip-flop exige que la entrada de datos sea estable durante una
ventana de tiempo alrededor del flanco activo de reloj:

- **Tiempo de establecimiento** ($t_s$, *setup time*): tiempo mínimo que el dato debe permanecer
  estable **antes** del flanco activo de reloj.
- **Tiempo de mantenimiento** ($t_h$, *holding time*): tiempo mínimo que el dato debe permanecer
  estable **después** del flanco activo de reloj.
- **Tiempo de propagación** ($t_p$): tiempo que tarda la salida $Q$ en reflejar el nuevo valor,
  contado desde el flanco activo de reloj.

```text
        D  ──────╳═══════════════════╳──────
                  │←── ts ──►│←── th ──►
       clk  ──────┴──────────╱‾‾‾‾‾‾‾‾‾‾‾‾
                              │
         Q  ─ ─ ─ ─ ─ ─ ─ ─ ─┼─────►│←tp►╳──
                              flanco activo
```

```{important}
Si no se cumple $t_s$ (el dato cambia demasiado cerca —antes— del flanco) o no se cumple $t_h$ (el
dato cambia demasiado cerca —después— del flanco), el flip-flop puede entrar en un estado de
**metaestabilidad**: una condición transitoria en la que la salida queda en un nivel intermedio o
tarda un tiempo impredecible en resolverse a 0 o a 1 {cite}`harris2012`. Es una de las causas más
frecuentes de fallas en sistemas digitales reales, especialmente al sincronizar señales que vienen
de otro dominio de reloj.
```

## 9. Clasificación: circuitos síncronos y asincrónicos

Un circuito secuencial se llama **síncrono** cuando **todos** sus elementos de memoria cambian de
estado exactamente en el mismo instante, gobernados por una única señal de reloj común. Se llama
**asincrónico** cuando los elementos de memoria no se actualizan todos en el mismo instante: cada
uno cambia en respuesta a un evento (por ejemplo, el cambio de otro biestable), lo que introduce
retardos de propagación acumulados entre etapas.

Esta distinción se desarrolla en detalle, con ejemplos completos de diseño, en el capítulo
[Circuitos contadores](19-circuitos-contadores.md), donde se construyen y comparan un contador
asincrónico (con flip-flops T encadenados) y uno sincrónico (con todos los flip-flops disparados
por el mismo flanco de reloj).

## 10. Resumen

- Un circuito **secuencial** tiene memoria: sus salidas dependen de las entradas y del estado, a
  diferencia de un circuito **combinacional**. La realimentación es la diferencia estructural.
- El **latch SR** es el biestable más simple, pero tiene un estado prohibido; el **latch D**
  resuelve ese problema con una sola entrada de dato y una habilitación.
- Un **flip-flop** (sensible a flanco) se diferencia de un **latch** (sensible a nivel); se
  construye típicamente en configuración **maestro-esclavo** con dos latches D.
- El **flip-flop JK** generaliza al SR sin estado prohibido (conmuta cuando $J=K=1$); el
  **flip-flop T** es un caso particular del JK ($T=J=K$) y es la base de los contadores.
- Cuando el registro destino de una operación coincide con uno de sus operandos de entrada, deben
  usarse **flip-flops**, nunca latches, para evitar que el dato dé más de una vuelta por el lazo
  combinacional durante un mismo pulso de reloj.
- Los tiempos de **setup**, **hold** y **propagación** determinan el funcionamiento correcto de un
  flip-flop; violarlos puede producir **metaestabilidad**.

## 11. Bibliografía

```{bibliography}
:filter: docname in docnames
```

## 12. Ejercicios propuestos

```{exercise}
:label: ex-secuencial-1
Implementar un flip-flop T a partir de un flip-flop D.
```

```{solution} ex-secuencial-1
:class: dropdown
Como el flip-flop T conmuta cuando $T=1$ y mantiene cuando $T=0$, basta con conectar
$D = T \oplus Q$: si $T=0$, $D=Q$ (mantiene); si $T=1$, $D=Q'$ (conmuta).
```

```{exercise}
:label: ex-secuencial-2
Implementar un flip-flop T a partir de un flip-flop JK.
```

```{solution} ex-secuencial-2
:class: dropdown
Se conectan ambas entradas del JK entre sí: $J=K=T$. Cuando $T=0$ ($J=K=0$) el JK mantiene;
cuando $T=1$ ($J=K=1$) el JK conmuta, que es exactamente el comportamiento del flip-flop T.
```

```{exercise}
:label: ex-secuencial-3
Implementar un flip-flop JK a partir de un flip-flop T.
```

```{solution} ex-secuencial-3
:class: dropdown
Se necesita lógica combinacional que decida cuándo conmutar en función de $J$, $K$ y el estado
actual $Q$: el flip-flop debe conmutar cuando ($J=1$ y $Q=0$) o cuando ($K=1$ y $Q=1$). Es decir:
$$T = J \cdot Q' + K \cdot Q$$
y esa señal $T$ es la que se conecta a la entrada del flip-flop T.
```

```{exercise}
:label: ex-secuencial-4
¿Por qué un latch D síncrono con preset y clear asíncronos permite inicializar el circuito "al
encender" sin esperar a un flanco de reloj?
```

```{solution} ex-secuencial-4
:class: dropdown
Porque preset y clear actúan de forma **asíncrona**: fuerzan $Q=1$ o $Q=0$ inmediatamente al
activarse, sin depender de la señal de habilitación/reloj. Esto permite llevar el circuito a un
estado conocido apenas se energiza el sistema, antes de que el reloj empiece siquiera a
funcionar de forma estable.
```
