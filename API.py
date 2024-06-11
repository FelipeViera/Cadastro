from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return ""

@app.route('/login', methods=['POST'])
def login():
    senha = request.json['senha']

    if (senha == "felipe"):
        resposta = "Aceito"
    else:
        resposta = "Negado"

    response = {'resultado': resposta}
    return jsonify(response), 200

app.run(host='0.0.0.0')