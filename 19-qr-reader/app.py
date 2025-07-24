from flask import Flask, render_template, Response, jsonify
import cv2
import threading
from pyzbar import pyzbar

app = Flask(__name__)

# Estado global
frame_lock = threading.Lock()
current_frame = None
latest_qr = ""

def camera_loop():
    global current_frame, latest_qr
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("❌ No se pudo abrir la cámara.")
        return

    while True:
        success, frame = cap.read()
        if not success or frame is None:
            continue

        decoded = pyzbar.decode(frame)
        with frame_lock:
            current_frame = frame.copy()
            if decoded:
                latest_qr = decoded[0].data.decode('utf-8')
            else:
                latest_qr = ""

    cap.release()

# Inicia el hilo de la cámara al inicio
threading.Thread(target=camera_loop, daemon=True).start()

@app.route('/')
def index():
    return render_template('stream.html')

@app.route('/video')
def video():
    def generate():
        while True:
            with frame_lock:
                if current_frame is None:
                    continue
                frame = current_frame.copy()
                text = latest_qr

            if text:
                cv2.putText(frame, f"QR: {text}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/qr_data')
def qr_data():
    with frame_lock:
        return jsonify({'qr_data': latest_qr})

if __name__ == '__main__':
    app.run(debug=True)
