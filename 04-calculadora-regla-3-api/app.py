from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            if a == 0:
                error = "El valor de A no puede ser cero."
            else:
                resultado = (b * c) / a

        except ValueError:
            error = "Introduce solo números válidos."

    return render_template('index.html', resultado=resultado, error=error)

if __name__ == '__main__':
    try:
        app.run(debug=True)
        # app.run(host='127.0.0.1', port=8500, debug=True)
    except OSError as e:
        print("Error: El puerto 5000 está en uso o bloqueado.")