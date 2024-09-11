from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
def index():
    return "<h1>Hello World</h1>" \
    "<h2> outro texto </h2>" 

@app.route("/")
def indexHtml():
    return render_template("index.html", uma_variavel_no_html = "Rodrigo")

@app.route("/outraRota")
def index2():
    return "Hello World"


@app.route("/rotaHtml1")
def indexHtml1():
    array = [3, 7, 8]
    return render_template("index1.html", variavel_do_meu_primeiro_html = array)

@app.route("/rotaHtml2")
def indexHtml2():
    dictionary = {"chave" : 3}
    return render_template("index2.html", variavel_do_meu_segundo_html= dictionary)

@app.route("/rotaHtml3")
def indexHtml3():
    return render_template("index3.html", variavel_do_meu_terceiro_html = "Rodrigo")

@app.route("/rotaPagina2")
def pagina2(): # Rota com If dentro do HTML
    return render_template("pagina2.html", usuario = "2", variable_name = 4)

app.run(debug=True) # Verifica alterações em tempo real