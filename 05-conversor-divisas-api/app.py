import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
app = Flask(__name__)

# Lista de monedas admitidas (puedes ampliarla si lo deseas)
CURRENCIES = {
    "EUR": "Euro",
    "USD": "Dólar estadounidense",
    "JPY": "Yen japonés",
    "GBP": "Libra esterlina",
    "CHF": "Franco suizo",
    "CAD": "Dólar canadiense",
    "AUD": "Dólar australiano",
    "CNY": "Yuan chino",
    "MXN": "Peso mexicano",
    "BRL": "Real brasileño"
}

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    amount = ""
    from_currency = "EUR"
    to_currency = "USD"

    if request.method == "POST":
        from_currency = request.form.get("from")
        to_currency = request.form.get("to")
        amount = request.form.get("amount", "")

        try:
            amount_float = float(amount)
            url = "https://api.apilayer.com/exchangerates_data/convert"
            params = {
                "from": from_currency,
                "to": to_currency,
                "amount": amount_float
            }
            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            if response.status_code == 200 and "result" in data:
                resultado = round(data["result"], 2)
            else:
                error = "Error al obtener datos de la API."

        except ValueError:
            error = "Introduce una cantidad válida."

    return render_template(
        "index.html",
        resultado=resultado,
        error=error,
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
        currencies=CURRENCIES
    )

if __name__ == "__main__":
    app.run(debug=True)
