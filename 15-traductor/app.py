from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    original_text = ""
    translations = {"en": "", "fr": "", "it": "", "de": ""}
    if request.method == "POST":
        original_text = request.form.get("text_es", "")
        if original_text.strip():
            for lang in translations.keys():
                try:
                    translated = GoogleTranslator(source='es', target=lang).translate(original_text)
                    translations[lang] = translated
                except Exception as e:
                    translations[lang] = f"Error: {str(e)}"
    return render_template("index.html", original_text=original_text, translations=translations)

if __name__ == "__main__":
    app.run(debug=True)
