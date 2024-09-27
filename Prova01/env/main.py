from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root_function():
    return render_template("pagina_inicial.html")

def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"
    
@app.route("/calc-triangulo")
def calcula_triangulo():
    lado1 = request.args.get('lado1', type=float)
    lado2 = request.args.get('lado2', type=float)
    lado3 = request.args.get('lado3', type=float)
    
    tipo = None
    imagem = None
    if lado1 and lado2 and lado3:
        tipo = tipo_triangulo(lado1, lado2, lado3)
        if tipo == "Equilátero":
            imagem = "triangulo-equilatero.png"
        elif tipo == "Escaleno":
            imagem = "triangulo-escaleno.png"
        else:
            imagem = "triangulo-isosceles.png"
    
    return render_template("calc_triangulo.html", tipo=tipo, imagem = imagem)

def calcular_media(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

@app.route("/media-notas", methods=['GET', 'POST'])
def media_notas():
    media = None
    imagem = None
    if request.method == 'POST':
        try:
            nota1 = request.form.get('nota1', type=float)
            nota2 = request.form.get('nota2', type=float)
            nota3 = request.form.get('nota3', type=float)
            nota4 = request.form.get('nota4', type=float)
            
            media = calcular_media(nota1, nota2, nota3, nota4)

            if media >= 7:
                imagem = "aprovado.jpg"
            else:
                imagem = "reprovado.jpg"

        except TypeError:
            media = "Erro: Todas as notas devem ser números."

    return render_template("media_notas.html", media=media, imagem = imagem)

app.run()