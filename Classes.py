class Filtro():

    # Esta classe tem como função apenas realizar o replace do dado consultado do database.
    # Sem o Filtro: ('Josias',)
    #Com o Filtro: Josias
    def __init__(self):
        self.valor = ""

    def Simplificar(self, simplificando):
        simplificando = simplificando.replace('(', '')
        simplificando = simplificando.replace(')', '')
        simplificando = simplificando.replace(',', '')
        simplificando = simplificando.replace("'", '')
        simplificando = simplificando.replace("'", '')
        self.valor = simplificando

