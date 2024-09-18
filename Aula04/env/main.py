from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def imc():
    return render_template("imc.html")

@app.route("/calcular_imc_post", methods = ['POST'])
def calcular_imc_post():
    altura = float(request.form["txt_altura"])
    peso = float(request.form["txt_peso"])
    imc = peso / (altura ** 2)
    return render_template("imc.html", imc=format(imc:.2f))

"""
@app.route("/", methods=['GET', 'POST'])
def calcular_imc_post():
    imc = None  # Variável para armazenar o valor do IMC
    if request.method == 'POST':
        altura = float(request.form["txt_altura"])
        peso = float(request.form["txt_peso"])
        imc = peso / (altura ** 2)  # Cálculo do IMC

    # Renderiza o template com o valor do IMC (se disponível)
    return render_template("imc.html", imc="{imc:}")
"""

app.run()