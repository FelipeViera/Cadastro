from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector


app = Flask(__name__)
CORS(app)


@app.route('/')
def homepage():
    return ""


@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:

        conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
        if conexao.is_connected():
            cursor = conexao.cursor()

        senha = request.json['senha']
        email = request.json['email']

        cursor.execute('SELECT senha from pessoas where email = %s', (email,))

        #Serve para filtrar o dado consultado do database
        simplificando = str(cursor.fetchone())
        simplificando = simplificando.replace('(', '')
        simplificando = simplificando.replace(')', '')
        simplificando = simplificando.replace(',', '')
        simplificando = simplificando.replace("'", '')
        simplificando = simplificando.replace("'", '')
        verificando = simplificando

        if str(senha) == verificando:
            cursor.execute('SELECT nome from pessoas where email = %s', (email,))
            simplificando = str(cursor.fetchone())
            simplificando = simplificando.replace('(', '')
            simplificando = simplificando.replace(')', '')
            simplificando = simplificando.replace(',', '')
            simplificando = simplificando.replace("'", '')
            simplificando = simplificando.replace("'", '')
            resposta = simplificando

        else:
            resposta = "Negado"

        response = jsonify({'resultado': resposta})

    return response, 200


app.run(host='0.0.0.0')
