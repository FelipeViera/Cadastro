import mysql.connector

class ClassePrincipal:

    # Esta classe tem como função apenas realizar o replace do dado consultado do database.
    # Sem o Filtro: ('Josias',)
    #Com o Filtro: Josias
    def __init__(self):
        # Vai chamar a função de conexão ao banco de dados
        self.valor = ""
        self.nome = ""
        self.data_nasc = ""
        self.email = ""
        self.senha = ""

        #Conexão direta com o Banco de dados
        try:
            self.conexao = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')
            self.cursor = self.conexao.cursor()

        except:
            print("Banco de dados fora do ar")

    def Simplificar(self, simplificando):
        simplificando = simplificando.replace('(', '')
        simplificando = simplificando.replace(')', '')
        simplificando = simplificando.replace(',', '')
        simplificando = simplificando.replace("'", '')
        simplificando = simplificando.replace("'", '')
        self.valor = simplificando

    def Executar(self, comando, parametro):
        self.cursor.execute(comando, (parametro))
        resposta_consulta = str(self.cursor.fetchone())
        self.Simplificar(resposta_consulta)

    def Encerrar(self):
        self.cursor.close()

