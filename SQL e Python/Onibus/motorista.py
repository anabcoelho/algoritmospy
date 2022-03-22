#ID motorista: int
#Número CNH: int
#Nome: string
#Sobrenome: stirng
#Data de nascimento: date

class Motorista:

    def __init__(self, id_motorista, nCNH, nome,
                 sobrenome, data_nascimento):
        self.id_motorista = id_motorista
        self.nCNH=nCNH
        self.nome =nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def set_motorista(self, id_motorista, nCNH, nome,
                 sobrenome, data_nascimento):
        from conectar import conectar
        from datetime import datetime
        conexao=conectar()

        # convert datetime string to object, specifying input format
        #o data_nascimento não vai
        data_convert = datetime.strptime(self.data_nascimento, '%Y-%m-%d')
        int_cnh=int(self.nCNH)
        comando = f"""INSERT INTO ana_rodrigues.motorista 
        VALUES( {self.id_motorista}, {int_cnh},'{self.nome}',
        '{self.sobrenome}', '{data_convert}');"""

        cursor = conexao.cursor()
        cursor.execute(comando)
        cursor.commit()

    def novo_motorista (self):
        RED = "\033[1;31m"
        RESET = "\033[0;0m"
        id_motorista = int(input('Informe o ID do motorista'))
        nCNH = int(input('Informe CNH do motorista'))
        nome=input('Informe o nome do proprietário ')
        sobrenome = input ('Informe o sobrenome do proprietário')
        data_nascimento = input('Informe a data de nascimento \n formato: aaaa-mm-dd')
        Motorista(id_motorista, nCNH, nome,
                 sobrenome, data_nascimento).\
            set_motorista(id_motorista, nCNH, nome,
                 sobrenome, data_nascimento)

    def get_motorista(self):
        from conectar import conectar
        import pandas as pd

        conexao = conectar()
        comando = "SELECT * from ana_rodrigues.motorista;"
        cursor = conexao.cursor()
        cursor.execute(comando)
        print([column[0] for column in cursor.description])
        for row in cursor:
            print(row)

Motorista(0,0,0,0,0).novo_motorista()