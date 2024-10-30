from flask import Flask, render_template, request, flash
import mysql.connector

app = Flask(__name__)

@app.route("/login")
def loginPage():
    return render_template("login.html", senhaErrada = "")

@app.route("/login", methods = ["POST"])
def validarLogin():
    usuario = request.form["txt_usuario"]
    senha = request.form["txt_senha"]

    db = mysql.connector.connect(
        host="201.23.3.86",
        user="usr_aluno",
        password="E$tud@_m@1$",
        port=5000,
        database="aula_fatec"
    )

    query = "SELECT usuario, senha from Mateus_tbusuario where usuario = %s and senha = %s"
    meu_cursor = db.cursor()
    meu_cursor.execute(query, (usuario, senha))
    results = meu_cursor.fetchall()
    db.close()
    
    if results:
        return "Deu certo"
    else:
        return render_template("login.html", senhaErrada = "Usuário ou senha inválido")

@app.route("/user")
def userPage():
    return render_template("cad_usuario.html", users = findAllUser())

def findAllUser():
    db = mysql.connector.connect(
        host="201.23.3.86",
        user="usr_aluno",
        password="E$tud@_m@1$",
        port=5000,
        database="aula_fatec"
    )
    query = "SELECT codigo, usuario, email FROM Mateus_tbusuario"
    meu_cursor = db.cursor()
    meu_cursor.execute(query)
    results = meu_cursor.fetchall()
    db.close()
    return results

@app.route("/user", methods = ["POST"])
def inserirUsuario():
    usuario = request.form["txt_usuario"]
    email = request.form["txt_email"]
    senha = request.form["txt_senha"]

    db = mysql.connector.connect(
        host="201.23.3.86",
        user="usr_aluno",
        password="E$tud@_m@1$",
        port=5000,
        database="aula_fatec"
    )

    query = "INSERT INTO Mateus_tbusuario (usuario, email, senha) VALUES (%s, %s, %s)"
    valores = (usuario, email, senha)

    meu_cursor = db.cursor()
    meu_cursor.execute(query, valores)
    db.commit()

    db.close()
    return render_template("cad_usuario.html")

@app.route("/client")
def clientPage():
    return render_template("cad_cliente.html")

@app.route("/client", methods = ["POST"])
def inserirCliente():
    nome = request.form["txt_nome"]
    cpf = request.form["txt_cpf"]
    rg = request.form["txt_rg"]
    endereco = request.form["txt_endereco"]
    bairro = request.form["txt_bairro"]
    cidade = request.form["txt_cidade"]
    cep = request.form["txt_cep"]

    db = mysql.connector.connect(
        host="201.23.3.86",
        user="usr_aluno",
        password="E$tud@_m@1$",
        port=5000,
        database="aula_fatec"
    )

    query = "INSERT INTO Mateus_tbcliente (nome, cpf, rg, endereco, bairro, cidade, cep) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (nome, cpf, rg, endereco, bairro, cidade, cep)

    meu_cursor = db.cursor()
    meu_cursor.execute(query, valores)
    db.commit()

    db.close()
    return render_template("cad_cliente.html")

app.run(debug = True)