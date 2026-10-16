---
title: "Lenguajes de Programación HDL"
subject: "Diseño Lógico"
author: "Prof. Dr. Martín Vázquez"
---

# Lenguajes de Programación HDL

```{admonition} Sobre este apunte
:class: note
Este apunte reorganiza y desarrolla el material de las clases **"Introducción a VHDL - Parte I"**
y **"Introducción a VHDL - Parte II"** (Prof. Dr. Martín Vázquez - Lucas Leiva). Es, por lejos, el
capítulo con más contenido fuente de todo el apunte: junta dos clases completas dedicadas al
lenguaje que se usa en la materia para describir, simular y sintetizar los circuitos digitales
vistos en los capítulos anteriores. Se organiza en dos partes: **Parte I** cubre los fundamentos
del lenguaje (tipos, estructura, concurrencia, estilos de modelado) y **Parte II** cubre el diseño
jerárquico y la verificación mediante testbenches. Donde hizo falta completar con bibliografía
estándar de VHDL se citan {cite}`ashenden2008designers`, {cite}`skahill1996`, {cite}`perry2002` y
{cite}`chu2008fpga`.
```

## Parte I: Fundamentos de VHDL

### 1. ¿Qué es un HDL y por qué se usa?

Un **HDL** (*Hardware Description Language*, lenguaje de descripción de hardware) es un lenguaje de
alto nivel para modelar circuitos digitales, alternativo al uso de esquemáticos dibujados a mano.
**VHDL** significa **VHSIC Hardware Description Language**, donde VHSIC es a su vez la sigla de
*Very High Speed Integrated Circuit*.

Los usos principales de un HDL son:

- **Documentar** un diseño de forma no ambigua.
- **Especificar** requerimientos funcionales.
- **Simular** el circuito para comprobar su funcionalidad y detectar errores antes de fabricarlo.
- **Sintetizar**: obtener a partir de la descripción una implementación real en hardware (ver
  [Implementación](10-implementacion.md)).

```{note}
VHDL no es el único HDL utilizado en la industria: **Verilog** (más cercano en su sintaxis al
lenguaje C) es el otro gran estándar, especialmente extendido en Estados Unidos y en el diseño de
semiconductores comercial. Este curso trabaja exclusivamente con VHDL, pero los conceptos de fondo
(entidad/módulo, señales, procesos, síntesis) son equivalentes entre ambos lenguajes.
```

### 2. Historia de VHDL

- Propuesto en **1980** por el Departamento de Defensa de EE.UU. dentro del proyecto **VHSIC**.
- Primera versión del lenguaje: **1985**.
- Estandarizado por el **IEEE** en **1987** (IEEE 1076).
- Primer gran éxito de aplicación: el programa del caza **F-22** (1986-1993).
- Revisiones posteriores del estándar: **1993, 2000, 2002 y 2008**.

```{admonition} El costo de estandarizar un lenguaje
:class: tip
Se estima que el desarrollo del lenguaje VHDL costó unos **U$S 17 millones**, y el desarrollo de
las herramientas asociadas (simuladores, sintetizadores) otros **U$S 16 millones**. Da una idea de
la magnitud de la inversión necesaria para introducir un estándar de diseño en toda una industria.
```

### 3. VHDL frente a un lenguaje de programación de software

**Similitudes:**

- Es un lenguaje **estructurado**.
- Permite la **reutilización de módulos**.
- Es **portable** entre herramientas y fabricantes.

**Diferencias clave:**

- El paradigma es distinto: VHDL está **orientado a procesos** concurrentes, no a una secuencia
  única de instrucciones.
- Las sentencias **no siempre se ejecutan secuencialmente** (fuera de un proceso, todo es
  concurrente).
- La información **temporal es explícita**: en VHDL tiene sentido preguntar "¿en qué instante
  cambia esta señal?".
- VHDL **no se compila en un ejecutable**: se **sintetiza** en un circuito digital real (o se
  simula, sin llegar a sintetizarse, en el caso de los testbenches — ver sección 22).

### 4. Ventajas de VHDL y niveles de abstracción

Ventajas del lenguaje: está **estandarizado**, cuenta con **soporte gubernamental e industrial**, es
**portable**, permite **diseño modular y jerárquico**, favorece la **reusabilidad** de código, y
admite distintos **niveles de abstracción**:

- **Comportamental**: conjunto de instrucciones secuenciales que describen *qué* hace el circuito,
  sin detallar relojes o retardos. No siempre es sintetizable — se usa sobre todo para simular
  (ver testbenches, sección 22).
- **RTL** (*Register-Transfer-Level*): es la entrada típica para la síntesis. Las operaciones se
  realizan en un ciclo de reloj específico, sin detallar retardos internos.
- **Lógico o de compuertas**: es la **salida** de la síntesis, expresado en términos de ecuaciones
  lógicas o de compuertas de una biblioteca genérica o específica, ya con información de retardo.

Es conveniente describir en VHDL en el nivel de abstracción **más alto que resulte sintetizable**
(en general, RTL). Estos niveles son la contraparte, del lado del lenguaje, de los niveles de
abstracción del diseño hardware ya vistos en [Implementación](10-implementacion.md): algorítmico →
lógico (HDL) → circuito lógico (compuertas) → físico (transistor y layout).

```{mermaid}
flowchart LR
    A[Comportamental] --> B[RTL]
    B --> C["Lógico (compuertas)"]
    C --> D["Físico (transistor / layout)"]
```

### 5. Estructura de un diseño VHDL: entidad y arquitectura

Todo diseño en VHDL cuenta con **dos unidades obligatorias**: la **entidad** (`ENTITY`) y la
**arquitectura** (`ARCHITECTURE`). Una unidad de hardware se modela como una "caja negra": tiene una
**interfaz** completamente definida por sus puertos (modo y tipo), y un **interior oculto** que es
la descripción interna del diseño.

```vhdl
ENTITY nombre_entidad IS
  -- declaración de puertos
END nombre_entidad;

ARCHITECTURE nombre_arquitectura OF nombre_entidad IS
  -- declaraciones de señales y componentes
BEGIN
  -- procesos, sentencias concurrentes, instanciación de componentes
END nombre_arquitectura;
```

- La **entidad** define **qué se ve desde afuera**: los puertos, que son canales de comunicación con
  un nombre único dentro de la entidad, un **modo** (dirección del flujo) y un **tipo** (los valores
  que puede tomar).
- La **arquitectura** define **qué hay adentro**: se compone de una parte declarativa (señales,
  componentes) y un cuerpo (procesos, sentencias concurrentes, instanciaciones).

### 6. Puertos y modos

| Modo | Descripción |
|---|---|
| `IN` | Señal que **entra** a la entidad y no sale. Puede leerse pero no escribirse dentro de la entidad. |
| `OUT` | Señal que **sale** de la entidad y no se usa internamente. No puede leerse dentro de la entidad. |
| `BUFFER` | Señal que sale de la entidad y **además se realimenta** internamente. A diferencia de `OUT`, esta señal sí puede leerse. |
| `INOUT` | Señal **bidireccional**, tanto de entrada como de salida. |

Ejemplo de declaración de entidad con puertos de tipo `std_logic` y `std_logic_vector` (ver
sección 7):

```vhdl
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY mi_componente IS
  PORT (
    clk, rst : IN  std_logic;
    d        : IN  std_logic_vector(7 DOWNTO 0);
    q        : OUT std_logic_vector(7 DOWNTO 0);
    co       : OUT std_logic
  );
END mi_componente;
```

### 7. Sistema de tipos

VHDL es un lenguaje **fuertemente tipado**: todo objeto tiene un tipo declarado, y las asignaciones
solo pueden hacerse entre objetos del **mismo tipo**. Los tipos predefinidos se agrupan en:

- **Escalares**: `integer`, punto flotante, `enumerated` (ver [Representación de números](03-representacion-de-numeros-enteros-fraccionarios-y-negativos.md) para la codificación de estos valores a nivel bit).
- **Compuestos**: `array`, `record`.
- **Punteros**: `access`.
- **Archivos**: `file` (ver sección 23).

Tipos básicos más usados:

| Tipo | Descripción |
|---|---|
| `BIT` | Solo puede valer `'0'` o `'1'`. Modela una señal digital ideal. |
| `BIT_VECTOR` | Array unidimensional de bits. Modela un bus. |
| `INTEGER` | Tipo entero, usado como índice en lazos, constantes o valores genéricos. |
| `BOOLEAN` | Puede valer `TRUE` o `FALSE`. |
| `REAL` | Números en punto flotante (solo para simulación, no sintetizable). |
| `ENUMERATED` | Enumeración definida por el usuario. Ej.: `type estados is (inicio, lento, rapido);` |

**El tipo `std_logic`.** El tipo `BIT` solo admite dos valores, insuficientes para modelar todos los
estados posibles de una señal digital real (una línea sin conducir, un corto entre dos fuentes, alta
impedancia, etc.). El paquete `IEEE.std_logic_1164` define el tipo **`std_logic`**, con nueve
valores posibles:

| Valor | Significado |
|:---:|---|
| `U` | No inicializado (valor por defecto) |
| `X` | Desconocido fuerte — salida con múltiples fuentes en corto |
| `0` | Nivel lógico bajo |
| `1` | Nivel lógico alto |
| `Z` | Alta impedancia |
| `W` | Desconocido débil — terminación de bus |
| `L` | `0` débil (resistencia de *pull-down*) |
| `H` | `1` débil (resistencia de *pull-up*) |
| `-` | No importa — comodín usado para síntesis |

```{important}
Todos estos valores son válidos dentro de un **simulador** VHDL, pero para **síntesis** solo se
reconocen `'1'`, `'0'`, `'Z'`, `'L'`, `'H'` y `'-'`. `std_logic` y `std_logic_vector` (la versión en
bus de `std_logic`) son un estándar industrial y son, en la práctica, los tipos que más se usan para
modelar señales digitales reales, por encima de `bit`/`bit_vector`.
```

El paquete `IEEE.std_logic_1164` también define `std_ulogic` y `std_ulogic_vector`: son los mismos
tipos pero **sin pasar por la función de resolución**, que es la que decide qué valor final toma una
señal cuando dos fuentes distintas le asignan valores diferentes (por ejemplo, si una fuente asigna
`'1'` y otra `'L'`, la resolución determina que la señal queda en `'1'`).

### 8. Arrays y agregados

Los vectores pueden declararse en rango **ascendente** (`to`) o **descendente** (`downto`):

```vhdl
signal a : bit_vector(0 to 3);      -- rango ascendente
signal b : bit_vector(3 downto 0);  -- rango descendente

a <= "0101";  -- a(0)='0', a(1)='1', a(2)='0', a(3)='1'
b <= "0101";  -- b(0)='1', b(1)='0', b(2)='1', b(3)='0'
```

Los **agregados** (*aggregates*) permiten asignar valores a un vector posición por posición, de
forma compacta:

```vhdl
a <= (0 => '1', 1 => c and d, others => 'Z');
```

Esto asigna `'1'` a la posición 0, el resultado de `c and d` a la posición 1, y `'Z'` a todas las
demás posiciones (cláusula `others`).

### 9. Operadores

| Categoría | Operadores |
|---|---|
| Lógicos | `and`, `or`, `not`, `xor`, `xnor` |
| Relacionales | `=`, `/=`, `<`, `<=`, `>`, `>=` |
| Aditivos | `+`, `-`, `&` (concatenación de vectores) |
| Multiplicativos | `*`, `/`, `rem`, `mod` |
| Signo (unarios) | `+`, `-` |
| Desplazamiento (`bit_vector`) | `sll`, `srl`, `sla`, `sra`, `rol`, `ror` |
| Misceláneos | `abs`, `**` (exponenciación) |

### 10. Diseño concurrente

VHDL soporta la noción de **ejecución concurrente**: dentro de una arquitectura, el orden relativo
entre procesos y asignaciones concurrentes **no es relevante** para el resultado. Hay tres formas de
describir concurrencia:

- **Instanciaciones** de componentes (otras entidades).
- **Asignaciones concurrentes** de señales.
- **Procesos**: un conjunto de sentencias *secuenciales* que se evalúan en orden, pero que como
  bloque se ejecuta de forma concurrente con el resto de la arquitectura.

El siguiente ejemplo (un multiplexor de 2 entradas) muestra las tres formas equivalentes de
describir la misma función, dos de ellas concurrentes y una con proceso:

```vhdl
-- Asignación concurrente por ecuación booleana
x <= (a and not sel) or (b and sel);

-- Asignación concurrente condicional
x <= a when sel = '0' else b;

-- Proceso explícito equivalente
mux: process (a, b, sel)
begin
  if (sel = '0') then
    x <= a;
  else
    x <= b;
  end if;
end process;
```

### 11. Procesos

Semánticamente, un **proceso** es un **bucle infinito** de instrucciones secuenciales: el tiempo
**no avanza** mientras el proceso se ejecuta, solo avanza cuando el proceso **se suspende**. Para
que el proceso avance en el tiempo hace falta la instrucción **`wait`**:

- `wait on a, b` — se reactiva ante un cambio en `a` o en `b`.
- `wait for <retraso>` — se reactiva luego de transcurrido un tiempo fijo.
- `wait until <condición>` — se reactiva cuando la condición pasa a ser verdadera.

Un proceso puede ser:

- **Implícito**: la lista de sensibilidad se deduce de la propia expresión (asignaciones
  concurrentes, instanciación de componentes).
- **Explícito**: la lista de sensibilidad se declara entre paréntesis junto al `process`, como en el
  ejemplo del `mux` de la sección anterior (sensible a `a`, `b`, `sel`).

```{tip}
Una arquitectura puede tener tantos procesos como se necesite, y **todos corren en paralelo**. Cada
uno se activa cuando cambia alguna señal de su lista de sensibilidad. Las señales modelan cables:
solo pueden cambiar de valor cuando el tiempo avanza, es decir, cuando algún proceso se suspende.
```

### 12. Sentencias secuenciales

Dentro de un proceso, las sentencias se ejecutan **secuencialmente**, a diferencia del resto de la
arquitectura.

**IF-THEN-ELSE** (con prioridad: se evalúa de arriba hacia abajo, la primera condición verdadera
determina la rama ejecutada):

```vhdl
process (selc, selb, a, b, c)
begin
  if (selc = '1') then
    x <= c;
  elsif (selb = '1') then
    x <= b;
  else
    x <= a;
  end if;
end process;
```

**CASE** (sin prioridad: todas las condiciones se evalúan de una vez; `others` cubre los casos no
enumerados explícitamente):

```vhdl
process (sel, a, b, c, d)
begin
  case sel is
    when "00"   => x <= a;
    when "01"   => x <= b;
    when "10"   => x <= c;
    when others => x <= d;
  end case;
end process;
```

**Bucles (`LOOP`)**: bucle infinito con salida explícita, bucle `while` con condición, y bucle `for`
iterativo sobre un rango:

```vhdl
[label_loop] loop
  -- sentencias secuenciales
end loop [label_loop];

while <condicion> loop
  -- sentencias secuenciales
end loop;

for <identificador> in <rango> loop
  -- sentencias secuenciales
end loop;
```

### 13. Señales frente a variables

| | Señal (`signal`) | Variable (`variable`) |
|---|---|---|
| Sintaxis de asignación | `destino <= fuente` | `destino := fuente` |
| Utilidad | Modela un **cable** físico del circuito | Almacenamiento **local** temporal |
| Visibilidad | **Global**: comunica puertos y procesos entre sí | **Local**: solo dentro del proceso donde se declara |
| Actualización | **Diferida**: recién tiene efecto cuando avanza el tiempo (el proceso se suspende) | **Inmediata** |

Este detalle no es un tecnicismo menor: puede cambiar el resultado de un diseño. El siguiente
ejemplo (adaptado de la presentación) muestra un multiplexor con *latch* de habilitación mal
resuelto por usar una señal donde hacía falta el valor **ya actualizado**:

```vhdl
-- INCORRECTO: cuando en='1', a x se le asigna el valor PREVIO de c
architecture comp of mux2latch is
  signal c : std_logic;
begin
  mux: process (a, b, sel, en)
  begin
    if (sel = '0') then c <= a; else c <= b; end if;
    x <= (x and (not en)) or (c and en);  -- c todavía no se actualizó
  end process;
end comp;
```

Hay dos formas correctas de resolverlo: separar el proceso de la asignación concurrente, o usar una
**variable** (que sí se actualiza de inmediato):

```vhdl
-- CORRECTO con variable: la asignación a c es inmediata
architecture comp of mux2latch is
begin
  mux: process (a, b, sel, en)
    variable c : std_logic;
  begin
    if (sel = '0') then c := a; else c := b; end if;   -- inmediato
    x <= (x and (not en)) or (c and en);                -- ya ve el c nuevo
  end process;
end comp;
```

### 14. Constantes y objetos disponibles en VHDL

- **Constante**: asocia un nombre a un valor fijo. Ej.: `constant pi : real := 3.1416;`
- **Variable**: almacenamiento local temporal, visible solo dentro de un proceso, con asignación
  inmediata (`:=`). Ej.: `variable parada : std_logic := '0';`
- **Señal**: modela un cable, con asignación diferida (`<=`). Ej.: `signal parada : std_logic <= '0';`

### 15. Estilos de modelado

Una misma función puede describirse en VHDL con distintos **estilos**, independientemente del nivel
de abstracción. El siguiente ejemplo (un comparador de igualdad de 1 bit, $C = 1 \iff A=B$) muestra
los tres estilos clásicos:

**Algorítmico** (proceso con sentencias secuenciales, similar a un programa):

```vhdl
entity comparador is
  port (A, B : in bit; C : out bit);
end comparador;

architecture algoritmico of comparador is
begin
  process
  begin
    if (A = B) then
      C <= '1';
    else
      C <= '0';
    end if;
    wait on A, B;
  end process;
end algoritmico;
```

**Flujo de datos** (*dataflow*, ecuaciones concurrentes que reflejan dependencias entre señales):

```vhdl
entity comparador is
  port (A, B : in bit; C : out bit);
end comparador;

architecture dataflow of comparador is
begin
  C <= (A and B) or (not A and not B);
end dataflow;
```

**Estructural** (la unidad se arma a partir de componentes de nivel inferior y sus conexiones):

```vhdl
entity comparador is
  port (A, B : in bit; C : out bit);
end comparador;

architecture structural of comparador is
  component XOR2
    port (O : out bit; I1, I2 : in bit);
  end component;
  component INV
    port (O : out bit; I : in bit);
  end component;
  signal S : bit;
begin
  C1: XOR2 port map (O => S, I1 => A, I2 => B);
  C2: INV  port map (O => C, I => S);
end structural;
```

| Nivel de abstracción | Estilos de modelado típicos |
|---|---|
| Comportamental / Funcional | Algorítmico |
| RTL | Flujo de datos, algorítmico |
| Lógico (compuertas) | Estructural |

### 16. Paquetes y librerías

Un **paquete** (`PACKAGE`) es una forma de almacenar y compartir información entre distintos
diseños. Se compone de una **declaración** (obligatoria: tipos, subprogramas) y un **cuerpo**
(opcional: definición de esos subprogramas). Ejemplo:

```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.all;

PACKAGE filt_cmp IS
  TYPE state_type IS (idle, tap1, tap2, tap3, tap4);
  COMPONENT acc
    port (xh          : in  std_logic_vector(10 downto 0);
          clk, first  : in  std_logic;
          yn          : out std_logic_vector(11 downto 4));
  END COMPONENT;
  FUNCTION compare (SIGNAL a, b : integer) RETURN boolean;
END filt_cmp;

PACKAGE BODY filt_cmp IS
  FUNCTION compare (SIGNAL a, b : integer) RETURN boolean IS
    VARIABLE temp : boolean;
  BEGIN
    IF a < b THEN
      temp := true;
    ELSE
      temp := false;
    END IF;
    RETURN temp;
  END compare;
END filt_cmp;
```

Una **librería** contiene un paquete o una colección de paquetes. La librería estándar `STD`
incluye el paquete `STANDARD` (tipos `bit`, `boolean`, `integer`, `real`, `time` y sus operadores) y
el paquete `TEXTIO` (funciones de acceso a archivos, ver sección 23). La librería `work` es aquella
donde se compilan (o sintetizan) los módulos propios del proyecto.

## Parte II: Diseño y verificación

### 17. Multiplexores en VHDL

Retomando el multiplexor de la Parte I, VHDL ofrece varias formas equivalentes de describirlo. Con
**asignación concurrente**:

```vhdl
x <= (a and not sel) or (b and sel);        -- por ecuación booleana
x <= a when sel = '0' else b;                -- condicional simple
with sel select
  x <= a when '0',
       b when '1',
       '0' when others;                      -- por selección
```

Con **sentencias secuenciales**, un mux de 4 a 1 con prioridad (`if`) o sin prioridad (`case`):

```vhdl
-- con prioridad
process (selc, selb, a, b, c)
begin
  if (selc = '1') then x <= c;
  elsif (selb = '1') then x <= b;
  else x <= a;
  end if;
end process;

-- sin prioridad
process (sel, a, b, c, d)
begin
  case sel is
    when "00"   => x <= a;
    when "01"   => x <= b;
    when "10"   => x <= c;
    when others => x <= d;
  end case;
end process;
```

### 18. Registros y flip-flops en VHDL

Existen dos métodos para crear flip-flops en VHDL: **instanciar** un componente de flip-flop desde
una librería, o describirlo mediante un **proceso sensible al flanco de reloj**.

**Instanciación de componente:**

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity ffd is
  port (d, clk : in std_logic; q : out std_logic);
end ffd;

use ieee.rtlpkg.all;
architecture instffd of ffd is
begin
  flipflop: dff port map (d, clk, q);  -- componente dff de rtlpkg
end instffd;
```

**Descripción basada en proceso:**

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity ffd is
  port (d, clk : in std_logic; q : out std_logic);
end ffd;

architecture compffd of ffd is
begin
  flipflop: process (clk)
  begin
    if (clk'event and clk = '1') then
      q <= d;
    end if;
  end process;
end compffd;
```

```{important}
El sintetizador **infiere** que hay que crear un registro para `q` a partir de dos pistas del
código: (1) el proceso es sensible **únicamente** a la señal de reloj, y la condición
`clk'event and clk='1'` implica que la asignación ocurre en el **flanco de subida** — eso indica un
elemento síncrono; y (2) el `IF` está **incompleto** (no tiene `ELSE`): si no hay flanco de subida,
`q` debe **mantener su valor** hasta la próxima asignación. Esa "memoria implícita" es exactamente
lo que hace un flip-flop D (ver [Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md)).
```

### 19. Tipos de registro en código

Cuatro variantes del flip-flop D, según lleve o no señales de inicialización y de qué tipo:

```vhdl
-- Flip-flop D simple
ff: process (clk)
begin
  if (clk'event and clk = '1') then
    output <= input;
  end if;
end process;

-- Flip-flop D con set asíncrono
ff_SA: process (clk, st)
begin
  if (st = '1') then
    output <= (others => '1');
  elsif (clk'event and clk = '1') then
    output <= input;
  end if;
end process;

-- Flip-flop D con reset síncrono
ff_RS: process (clk)
begin
  if (clk'event and clk = '1') then
    if (rst = '1') then
      output <= (others => '0');
    else
      output <= input;
    end if;
  end if;
end process;

-- Flip-flop D con reset asíncrono
ff_RA: process (clk, rst)
begin
  if (rst = '1') then
    output <= (others => '0');
  elsif (clk'event and clk = '1') then
    output <= input;
  end if;
end process;
```

| Variante | ¿Sensible a la señal de init? | ¿Cuándo actúa la inicialización? |
|---|:---:|---|
| D simple | No | Nunca (no tiene) |
| D con *set* asíncrono | Sí (`st`) | Inmediatamente, sin esperar flanco de reloj |
| D con reset síncrono | No (solo `clk`) | Solo en el flanco de reloj, si `rst='1'` |
| D con reset asíncrono | Sí (`rst`) | Inmediatamente, sin esperar flanco de reloj |

La diferencia entre reset **síncrono** y **asíncrono** es exactamente la diferencia entre estar o no
en la lista de sensibilidad del proceso: si la señal de reset está en la lista de sensibilidad y se
evalúa fuera/antes de la condición de flanco, es asíncrona; si solo se evalúa dentro del `if` de
flanco, es síncrona.

### 20. Contador en VHDL

```vhdl
PCont: process (clk, rst)
begin
  if (rst = '1') then
    cont <= (others => '0');
  elsif (clk'event and clk = '1') then
    cont <= cont + 1;
  end if;
end process;
```

Esta descripción de tres líneas efectivas es la versión en VHDL del contador síncrono desarrollado
en detalle (con su derivación bit a bit) en [Circuitos contadores](19-circuitos-contadores.md).

### 21. Diseño jerárquico

El diseño jerárquico consiste en construir componentes grandes a partir de componentes más
pequeños ya verificados. Es fundamental para la **reutilización de código**, permite mezclar
componentes descriptos con distintos métodos (VHDL, Verilog, esquemáticos), y es indispensable en
estrategias de diseño *top-down* o *bottom-up*.

Antes de instanciar un componente hay que **declararlo** (sus puertos con `PORT`, y opcionalmente
parámetros con `GENERIC`). Una vez instanciado, sus puertos se conectan a señales del circuito con
`PORT MAP`, por **posición** o por **nombre**. La declaración de componentes puede colocarse en un
`PACKAGE` para no repetirla en cada archivo.

Ejemplo completo: un `mux4to1` construido jerárquicamente a partir de tres `mux2to1`:

```vhdl
-- Componente de nivel inferior
entity mux2to1 is
  port (i0, i1, s : in std_logic; o : out std_logic);
end mux2to1;

architecture archmux2to1 of mux2to1 is
begin
  o <= (i0 and not s) or (i1 and s);
end archmux2to1;

-- Paquete con la declaración del componente
package mymuxpkg is
  component mux2to1
    port (i0, i1, s : in std_logic; o : out std_logic);
  end component;
end mymuxpkg;

-- Top-level: mux4to1 construido con tres mux2to1 (igual al árbol visto en
-- Multiplexores y demultiplexores)
entity mux4to1 is
  port (a, b, c, d : in std_logic;
        sel         : in std_logic_vector(1 downto 0);
        o           : out std_logic);
end mux4to1;

use work.mymuxpkg.all;
architecture InstComp of mux4to1 is
  signal r : std_logic_vector(1 downto 0);
begin
  mux0: mux2to1 port map (i0 => a, i1 => b, s => sel(0), o => r(0));  -- por nombre
  mux1: mux2to1 port map (i0 => c, i1 => d, s => sel(0), o => r(1));  -- por nombre
  mux2: mux2to1 port map (r(0), r(1), sel(1), o);                     -- por posición
end InstComp;
```

Este `mux4to1` es exactamente la implementación jerárquica en árbol que se desarrolló con diagramas
ASCII en [Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md): dos `MUX2_1` en
el primer nivel y uno en el segundo.

### 22. Verificación con testbenches

Un diseño **sin verificar no está completo**. La forma más habitual de verificar un diseño VHDL es
mediante un **testbench**: un código VHDL cuyo único propósito es **generar estímulos** y
**observar resultados** sobre el diseño bajo prueba (llamado **UUT**, *Unit Under Test*). Los
testbenches **no se sintetizan** — pueden usar VHDL puramente algorítmico y secuencial sin
restricciones de sintetizabilidad.

Estructura general de un testbench:

1. Instanciar el diseño a verificar (la UUT). El testbench pasa a ser el nuevo *top-level*, y es una
   entidad **sin puertos**.
2. Generar los estímulos de entrada.
3. Observar (comprobar) los resultados.
4. Informar al usuario si algo falló.

Para generar estímulos, a diferencia de la síntesis (donde el tiempo no tiene sentido físico), en un
testbench **el tiempo es el concepto central**:

```vhdl
-- Asignación secuencial con wait
s <= '1';
wait for 20 ns; s <= '0';
wait for 30 ns; s <= '1';

-- Asignación concurrente equivalente
s <= '1', '0' after 20 ns, '1' after 30 ns;
```

Para observar resultados se usa la sentencia **`assert`**, equivalente a `if (not condicion) then ...`:

```vhdl
assert <condicion> report <cadena_de_texto> severity <nivel>;
```

Los niveles de `severity` posibles son:

| Nivel | Significado |
|---|---|
| `NOTE` | Aviso informativo |
| `WARNING` | Advertencia |
| `ERROR` | Error (nivel por defecto si se omite `severity`) |
| `FAILURE` | Falla grave |

El **algoritmo básico** de un testbench es: dar valores a las entradas de la UUT → esperar con
`wait for` → comprobar el resultado con `assert` → repetir. Ejemplo completo de testbench para un
flip-flop D:

```vhdl
entity dff_tb is
end dff_tb;

architecture tb_arch of dff_tb is
  component dff
    port (d, clk : in std_logic; q : out std_logic);
  end component;
  signal d, c, q : std_logic;
begin
  uut: dff port map (d => d, clk => c, q => q);

  process
  begin
    c <= '0'; d <= '0';
    wait for 10 ns;
    c <= '1';
    wait for 10 ns;
    assert q = d report "falla" severity failure;
  end process;
end tb_arch;
```

### 23. Acceso a archivos

Las simulaciones más avanzadas trabajan sobre archivos: por ejemplo, un testbench de un
multiplicador que escribe sus resultados a un archivo de texto, o un testbench de un
microprocesador que lee un programa ensamblador desde un archivo, lo ensambla y lo ejecuta.

El acceso básico a archivos de texto se hace con el paquete **`std.textio`** (acceso línea a línea
con `readline`/`writeline`, y campo a campo dentro de una línea con `read`/`write`), y existe una
versión específica para `std_logic` en **`ieee.std_logic_textio`**.

```vhdl
file archivo_estimulos : text is in "Stim.txt";
variable linea : line;
variable opcode : string(2 downto 0);
...
readline(archivo_estimulos, linea);   -- lee una línea
read(linea, opcode);                  -- lee un campo de esa línea
...
write(linea, resultado);              -- escribe un campo
writeline(archivo_resultados, linea); -- escribe la línea completa
```

El siguiente paso natural, una vez que un diseño VHDL está descrito y verificado, es **sintetizarlo**
sobre un dispositivo real — ver [Lógica programable](23-logica-programable.md).

## 24. Resumen

- **VHDL** (VHSIC Hardware Description Language) es un lenguaje estandarizado por IEEE en 1987 para
  documentar, simular y sintetizar circuitos digitales, con un paradigma de **ejecución concurrente**
  muy distinto al de un lenguaje de programación de software.
- Todo diseño se compone de una **entidad** (interfaz: puertos con modo `IN`/`OUT`/`BUFFER`/`INOUT`
  y tipo) y una **arquitectura** (implementación interna).
- El tipo **`std_logic`** (con sus 9 valores) y `std_logic_vector` son el estándar de facto para
  modelar señales digitales reales, por encima de `bit`/`bit_vector`.
- Dentro de una arquitectura conviven **procesos** (secuenciales puertas adentro, concurrentes entre
  sí) y **asignaciones/instanciaciones concurrentes**. Las **señales** se actualizan de forma
  diferida y las **variables** de forma inmediata — una distinción que puede cambiar el resultado
  del diseño.
- Un mismo circuito admite estilos de modelado **algorítmico**, **de flujo de datos** y
  **estructural**, y niveles de abstracción **comportamental**, **RTL** y **lógico**.
- Un proceso sensible solo al reloj, con un `IF` de flanco **incompleto** (sin `ELSE`), es la forma
  estándar en que VHDL infiere un **registro** (flip-flop); agregar señales de *set*/reset dentro o
  fuera de esa condición determina si son síncronas o asíncronas.
- El **diseño jerárquico** (declaración de componentes, `PORT MAP` por posición o por nombre,
  paquetes) permite construir bloques grandes reutilizando bloques chicos ya verificados.
- Todo diseño debe verificarse con un **testbench**: código VHDL no sintetizable que instancia la
  UUT, genera estímulos temporizados y comprueba resultados con `assert`/`report`/`severity`.

## 25. Bibliografía

```{bibliography}
:filter: docname in docnames
```

## 26. Ejercicios propuestos

```{exercise}
:label: ex-hdl-1
Escribir la entidad y la arquitectura (estilo de flujo de datos) de una compuerta XOR de 2 entradas
en VHDL, usando el tipo `std_logic`.
```

````{solution} ex-hdl-1
:class: dropdown
```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity xor2 is
  port (a, b : in std_logic; o : out std_logic);
end xor2;

architecture dataflow of xor2 is
begin
  o <= a xor b;
end dataflow;
```
````

````{exercise}
:label: ex-hdl-2
Explicar, en términos de la lista de sensibilidad y de la estructura del `IF`, por qué el siguiente
proceso sintetiza un **latch** en lugar de un flip-flop:

```vhdl
process (en, d)
begin
  if (en = '1') then
    q <= d;
  end if;
end process;
```
````

```{solution} ex-hdl-2
:class: dropdown
El proceso es sensible a `en` y a `d` (no solo a un reloj), y el `IF` no tiene `ELSE`: cuando
`en='1'` la salida sigue a `d` en todo momento (transparencia), y cuando `en='0'` mantiene su
último valor. Esa es exactamente la definición de un *latch* D con habilitación (ver
[Circuitos secuenciales](17-circuitos-secuenciales-asincronicos-y-sincronicos.md)), no de un
flip-flop sensible a flanco.
```

```{exercise}
:label: ex-hdl-3
Escribir el proceso VHDL de un flip-flop D con **reset asíncrono activo en bajo** (es decir, resetea
cuando `rst_n = '0'`).
```

````{solution} ex-hdl-3
:class: dropdown
```vhdl
process (clk, rst_n)
begin
  if (rst_n = '0') then
    q <= '0';
  elsif (clk'event and clk = '1') then
    q <= d;
  end if;
end process;
```
La única diferencia respecto al reset asíncrono activo en alto es la condición (`rst_n = '0'` en
vez de `rst = '1'`); sigue siendo asíncrono porque `rst_n` está en la lista de sensibilidad.
````

```{exercise}
:label: ex-hdl-4
Instanciar dos veces el componente `mux2to1` de la sección 21 (por nombre) para armar un
`mux2to1` de 4 bits en paralelo (es decir, un `MUX2_4`, ver [Multiplexores y demultiplexores](15-multiplexores-y-demultiplexores.md)).
```

````{solution} ex-hdl-4
:class: dropdown
No se necesitan dos instancias sino **cuatro** (una por bit), todas comandadas por la misma señal de
selección `s`, replicando exactamente la idea de `MUX2_8` del capítulo 15 pero con buses de 4 bits:

```vhdl
entity mux2_4 is
  port (x, y : in std_logic_vector(3 downto 0);
        s    : in std_logic;
        o    : out std_logic_vector(3 downto 0));
end mux2_4;

use work.mymuxpkg.all;
architecture struct of mux2_4 is
begin
  bit0: mux2to1 port map (i0 => x(0), i1 => y(0), s => s, o => o(0));
  bit1: mux2to1 port map (i0 => x(1), i1 => y(1), s => s, o => o(1));
  bit2: mux2to1 port map (i0 => x(2), i1 => y(2), s => s, o => o(2));
  bit3: mux2to1 port map (i0 => x(3), i1 => y(3), s => s, o => o(3));
end struct;
```
````

```{exercise}
:label: ex-hdl-5
Escribir un testbench mínimo para el `xor2` del ejercicio 1, que pruebe las 4 combinaciones de
entrada y reporte una falla si alguna no coincide con el resultado esperado.
```

````{solution} ex-hdl-5
:class: dropdown
```vhdl
entity xor2_tb is
end xor2_tb;

architecture tb of xor2_tb is
  component xor2
    port (a, b : in std_logic; o : out std_logic);
  end component;
  signal a, b, o : std_logic;
begin
  uut: xor2 port map (a => a, b => b, o => o);

  process
  begin
    a <= '0'; b <= '0'; wait for 10 ns;
    assert o = '0' report "falla 0 xor 0" severity failure;
    a <= '0'; b <= '1'; wait for 10 ns;
    assert o = '1' report "falla 0 xor 1" severity failure;
    a <= '1'; b <= '0'; wait for 10 ns;
    assert o = '1' report "falla 1 xor 0" severity failure;
    a <= '1'; b <= '1'; wait for 10 ns;
    assert o = '0' report "falla 1 xor 1" severity failure;
    wait;
  end process;
end tb;
```
````

```{exercise}
:label: ex-hdl-6
¿Por qué un testbench puede usar construcciones que no son sintetizables (por ejemplo, `wait for
20 ns` sin condición de reactivación)?
```

```{solution} ex-hdl-6
:class: dropdown
Porque el testbench nunca se convierte en hardware: es una herramienta de **simulación**, no de
síntesis. Su único propósito es generar estímulos y comprobar resultados sobre la UUT dentro del
simulador; por eso puede usar tiempo explícito, tipos no sintetizables (`real`, `time`) y sentencias
como `assert`/`report` que no tienen sentido en un circuito físico.
```
