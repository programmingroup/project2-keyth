from flask import Flask, request
import string
import random

app = Flask(__name__)

def generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Debes seleccionar al menos un tipo de carácter"

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        longitud = int(request.form['longitud'])
        incluir_mayusculas = 'mayusculas' in request.form
        incluir_minusculas = 'minusculas' in request.form
        incluir_numeros = 'numeros' in request.form
        incluir_simbolos = 'simbolos' in request.form

        contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
        return f"<p>Tu contraseña generada es: {contrasena}</p>"
    else:
        return """
        <form method="POST">
            <label for="longitud">Longitud:</label>
            <input type="number" id="longitud" name="longitud" required>
            <label><input type="checkbox" name="mayusculas"> Mayúsculas</label>
            <label><input type="checkbox" name="minusculas"> Minúsculas</label>
            <label><input type="checkbox" name="numeros"> Números</label>
            <label><input type="checkbox" name="simbolos"> Símbolos</label>
            <button type="submit">Generar</button>
        </form>
        """

if __name__ == '__main__':
    app.run(debug=True)



