-- Filtro de pandoc para los PDF de exámenes resueltos.
--  * El primer título de nivel 1 pasa a ser el título del documento y el resto
--    de los títulos sube un nivel (## Ejercicio -> \section).
--  * Las figuras SVG se reemplazan por su versión PDF (vectorial) generada por
--    build.py en _fuentes/build/.
--  * Las citas en bloque se convierten en recuadros según su primera palabra en
--    negrita: Enunciado, Dónde está en el apunte, Ojo, Supuesto; el resto, idea.

local titulo_tomado = false

local cajas = {
  { "^Enunciado", "cajaenunciado" },
  { "^Dónde", "cajafuente" },
  { "^Apunte", "cajafuente" },
  { "^Ojo", "cajaojo" },
  { "^Supuesto", "cajasupuesto" },
  { "^Respuesta", "cajarespuesta" },
}

function Pandoc(doc)
  local bloques = {}
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 and not titulo_tomado then
      doc.meta.title = pandoc.MetaInlines(b.content)
      titulo_tomado = true
    else
      if b.t == "Header" then
        b.level = math.max(1, b.level - 1)
        -- cada ejercicio empieza en una página nueva
        if b.level == 1 then
          table.insert(bloques, pandoc.RawBlock("latex", "\\clearpage"))
        end
      end
      table.insert(bloques, b)
    end
  end
  doc.blocks = bloques
  return doc
end

function Image(img)
  local examen, nombre = img.src:match("^figuras/([^/]+)/([^/]+)%.svg$")
  if examen then
    img.src = "_fuentes/build/" .. examen .. "/" .. nombre .. ".pdf"
  end
  return img
end

function BlockQuote(bq)
  local primero = bq.content[1]
  local entorno = "cajaidea"
  if primero and (primero.t == "Para" or primero.t == "Plain") then
    local ini = primero.content[1]
    if ini and ini.t == "Strong" then
      local texto = pandoc.utils.stringify(ini)
      for _, c in ipairs(cajas) do
        if texto:match(c[1]) then
          entorno = c[2]
          break
        end
      end
    end
  end
  local out = { pandoc.RawBlock("latex", "\\begin{" .. entorno .. "}") }
  for _, b in ipairs(bq.content) do
    table.insert(out, b)
  end
  table.insert(out, pandoc.RawBlock("latex", "\\end{" .. entorno .. "}"))
  return out
end
