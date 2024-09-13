from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def imc():
    return render_template("imc.html")

@app.route("/calcular_imc_post", methods = ['POST'])
def calcular_imc_post():
    return 'Hello world'


app.run()