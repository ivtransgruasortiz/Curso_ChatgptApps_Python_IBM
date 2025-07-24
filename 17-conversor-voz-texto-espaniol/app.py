import os
from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import speech_recognition as sr
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    translations = {"en": "", "fr": "", "it": "", "de": ""}

    if request.method == "POST":
        audio_file = request.files.get("audio_file")
        if audio_file:
            filename = secure_filename(audio_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            audio_file.save(filepath)

            recognizer = sr.Recognizer()
            with sr.AudioFile(filepath) as source:
                audio = recognizer.record(source)
                try:
                    transcript = recognizer.recognize_google(audio, language="es-ES")
                    for lang in translations.keys():
                        translations[lang] = GoogleTranslator(source='es', target=lang).translate(transcript)
                except sr.UnknownValueError:
                    transcript = "No se pudo reconocer el audio."
                except Exception as e:
                    transcript = f"Error: {str(e)}"

            os.remove(filepath)  # Limpieza del archivo subido

    return render_template("index.html", transcript=transcript, translations=translations)


if __name__ == "__main__":
    app.run(debug=True)
