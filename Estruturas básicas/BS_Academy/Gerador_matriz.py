class Matriz:
    def __init__(self, Linha, Coluna):
        self.Linha = Linha
        self.Coluna = Coluna

    def fazer_matriz(self, linha_indisponivel, coluna_indisponivel):
        matriz = []
        for i in range(self.Linha):
            a = []
            if i == linha_indisponivel:
                for j in range(self.Coluna):
                    a.append('I')
            for j in range(self.Coluna):
                if j == coluna_indisponivel:
                    a.append('I')
                else:
                    a.append(0)
            matriz.append(a)
        return matriz

    def print_matriz(self, matriz):
        for i in range(self.Linha):
            for j in range(self.Coluna):
                print(matriz[i][j], end=" ")
            print()



