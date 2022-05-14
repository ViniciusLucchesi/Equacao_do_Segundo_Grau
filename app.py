# Importing required Libraries
from math import sqrt
from flask import Flask, render_template, redirect, request, url_for
from flaskwebgui import FlaskUI
from functions.calcular import SegundoGrau

# Initializing Flask server
app = Flask(__name__)
gui = FlaskUI(app, width=1200, height=850)


# Defining Flask routes
@app.route("/")
def index():
    return render_template('inputData.html')

@app.route("/resolution", methods=['GET', 'POST'])
def resolution():
    if request.method == 'POST':
        # Getting the form parameters
        A = int(request.form.get('A'))
        B = int(request.form.get('B'))
        C = int(request.form.get('C'))

        equacao = SegundoGrau(A, B, C)
        delta = equacao.calcular_delta()
        data = equacao.calcular_raizes()        
        raiz_delta = sqrt(equacao.calcular_delta()) if delta > 0 else 0 

        return render_template(
            'resolution.html',
            A = A,
            B = B,
            C = C,
            data=data,
            raiz_delta=raiz_delta,
            delta=delta
        )

@app.route("/voltar")
def voltar():
    return redirect(url_for('index'))


# Running flaks app
if __name__ == '__main__':
    gui.run()