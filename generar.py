import sys
import datetime

# Recibe los números desde GitHub Actions
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
resultado = num1 + num2
fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

# Genera el HTML con el resultado incrustado
html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Resultado: {num1} + {num2}</title>
  <style>
    body {{ font-family: system-ui, sans-serif; text-align: center; padding: 60px 20px; background: #0f172a; color: #e2e8f0; }}
    .card {{ background: #1e293b; padding: 35px; border-radius: 16px; display: inline-block; box-shadow: 0 8px 30px rgba(0,0,0,0.4); }}
    h1 {{ margin: 0 0 15px; color: #38bdf8; }}
    .op {{ font-size: 22px; margin-bottom: 10px; }}
    .res {{ font-size: 56px; font-weight: 800; color: #4ade80; margin: 15px 0; }}
    .meta {{ color: #64748b; font-size: 13px; margin-top: 15px; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>🐍 Python calculó</h1>
    <div class="op">{num1} + {num2}</div>
    <div class="res">= {resultado}</div>
    <div class="meta">Generado con GitHub Actions el {fecha}</div>
  </div>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"✅ index.html generado: {num1} + {num2} = {resultado}")