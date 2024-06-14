import requests

link = "http://127.0.0.1:5000/login"

valor = int(input('digite: '))
data = {"senha": valor}

try:
    # Envie a requisição POST
    #convertendo os valores em bibliotecas
    response = requests.post(link, json=data)

    # Verifique se a requisição foi bem sucedida
    if response.status_code == 200:

        # Converta a resposta JSON em um dicionário
        resultado = response.json()

        # Exiba o resultado da soma
        print(f"Resultado: {resultado['resultado']}")

    else:
        # Erro na requisição
        print(f"Erro na requisição: {response.status_code}")
except Exception as e:
    # Erro genérico
    print(f"Erro inesperado: {e}")

valor = int(input('digite: '))
data = {"senha": valor}

try:
    # Envie a requisição POST
    #convertendo os valores em bibliotecas
    response = requests.post(link, json=data)

    # Verifique se a requisição foi bem sucedida
    if response.status_code == 200:

        # Converta a resposta JSON em um dicionário
        resultado = response.json()

        # Exiba o resultado da soma
        print(f"Resultado: {resultado['resultado']}")

    else:
        # Erro na requisição
        print(f"Erro na requisição: {response.status_code}")
except Exception as e:
    # Erro genérico
    print(f"Erro inesperado: {e}")