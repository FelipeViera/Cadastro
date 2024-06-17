from flask import Flask, request, jsonify
from flask_cors import CORS

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
        senha = request.json['senha']
        if senha == "10":
            resposta = "Aceito"
        else:
            resposta = "Negado"
        response = jsonify({'resultado': resposta})

    return response, 200


app.run(host='0.0.0.0')
