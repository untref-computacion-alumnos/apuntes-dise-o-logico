---
title: "Registros"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Registros

```{admonition} Sobre este apunte
:class: note
Este apunte desarrolla las secciones "Registro" y "Banco de registros" de la presentación
*Circuitos Secuenciales II* (Lucas Leiva, Diseño Lógico 2024), junto con la sección "Registros de
datos" de *Circuitos Secuenciales I* (Diseño Digital 2024). El ejemplo paso a paso del registro de
desplazamiento sigue la misma secuencia de entrada (`s_in = 0,1,1,0,1`) que la diapositiva
original, partiendo de un estado inicial conocido (todo en 0) para que la tabla quede
autocontenida. Se asume conocido el contenido de
[Circuitos secuenciales asincrónicos y sincrónicos](17-circuitos-secuenciales-asincronicos-y-sincronicos.md).
```

## 1. Registro PIPO

Un flip-flop almacena 1 bit. Para almacenar $n$ bits se usan $n$ flip-flops en paralelo, todos con
entrada de reloj (y habitualmente reset) comunes: cada bit de entrada $a_i$ se conecta a la entrada
$D$ de un flip-flop, y cada salida $s_i$ es la $Q$ correspondiente. Esta disposición se conoce como
**registro PIPO** (*Parallel Input – Parallel Output*):

```text
   a3   a2   a1   a0
   │    │    │    │
 ┌─▼─┐┌─▼─┐┌─▼─┐┌─▼─┐
 │D Q├┤D Q├┤D Q├┤D Q│
 └─┬─┘└─┬─┘└─┬─┘└─┬─┘
   │    │    │    │
   s3   s2   s1   s0

clk, rst: comunes a los cuatro flip-flops
```

### Ejemplo comercial: SN54273

El circuito integrado comercial **SN54273** implementa un registro PIPO de 8 bits con 8 flip-flops
tipo D:

- Señales de reloj (`CLK`) y de clear (`CLR'`) **comunes** a los 8 flip-flops.
- Los datos se almacenan en el **flanco ascendente** de `CLK`.
- La señal de clear está **activa en estado bajo** (`CLR' = 0` fuerza todas las salidas a 0,
  independientemente del reloj).

## 2. Habilitación de escritura (write enable)

En muchos diseños el registro debe mantener su valor durante varios ciclos de reloj y actualizarse
solo cuando una señal de habilitación `we` (*write enable*) está activa.

### 2.1 Solución inválida: intervenir la línea de reloj

Una primera idea es "cortar" el reloj con una compuerta AND: `clk_gated = clk AND we`.

```{warning}
Esta solución es **inválida**. Interferir sobre la línea de reloj puede introducir *glitches* y
retardos adicionales (*clock skew*) que rompen la sincronización entre flip-flops del mismo
registro o de registros distintos que comparten el mismo reloj. Además, si `we` cambia cerca de un
flanco activo de `clk`, la compuerta AND puede generar un pulso de reloj angosto o deformado,
violando los tiempos de $t_s$/$t_h$ vistos en
[Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md) y llevando al
flip-flop a un estado metaestable.
```

### 2.2 Solución válida: multiplexor en la línea de datos

La solución correcta **no toca la línea de reloj**: el reloj llega sin modificar a todos los
flip-flops, y en su lugar se coloca un **multiplexor 2 a 1** en la entrada $D$, que elige entre el
dato nuevo y el valor actual del propio flip-flop (realimentado):

$$d_{FF} = (Q \cdot we') + (d_{nuevo} \cdot we)$$

```text
              we
              │
   Q ────┐    │
         ▼    ▼
       ┌────────┐
       │ MUX2_1 ├──► D
       └────────┘
         ▲
d_nuevo ─┘
```

- Si $we=0$: $d_{FF}=Q$ → el flip-flop se realimenta a sí mismo y **mantiene** su valor anterior
  (aunque el reloj lo siga disparando en cada flanco).
- Si $we=1$: $d_{FF}=d_{nuevo}$ → se **guarda** el nuevo dato.

Esta solución no interfiere con la línea de reloj y por lo tanto no introduce problemas de
sincronismo.

## 3. Registro de desplazamiento

Un **registro de desplazamiento** (*shift register*) desplaza, en cada ciclo de reloj, el
contenido almacenado una posición hacia la derecha o hacia la izquierda. Cada flip-flop recibe el
valor almacenado en el flip-flop vecino.

### 3.1 SIPO: desplazamiento a derecha

En un **SIPO** (*Serial Input – Parallel Output*), el dato entra bit a bit por un extremo (entrada
serie `s_in`) y puede leerse en paralelo por las salidas $s_3 s_2 s_1 s_0$:

```text
 s_in──►D Q├─►D Q├─►D Q├─►D Q
        s3     s2     s1     s0
   clk, rst: comunes a los cuatro flip-flops
```

Cada flip-flop toma, en el siguiente flanco de reloj, el valor que tenía almacenado el flip-flop a
su izquierda; el de más a la izquierda ($s_3$) toma el valor de `s_in`.

**Ejemplo paso a paso.** Partiendo del estado inicial $0000$ e ingresando la secuencia
`s_in = 0, 1, 1, 0, 1` (un bit por ciclo de reloj):

| Ciclo | s_in | $s_3$ | $s_2$ | $s_1$ | $s_0$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 (inicial) | — | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 0 | 0 |
| 3 | 1 | 1 | 1 | 0 | 0 |
| 4 | 0 | 0 | 1 | 1 | 0 |
| 5 | 1 | 1 | 0 | 1 | 1 |

En cada fila, $s_0 \leftarrow s_1^{\text{anterior}}$, $s_1 \leftarrow s_2^{\text{anterior}}$,
$s_2 \leftarrow s_3^{\text{anterior}}$ y $s_3 \leftarrow \texttt{s\_in}$. Si el registro no se
resetea antes de empezar a desplazar, su contenido inicial es indeterminado ("basura"); con $n$
bits, hacen falta exactamente $n$ ciclos de reloj para que esa basura termine de "lavarse" por
completo y las $n$ salidas queden determinadas únicamente por los bits ingresados.

```{important}
Los elementos de memoria de un registro de desplazamiento **deben ser flip-flops** (sensibles a
flanco), nunca latches. Si fueran latches con una señal de habilitación común a todos, mientras esa
señal está activa cada latch es transparente y el dato ingresado se propagaría instantáneamente a
través de toda la cadena en un mismo ciclo (un "carrera" o *race-through*), en vez de avanzar una
sola posición por ciclo de reloj. La naturaleza de flanco del flip-flop es justamente lo que
garantiza que cada etapa capture el valor de la etapa anterior **antes** de que esta cambie — ver
[Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md#id-3-latch-vs-flip-flop)
para la comparación completa entre latches y flip-flops.
```

### 3.2 SISO

Si solo interesa el bit que va "saliendo" por el otro extremo (y no el contenido completo en
paralelo), se usa la misma estructura pero se lee únicamente la última salida ($s_0$ en el ejemplo):
un registro **SISO** (*Serial Input – Serial Output*). Es la base de las líneas de retardo digitales
y de la comunicación serie.

### 3.3 Desplazamiento a izquierda

La lógica es simétrica: cada flip-flop recibe el contenido almacenado en el flip-flop de su
**derecha**, y la entrada serie ingresa por el extremo opuesto (en el ejemplo, por $s_0$).

### 3.4 Ejemplo comercial

El circuito integrado **M74HC164** es un registro de desplazamiento SIPO de 8 bits comercial, con
dos entradas serie combinadas por AND y salidas paralelas de las 8 etapas.

## 4. Registro universal

Un **registro universal** combina en un solo bloque las cuatro operaciones anteriores (carga
paralela, mantener, desplazar a izquierda, desplazar a derecha), seleccionadas mediante un código de
control de 2 bits:

| control | operación |
|:---:|---|
| 0 | $s \leftarrow a$ (carga paralela) |
| 1 | $s \leftarrow s$ (mantiene) |
| 2 | $s \leftarrow s \ll 1$ (desplaza a izquierda) |
| 3 | $s \leftarrow s \gg 1$ (desplaza a derecha) |

Se construye colocando, delante de la entrada $D$ de **cada** flip-flop, un multiplexor 4 a 1 cuyas
cuatro entradas son: el bit correspondiente de la carga paralela $a_i$, la propia salida $Q_i$
(mantener), la salida del vecino de la izquierda (desplazar a la izquierda) y la salida del vecino
de la derecha (desplazar a la derecha), todos gobernados por el **mismo** código `control`:

```text
control ──┬─────────────┬─────────────┬─────────────┐
          │             │             │             │
 a3 ──┐   │      a2 ──┐  │     a1 ──┐  │     a0 ──┐  │
      ├[MUX4_1]─►D Q├─┴──┤[MUX4_1]─►D Q├┴──┤[MUX4_1]─►D Q├┴──┤[MUX4_1]─►D Q
 s_in─┘       s3         s2            s1            s0
   clk: común a los cuatro flip-flops
```

```{tip}
Mediante desplazamientos a izquierda o derecha es posible **multiplicar o dividir por 2** el valor
almacenado. Esto no permite, por sí solo, multiplicar por cualquier constante — pero combinando
desplazamientos con sumas parciales (técnica de *shift-and-add*) sí es posible multiplicar por
cualquier valor, descomponiéndolo en potencias de 2 (esta es, de hecho, la base de los
multiplicadores binarios de bajo costo).
```

## 5. Banco de registros

Un **banco de registros** (*register file*) agrupa $n$ registros PIPO direccionables
individualmente. Sus señales típicas son:

- `addr_rd`: dirección de lectura.
- `addr_wr`: dirección de escritura.
- `data_wr`: dato a escribir.
- `we`: habilitación de escritura.
- `data_rd`: dato leído (salida).

```text
                       we
                       │
            ┌──────────┼─────────────────────────┐
            │      ┌───▼───┐  ┌───────┐  ┌───────┐│
addr_wr ───►│DECOD  │Reg0 we├  │Reg1 we├  │Reg2 we├┤ ...
            │  n:2^n│d_in  ├  │d_in   ├  │d_in   ├│
            └───────┴───┬───┘  └───┬───┘  └───┬───┘│
data_wr ─────────────────┴──────────┴──────────┘   │
                                                     │
addr_rd ────────────────────────────►[MUX 2^n:1]────┴──► data_rd
```

### Preguntas de diseño

- **¿Cuál es el ancho de `addr_rd` y `addr_wr`?** Con $n$ registros hacen falta
  $\lceil \log_2 n \rceil$ líneas de dirección para poder identificar a cada uno (ver
  [Codificadores y decodificadores](14-codificadores-y-decodificadores.md)).
- **¿Es necesario direccionar `data_wr`?** No: el dato a escribir se envía **a todos** los
  registros por igual; lo que decide *cuál* de ellos efectivamente lo almacena es la línea de `we`
  individual generada por el decodificador de `addr_wr` (solo el registro seleccionado tiene su
  entrada de habilitación en 1).
- **¿Los registros pueden ser latches?** No, en general: si el banco de registros participa en
  operaciones del tipo $R_i = F(R_j, R_k)$ donde el destino coincide con un operando de entrada
  (muy frecuente en una ALU), usar latches puede hacer que el nuevo valor "recircule" dentro del
  mismo nivel de reloj. Ver la sección 6.
- **Escalado**: para pasar de un banco de 16 registros de 32 bits a uno de **32 registros de 32
  bits**, se duplica la cantidad de registros y se agrega **1 bit** a `addr_rd`/`addr_wr` (de 4 a 5
  bits), ampliando el decodificador de escritura a 5:32 y el multiplexor de lectura a 32:1. Para
  pasar a uno de **16 registros de 64 bits**, se mantiene el ancho de direcciones (4 bits, 16
  registros) y simplemente se **duplica el ancho de cada registro** (64 flip-flops por registro en
  lugar de 32), replicando también al doble el ancho de `data_wr`, `data_rd` y el multiplexor de
  lectura.

## 6. Latches vs. flip-flops en registros: por qué importa

Como se desarrolla en
[Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md) y se retoma en
[Circuitos contadores](19-circuitos-contadores.md), cuando el nuevo valor de un registro depende
**combinacionalmente de su propio valor anterior** (por ejemplo, `Register4 → Adder4 → Register4`
realimentado), es **obligatorio** usar flip-flops.

Si el registro se implementara con **latches** y el reloj permanece en su nivel activo durante un
tiempo mayor al retardo del sumador, el valor recorrería el lazo latch→sumador→latch **más de una
vez** dentro de un mismo nivel de reloj: por ejemplo, con un reloj de período 20 ns (10 ns en alto y
10 ns en bajo) y un sumador de 4 ns de retardo, el dato podría dar más de una vuelta por el lazo
mientras el latch está transparente, y el contador **no avanzaría de a uno por ciclo** como se
espera, sino un número de posiciones dependiente de la relación entre el tiempo en alto del reloj y
el retardo del combinacional. Los **flip-flops**, al ser sensibles a un flanco y no a un nivel,
garantizan que la realimentación se actualice **exactamente una vez** por ciclo de reloj.

## 7. Resumen

- Un registro PIPO almacena $n$ bits en paralelo con $n$ flip-flops D y señales de reloj/clear
  comunes.
- La habilitación de escritura (`we`) **nunca** debe implementarse cortando la línea de reloj; se
  implementa con un multiplexor que realimenta la propia salida del flip-flop cuando `we=0`.
- Los registros de desplazamiento (SIPO, SISO, a izquierda o derecha) mueven el contenido una
  posición por ciclo de reloj y permiten conversión serie↔paralelo.
- El registro universal combina carga paralela, retención y desplazamiento en ambos sentidos
  mediante multiplexores 4 a 1 gobernados por un código de control común.
- Un banco de registros combina un decodificador (para la escritura, selecciona qué registro
  habilita) y un multiplexor (para la lectura, selecciona qué registro se observa).
- Siempre que el nuevo valor de un registro dependa combinacionalmente de su valor anterior, se
  deben usar flip-flops y no latches, para garantizar una única actualización por ciclo de reloj.

## 8. Ejercicios propuestos

```{exercise}
:label: ex-registro-1
Diseñar la lógica de habilitación de escritura para un registro de 4 bits, mostrando la ecuación
de la entrada $D$ de cada flip-flop en función del dato nuevo, la salida actual y `we`.
```

```{solution} ex-registro-1
:class: dropdown
Para cada bit $i \in \{0,1,2,3\}$: $d_i = (Q_i \cdot we') + (d_{nuevo,i} \cdot we)$, implementado
con un multiplexor 2 a 1 por bit, exactamente como en la sección 2.2, replicado 4 veces.
```

```{exercise}
:label: ex-registro-2
A partir de un registro de desplazamiento SIPO de 4 bits que desplaza a la derecha, indicar el
contenido del registro luego de 4 ciclos de reloj, partiendo de $0000$ e ingresando la secuencia
`s_in = 1,1,0,1`.
```

```{solution} ex-registro-2
:class: dropdown
Ciclo 1 (`s_in=1`): 1000. Ciclo 2 (`s_in=1`): 1100. Ciclo 3 (`s_in=0`): 0110. Ciclo 4 (`s_in=1`):
1011. (Cada ciclo, $s_3 \leftarrow$ `s_in`, y el resto se desplaza una posición a la derecha.)
```

```{exercise}
:label: ex-registro-3
Un banco de registros tiene 64 registros de 16 bits. ¿Cuántas líneas de dirección necesitan
`addr_rd` y `addr_wr`? ¿Cuántas entradas tiene el multiplexor de lectura?
```

```{solution} ex-registro-3
:class: dropdown
$\log_2 64 = 6$ líneas de dirección para cada uno de `addr_rd` y `addr_wr`. El multiplexor de
lectura es un $\text{MUX}_{64\_16}$ (64 entradas de 16 bits cada una, 1 salida de 16 bits).
```

```{exercise}
:label: ex-registro-4
Explicar por qué el contador de programa (PC) de un procesador debe implementarse con flip-flops y
no con latches, usando el vocabulario de este capítulo.
```

```{solution} ex-registro-4
:class: dropdown
El PC es un registro realimentado a través de un sumador (`PC ← PC + 1`, ver
[Circuitos contadores](19-circuitos-contadores.md)): su valor nuevo depende combinacionalmente de
su valor viejo. Por la razón desarrollada en la sección 6, con latches el valor podría recircular
más de una vez por ciclo de reloj; con flip-flops, se garantiza exactamente un incremento por ciclo.
```

## 9. Bibliografía

```{bibliography}
:filter: docname in docnames
```
