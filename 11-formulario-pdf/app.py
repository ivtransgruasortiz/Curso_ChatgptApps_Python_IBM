from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        edad = request.form.get("edad")
        dni = request.form.get("dni")
        localidad = request.form.get("localidad")

        # Generar el PDF con fpdf2
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=14)

        pdf.cell(200, 10, txt="Información de la persona", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True)
        pdf.cell(200, 10, txt=f"Apellido: {apellido}", ln=True)
        pdf.cell(200, 10, txt=f"Edad: {edad}", ln=True)
        pdf.cell(200, 10, txt=f"DNI: {dni}", ln=True)
        pdf.cell(200, 10, txt=f"Localidad: {localidad}", ln=True)

        # Guardar en memoria como archivo virtual
        pdf_output = io.BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)

        return send_file(
            pdf_output,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='informacion_persona.pdf'
        )

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)