from flask import Flask, request, jsonify
from flask_cors import CORS
from Classes import Filtro
import mysql.connector
from datetime import datetime


app = Flask(__name__)
CORS(app, methods=['GET', 'POST', 'PUT', 'OPTIONS'])


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
        resposta_consulta = str(cursor.fetchone())
        filtro1 = Filtro()
        filtro1.Simplificar(resposta_consulta)
        verificando = filtro1.valor

        if str(senha) == verificando:
            cursor.execute('SELECT nome from pessoas where email = %s', (email,))
            resposta_consulta = str(cursor.fetchone())
            filtro1.Simplificar(resposta_consulta)
            resposta = filtro1.valor

        else:
            resposta = "Negado"

        response = jsonify({'resultado': resposta})

    return response, 200

@app.route('/cadastro', methods=['POST'])

def cadastro():

    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:

        conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
        if conexao.is_connected():
            cursor = conexao.cursor()

        try:
            senha = request.json['senha']
            senha = str(senha)
            email = request.json['email']
            email = str(email)
            nome = request.json['nome']
            nome = str(nome)
            data_nascimento = request.json['nascimento']
            data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")


            try:
                cursor.execute('INSERT INTO pessoas(email, nome, data_nascimento, senha) VALUES (%s, %s, %s, %s);',(email, nome, data_nascimento, senha))
                conexao.commit()
                resposta = "CADASTRADO"
            except Exception as er:
                resposta = "Erro de banco de dados"
        except Exception as er:
            resposta = "Erro json"

        response = jsonify({'resultado': resposta})

        return response, 200



app.run(host='0.0.0.0')
