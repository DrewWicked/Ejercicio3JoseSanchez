from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            promedio = (nota1 + nota2 + nota3) / 3
            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
        except ValueError:
            promedio = "Error en los datos"

    return render_template("ejercicio1.html", promedio=promedio, estado=estado)

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_largo = None
    longitud = None
    if request.method == "POST":
        nombres = [
            request.form["nombre1"],
            request.form["nombre2"],
            request.form["nombre3"],
        ]
        nombre_largo = max(nombres, key=len)
        longitud = len(nombre_largo)

    return render_template("ejercicio2.html", nombre_largo=nombre_largo, longitud=longitud)

if __name__ == "__main__":
    app.run(debug=True)




