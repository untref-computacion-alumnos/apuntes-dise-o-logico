#!/usr/bin/env python3
"""Genera las figuras (SVG) y los PDF de los exámenes resueltos.

Uso (desde cualquier directorio):

    python3 contenidos/materiales/examenes/resueltos/_fuentes/build.py [examen ...]

Sin argumentos procesa todos los exámenes. Con argumentos procesa solo los
indicados (por ejemplo: final-2026-02-20).

Requiere: lualatex (con circuitikz y karnaugh-map), pdftocairo (poppler) y
pandoc >= 3. La ruta de pandoc se puede indicar con la variable PANDOC.
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FUENTES = Path(__file__).resolve().parent
RESUELTOS = FUENTES.parent
FIG_SRC = FUENTES / "figuras"
FIG_SVG = RESUELTOS / "figuras"
CACHE = FUENTES / "build"  # PDFs de las figuras (ignorado por git)
PDF_OUT = RESUELTOS / "pdf"
PANDOC = os.environ.get("PANDOC", "pandoc")


def compilar_figura(src: Path) -> None:
    examen = src.parent.name
    pdf = CACHE / examen / (src.stem + ".pdf")
    svg = FIG_SVG / examen / (src.stem + ".svg")
    preambulo = FUENTES / "figura-preambulo.tex"
    if (
        svg.exists()
        and pdf.exists()
        and pdf.stat().st_mtime > max(src.stat().st_mtime, preambulo.stat().st_mtime)
    ):
        return
    pdf.parent.mkdir(parents=True, exist_ok=True)
    svg.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        tex = Path(tmp) / "fig.tex"
        tex.write_text(
            preambulo.read_text()
            + "\n\\begin{document}\n"
            + src.read_text()
            + "\n\\end{document}\n"
        )
        r = subprocess.run(
            ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "fig.tex"],
            cwd=tmp,
            capture_output=True,
            text=True,
        )
        if r.returncode != 0:
            log = (Path(tmp) / "fig.log").read_text(errors="replace")
            err = [l for l in log.splitlines() if l.startswith("!")]
            idx = log.find("\n!")
            sys.exit(f"Error compilando {src}:\n" + log[idx : idx + 1500] if idx >= 0 else "\n".join(err))
        shutil.copy(Path(tmp) / "fig.pdf", pdf)
    subprocess.run(["pdftocairo", "-svg", str(pdf), str(svg)], check=True)
    print(f"  figura {examen}/{svg.name}")


def compilar_pdf(md: Path) -> None:
    salida = PDF_OUT / (md.stem + ".pdf")
    PDF_OUT.mkdir(exist_ok=True)
    cmd = [
        PANDOC,
        md.name,
        "--from=markdown+tex_math_dollars+pipe_tables+implicit_figures-yaml_metadata_block",
        "--pdf-engine=lualatex",
        "--lua-filter",
        str(FUENTES / "filtro.lua"),
        "--include-in-header",
        str(FUENTES / "estilo.tex"),
        "--syntax-highlighting=default",
        "-V", "documentclass=article",
        "-V", "papersize=a4",
        "-V", "geometry=margin=2.1cm",
        "-V", "fontsize=11pt",
        "-V", "colorlinks=true",
        "-V", "linkcolor=acento",
        "-V", "urlcolor=acento",
        "-V", "toc-depth=1",
        "--toc",
        "-o",
        str(salida),
    ]
    r = subprocess.run(cmd, cwd=RESUELTOS, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Error generando {salida.name}:\n{r.stderr[-3000:]}")
    if r.stderr.strip():
        print(r.stderr.strip())
    print(f"  pdf {salida.name}")


def main() -> None:
    pedidos = sys.argv[1:]
    # Primero todas las figuras: algunos exámenes reutilizan figuras de otros.
    for src in sorted(FIG_SRC.glob("*/*.tex")):
        compilar_figura(src)
    for md in sorted(RESUELTOS.glob("*-resuelto.md")):
        examen = md.stem.removesuffix("-resuelto")
        if pedidos and examen not in pedidos:
            continue
        compilar_pdf(md)


if __name__ == "__main__":
    main()
