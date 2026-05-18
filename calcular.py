import datetime

resultado = 2 + 2
ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Resultado Python</title>
  <style>
    body {{ font-family: system-ui, sans-serif; text-align: center; padding: 50px 20px; background: #0f172a; color: #e2e8f0; }}
    h1 {{ color: #38bdf8; }}
    .result {{ font-size: 64px; font-weight: 800; margin: 20px 0; }}
    .date {{ color: #94a3b8; font-size: 14px; }}
  </style>
</head>
<body>
  <h1>🐍 Python calculó: 2 + 2</h1>
  <div class="result">{resultado}</div>
  <p class="date">Generado automáticamente el {ahora}</p>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("✅ index.html generado correctamente")