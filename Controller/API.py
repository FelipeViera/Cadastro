from flask import Flask, request, jsonify
from flask_cors import CORS
from Model.Classe_principal import ClassePrincipal
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
            Consulta = ClassePrincipal()

            Consulta.senha = request.json['senha']
            Consulta.email = request.json['email']

            Consulta.Executar('SELECT senha from pessoas where email = %s',(Consulta.email,))

            # Serve para filtrar o dado consultado do database
            verificando = Consulta.valor

            if str(Consulta.senha) == verificando:
                resposta = "ACEITO"

            else:
                resposta = "NEGADO"

        except:
            resposta = "Banco de Dados fora do Ar"


        response = jsonify({'resultado': resposta})
        Consulta.Encerrar()
    return response, 200

@app.route('/perfil', methods=['POST'])

def perfil():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:
        try:
            Consulta = ClassePrincipal()

            Consulta.senha = request.json['senha']
            Consulta.email = request.json['email']

            Consulta.Executar('SELECT senha from pessoas where email = %s', (Consulta.email,))

            # Serve para filtrar o dado consultado do database
            verificando = Consulta.valor

            if str(Consulta.senha) == verificando:

                Consulta.Executar('SELECT nome from pessoas where email = %s', (Consulta.email,))
                Consulta.nome = Consulta.valor

                Consulta.Executar('SELECT data_nascimento from pessoas where email = %s', (Consulta.email,))

                Consulta.data_nasc = Consulta.valor

                Consulta.data_nasc = str(Consulta.data_nasc.replace('datetime.date', ''))
                Consulta.data_nasc = Consulta.data_nasc.replace(' ', '-')

                resposta = "Aceito"


            else:
                resposta = "Negado"

        except:
            resposta = "Fora do ar"





    response = jsonify({'nome': Consulta.nome, 'data_nasc': Consulta.data_nasc, 'resultado': resposta})
    Consulta.Encerrar()
    return response, 200


@app.route('/editar', methods=['POST'])
def editar():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:
        print('editar')

@app.route('/cadastro', methods=['POST'])

def cadastro():

    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
    else:

        try:
            Consulta = ClassePrincipal()

            try:
                resposta = "NEGADO"

                Consulta.senha = str(request.json['senha'])

                Consulta.email = str(request.json['email'])

                Consulta.nome = str(request.json['nome'])

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
                        Consulta.Executar('INSERT INTO pessoas(email, nome, data_nascimento, senha) VALUES (%s, %s, %s, %s);',
                            (Consulta.email, Consulta.nome, data_nascimento, Consulta.senha))

                        Consulta.conexao.commit()
                        resposta = "CADASTRADO"


                    except Exception as er:
                        print("Não cadastrado")

            except Exception as er:
                print("Erro json")
        except:
            print("fora do ar")


        response = jsonify({'resultado': resposta})
        Consulta.Encerrar()

        return response, 200



app.run(host='0.0.0.0')
