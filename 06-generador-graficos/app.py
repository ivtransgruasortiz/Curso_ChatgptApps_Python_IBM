from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
import matplotlib.ticker as mtick

app = Flask(__name__)

# Datos de inflación media (aproximados)
datos = {
    "Año": list(range(2005, 2025)),
    "España":  [3.4, 3.5, 2.8, 4.1, -0.3, 1.8, 3.1, 2.4, 1.4, -1.0,
                -0.5, 1.6, 1.2, 1.7, 0.7, -0.3, 3.1, 8.4, 3.5, 3.2],
    "Alemania": [1.9, 1.7, 2.3, 2.6, 0.3, 1.1, 2.3, 2.0, 1.5, 0.2,
                 0.3, 0.5, 1.6, 1.8, 1.4, 0.5, 3.2, 7.9, 5.9, 2.8],
    "Italia": [2.2, 2.2, 1.8, 3.5, 0.8, 1.5, 2.9, 3.0, 1.3, -0.1,
               0.1, -0.1, 1.2, 1.3, 0.6, -0.2, 1.9, 8.7, 5.7, 2.9],
    "Grecia": [3.5, 3.2, 2.9, 4.2, 1.2, 4.7, 3.3, 1.0, -1.3, -1.7,
               -1.4, 0.0, 1.1, 0.6, 0.5, -1.3, 1.2, 9.6, 4.3, 3.4],
}

df = pd.DataFrame(datos)

@app.route("/")
def index():
    fig, ax = plt.subplots(figsize=(11, 6))

    # Estilo profesional: colores consistentes
    colores = {
        "España": "#ff7f0e",
        "Alemania": "#1f77b4",
        "Italia": "#2ca02c",
        "Grecia": "#d62728"
    }

    for pais in ["España", "Alemania", "Italia", "Grecia"]:
        ax.plot(df["Año"], df[pais], marker='o', label=pais, linewidth=2, color=colores[pais])

    # Formato y estética
    ax.set_title("Inflación Media (2005–2024)", fontsize=16, weight='bold')
    ax.set_xlabel("Año", fontsize=12)
    ax.set_ylabel("Inflación (%)", fontsize=12)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=1))
    ax.set_xticks(df["Año"][::2])
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(title="País", loc="upper left")

    # Guardar imagen en base64
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', dpi=100)
    plt.close(fig)
    buf.seek(0)
    grafico_base64 = base64.b64encode(buf.read()).decode('utf-8')

    return render_template("index.html", grafico=grafico_base64)

if __name__ == "__main__":
    try:
        # app.run(debug=True)
        app.run(host='127.0.0.1', port=8800, debug=True)
    except OSError as e:
        print("Error: El puerto 5000 está en uso o bloqueado.")
