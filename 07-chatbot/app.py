import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Reemplaza por tu clave directamente o usa variable de entorno
OPENAI_API_KEY = os.getenv("API_KEY")  # O sustituye por "sk-xxxxx..."
if not OPENAI_API_KEY:
    raise ValueError("La variable de entorno API_KEY no está definida.")

@app.route("/")
def index():
    return render_template("index.html")  # Asegúrate de que tienes este archivo

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("mensaje", "")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        completions = response.json()
        respuesta = completions["choices"][0]["message"]["content"].strip()
        return jsonify({"respuesta": respuesta})
    except requests.exceptions.RequestException as e:
        print("ERROR EN LA PETICIÓN A OPENAI:", e)
        if e.response is not None:
            print("CÓDIGO:", e.response.status_code)
            print("TEXTO:", e.response.text)
        return jsonify({"error": "Error al conectar con OpenAI."}), 500


if __name__ == "__main__":
    try:
        # app.run(debug=True)
        app.run(host='127.0.0.1', port=8900, debug=True)
    except OSError as e:
        print("Error: El puerto 5000 está en uso o bloqueado.")
