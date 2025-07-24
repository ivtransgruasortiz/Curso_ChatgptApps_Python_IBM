from flask import Flask, render_template, request, jsonify
import pyttsx3
import threading

app = Flask(__name__)


def speak_text(text):
    engine = pyttsx3.init()

    # Establecer voz en español si está disponible
    for voice in engine.getProperty('voices'):
        if 'spanish' in voice.name.lower() or 'es_' in voice.id.lower():
            engine.setProperty('voice', voice.id)
            engine.setProperty('rate', 125)
            break

    engine.say(text)
    engine.runAndWait()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get('text', '')
    thread = threading.Thread(target=speak_text, args=(text,))
    thread.start()
    return jsonify({"status": "started"})


# Bloque de ejecución
if __name__ == '__main__':
    app.run(debug=True)
