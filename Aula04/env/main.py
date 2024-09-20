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

    if(imc < 18.5):
        classificacao = "MAGREZA"
    elif(imc >= 18.5 and imc < 25):
        classificacao = "NORMAL"
    elif(imc >= 25 and imc <30):
        classificacao = "SOBREPESO"
    elif(imc >= 30 and imc < 40):
        classificacao = "OBESIDADE"
    else:
        classificacao = "OBESIDADE GRAVE"

    return render_template("imc.html", imc=f"{imc:.2f}", classificacao = classificacao)

@app.route("/calcular_imc_get")
def calcular_imc_get():
    args = request.args
    altura = float(args.get("txt_altura"))
    peso = float(args.get("txt_peso"))
    imc = peso / (altura ** 2)

    if(imc < 18.5):
        classificacao = "static/chef-1.jpg"
    elif(imc >= 18.5 and imc < 25):
        classificacao = "static/chef-2.jpg"
    elif(imc >= 25 and imc <30):
        classificacao = "static/chef-3.jpg"
    elif(imc >= 30 and imc < 40):
        classificacao = "static/hero-1.jpg"
    else:
        classificacao = "static/favicon-32x32.png"
    return render_template("imc.html", imc=round(imc, 2), classificacao = classificacao)

""" 
@app.route("/", methods=['GET', 'POST'])
def calcular_imc_post():
    imc = None  # Variável para armazenar o valor do IMC
    if request.method == 'POST':
        altura = float(request.form["txt_altura"])
        peso = float(request.form["txt_peso"])
        imc = peso / (altura ** 2)  # Cálculo do IMC

    # Renderiza o template com o valor do IMC (se disponível)
    return render_template("imc.html", imc=f"{imc:.2f}")
"""

app.run()