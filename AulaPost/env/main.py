from flask import Flask, render_template, request, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("cad_usuario.html")

@app.route("/inserir_usuario", methods = ["POST"])
def inserirUsuario():
    try:
        nome = request.form["txt_nome"]
        email = request.form["txt_email"]
        senha = request.form["txt_senha"]

        db = mysql.connector.connect(
            host="201.23.3.86",
            user="usr_aluno",
            password="E$tud@_m@1$",
            port=5000,
            database="aula_fatec"
        )

        query = "INSERT INTO Mateus_tbusuario (nome, email, senha) VALUES (%s, %s, %s)"
        valores = (nome, email, senha)

        meu_cursor = db.cursor()
        meu_cursor.execute(query, valores)
        db.commit()

        flash("Usuário inserido com sucesso!")
        return render_template("cad_usuario.html")

    except Error as e:
        print(f"Erro ao conectar ou executar query no banco de dados: {e}")
        flash(f"Ocorreu um erro ao inserir o usuário: {e}")
        return render_template("erro.html")

    finally:
        if db.is_connected():
            meu_cursor.close()
            db.close()

app.run(debug = True)