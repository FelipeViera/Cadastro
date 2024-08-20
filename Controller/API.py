from flask import Flask, request, jsonify
from flask_cors import CORS
from Model.Classes  import Filtro
import mysql.connector
from datetime import datetime
from datetime import date


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

        try:
            conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
            if conexao.is_connected():
                cursor = conexao.cursor()

            senha = request.json['senha']
            email = request.json['email']

            cursor.execute('SELECT senha from pessoas where email = %s', (email,))

            # Serve para filtrar o dado consultado do database
            resposta_consulta = str(cursor.fetchone())
            filtro1 = Filtro()
            filtro1.Simplificar(resposta_consulta)
            verificando = filtro1.valor

            if str(senha) == verificando:
                # cursor.execute('SELECT nome from pessoas where email = %s', (email,))
                # resposta_consulta = str(cursor.fetchone())
                # filtro1.Simplificar(resposta_consulta)
                # resposta = filtro1.valor
                resposta = "ACEITO"

            else:
                resposta = "NEGADO"

        except:
            resposta = "Banco de Dados fora do Ar"


        response = jsonify({'resultado': resposta})

    return response, 200

@app.route('/perfil', methods=['POST'])

def perfil():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:

        try:

            conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
            if conexao.is_connected():
                cursor = conexao.cursor()
            senha = request.json['senha']
            email = request.json['email']

            cursor.execute('SELECT senha from pessoas where email = %s', (email,))

            # Serve para filtrar o dado consultado do database
            resposta_consulta = str(cursor.fetchone())
            filtro1 = Filtro()
            filtro1.Simplificar(resposta_consulta)
            verificando = filtro1.valor

            if str(senha) == verificando:
                cursor.execute('SELECT nome from pessoas where email = %s', (email,))
                resposta_consulta = str(cursor.fetchone())
                filtro1.Simplificar(resposta_consulta)
                nome = filtro1.valor

                cursor.execute('SELECT data_nascimento from pessoas where email = %s', (email,))
                resposta_consulta = str(cursor.fetchone())
                filtro1.Simplificar(resposta_consulta)
                data_nasc = filtro1.valor

                data_nasc = str(data_nasc.replace('datetime.date', ''))
                data_nasc = data_nasc.replace(' ', '-')

                resposta = "Aceito"


            else:
                resposta = "Negado"

        except:
            resposta = "Fora do ar"





    response = jsonify({'nome': nome, 'data_nasc': data_nasc, 'resultado': resposta})
    return response, 200


@app.route('/cadastro', methods=['POST'])

def cadastro():

    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:

        try:
            conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')


            try:
                resposta = "NEGADO"
                cursor = conexao.cursor()
                senha = request.json['senha']
                senha = str(senha)
                email = request.json['email']
                email = str(email)
                nome = request.json['nome']
                nome = str(nome)
                data_nascimento = request.json['nascimento']
                caracteres = str(data_nascimento)
                ano = ''
                i = 0
                data_atual = str(date.today())
                data_atual = data_atual.replace("-", " ")
                data_atual = data_atual.split()
                while i <= 3:
                    ano += caracteres[i]
                    i += 1

                if ((int(ano)) < (int(data_atual[0])) - 18 ):
                    data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
                    try:
                        cursor.execute(
                            'INSERT INTO pessoas(email, nome, data_nascimento, senha) VALUES (%s, %s, %s, %s);',
                            (email, nome, data_nascimento, senha))

                        conexao.commit()
                        resposta = "CADASTRADO"


                    except Exception as er:
                        print("Não cadastrado")


            except Exception as er:
                print("Erro json")
        except:
            print("fora do ar")


        response = jsonify({'resultado': resposta})

        return response, 200



app.run(host='0.0.0.0')
