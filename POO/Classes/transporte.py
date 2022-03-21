class transporte:
    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    def getnome(self):
        return self.nome

    def getpeso(self):
        return self.peso

    def getpreco(self):
        return self.preco


class carro(transporte):  # herdou de transporte
    def __init__(self, nome, peso, preco, seguro):
        transporte.__init__(self, nome, peso, preco)
        self.seguro = seguro

    def getseguro(self):
        return self.seguro


t = transporte('fusca', 5000, 2800)
print(t.getnome())

car = carro('fusca', 5000, 2800, 4000)
print(car.getpeso())