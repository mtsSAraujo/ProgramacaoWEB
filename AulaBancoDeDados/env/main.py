from flask import Flask, render_template, request
import mysql.connector
from mysql import connector

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("cad_usuario.html")

@app.route("/inserir_usuario", methods = ["POST"])
def inserirUsuario():
    nome = request.form["txt_nome"]
    email = request.form["txt_email"]
    senha = request.form["txt_senha"]
    db = mysql.connector.connect(host = "201.23.3.86",
                                user = "usr_aluno",
                                password = "E$tud@_m@1$",
                                port = 5000,
                                database = "aula_fatec"
                            )
    query = "INSERT INTO Mateus_tbusuario (nome, email, senha) VALUES ( %s, %s, %s)"
    valores = (nome, email, senha)

    meu_cursor = db.cursor()
    meu_cursor.execute(query,valores)
    db.commit()
    return render_template("cad_usuario.html")

app.run()