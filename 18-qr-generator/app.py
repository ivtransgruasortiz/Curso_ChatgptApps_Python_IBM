from flask import Flask, render_template, request, redirect, url_for
import qrcode
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/qr_codes'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        filename = f"qr_{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        qr = qrcode.make(url)
        qr.save(filepath)

        return redirect(url_for('result', filename=filename, url=url))
    return render_template('index.html')

@app.route('/result')
def result():
    filename = request.args.get('filename')
    url = request.args.get('url')
    return render_template('result.html', filename=filename, url=url)

if __name__ == '__main__':
    app.run(debug=True)
