from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'messages.json'


# Cargar mensajes desde el fichero JSON
def load_messages():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


# Guardar mensajes en el fichero JSON
def save_messages(messages):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()
        if name and message:
            messages = load_messages()
            messages.append({
                'name': name,
                'message': message,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            save_messages(messages)
        return redirect('/')

    messages = load_messages()
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True)