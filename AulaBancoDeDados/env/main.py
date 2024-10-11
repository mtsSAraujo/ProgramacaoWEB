from flask import Flask, render_template, request
from mysql_connector import

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("cad_usuario.html")

@app.route("/inserir_usuario", methods = ["POST"])
def inserirUsuario():
    nome = request.form["txt_nome"]
    email = request.form["txt_email"]
    senha = request.form["txt_senha"]
    return nome, email, senha

app.run()