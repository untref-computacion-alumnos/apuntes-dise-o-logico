#!/usr/bin/env python3
"""Genera el cuerpo TikZ de un PLA dibujado como matriz de puntos.

Uso desde Python:

    from pla import pla_tikz
    tex = pla_tikz(
        entradas=["a", "b", "w"],
        productos=[("a'b'w", "011"), ...],   # (etiqueta, código por entrada)
        salidas=[("r_1", [0, 1, 3]), ...],  # (nombre, índices de productos)
    )

Código por entrada en cada producto: "1" = variable directa, "0" = negada,
"-" = no participa (lo mismo que la codificación 10 / 01 / 00 del apunte).
"""


def pla_tikz(entradas, productos, salidas, titulo=None, max_productos=None):
    n = len(entradas)
    dx = 0.7  # separación de líneas verticales
    dy = 0.6  # separación de productos
    x_and = [(i * 2 * dx, i * 2 * dx + dx) for i in range(n)]  # (directa, negada)
    ancho_and = 2 * n * dx
    filas = max_productos or len(productos)
    x_or0 = ancho_and + 1.0
    lineas = ["\\begin{tikzpicture}"]
    top = 0.9
    bottom = -(filas) * dy
    # planos
    lineas.append(
        f"\\fill[acentosuave, rounded corners=2pt] (-0.35,{top-0.2:.2f}) rectangle ({ancho_and-0.35:.2f},{bottom-0.1:.2f});"
    )
    lineas.append(
        f"\\fill[oksuave, rounded corners=2pt] ({x_or0-0.35:.2f},{top-0.2:.2f}) rectangle ({x_or0+len(salidas)*dx*1.4-0.35:.2f},{bottom-0.1:.2f});"
    )
    lineas.append(f"\\node[font=\\scriptsize\\bfseries, text=acento] at ({ancho_and/2-0.35:.2f},{bottom-0.4:.2f}) {{plano AND}};")
    lineas.append(
        f"\\node[font=\\scriptsize\\bfseries, text=ok] at ({x_or0+len(salidas)*dx*0.7-0.35:.2f},{top+0.1:.2f}) {{plano OR}};"
    )
    # entradas
    for i, e in enumerate(entradas):
        xd, xn = x_and[i]
        lineas.append(f"\\draw ({xd:.2f},{top+0.9:.2f}) node[above] {{${e}$}} -- ({xd:.2f},{bottom:.2f});")
        lineas.append(f"\\draw ({xd:.2f},{top+0.5:.2f}) -| ({xn:.2f},{top+0.25:.2f});")
        lineas.append(f"\\fill ({xd:.2f},{top+0.5:.2f}) circle (1.3pt);")
        lineas.append(
            f"\\node[not port, rotate=-90, scale=0.45, anchor=in] at ({xn:.2f},{top+0.25:.2f}) {{}};"
        )
        lineas.append(f"\\draw ({xn:.2f},{top-0.25:.2f}) -- ({xn:.2f},{bottom:.2f});")
    # productos
    for j in range(filas):
        y = -j * dy
        lineas.append(f"\\draw[gris] (-0.25,{y:.2f}) -- ({x_or0+len(salidas)*dx*1.4-0.45:.2f},{y:.2f});")
        if j < len(productos):
            etq, cod = productos[j]
            lineas.append(f"\\node[font=\\scriptsize, anchor=east] at (-0.3,{y:.2f}) {{$p_{{{j+1}}} = {etq}$}};")
            for i, c in enumerate(cod):
                if c == "-":
                    continue
                x = x_and[i][0] if c == "1" else x_and[i][1]
                lineas.append(f"\\fill[acento] ({x:.2f},{y:.2f}) circle (2.2pt);")
        else:
            lineas.append(f"\\node[font=\\scriptsize, anchor=east, text=gris] at (-0.3,{y:.2f}) {{$p_{{{j+1}}}$ (sin usar)}};")
    # salidas
    for k, (nombre, usados) in enumerate(salidas):
        x = x_or0 + k * dx * 1.4
        lineas.append(f"\\draw ({x:.2f},{top-0.2:.2f}) -- ({x:.2f},{bottom-0.7:.2f}) node[below] {{${nombre}$}};")
        for j in usados:
            lineas.append(f"\\fill[ok] ({x:.2f},{-j*dy:.2f}) circle (2.2pt);")
    if titulo:
        lineas.append(f"\\node[font=\\small\\bfseries, anchor=south west] at (-3.4,{top+1.5:.2f}) {{{titulo}}};")
    lineas.append("\\end{tikzpicture}")
    return "\n".join(lineas) + "\n"
