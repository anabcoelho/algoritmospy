#create table ana_rodrigues.cartao(
#	id_cartao int PRIMARY KEY NOT NULL,
#	id_user int FOREIGN KEY references ana_rodrigues.usuario(id_user),
#	creditos decimal (25,2) NOT NULL,
#	tipo varchar(15) NOT NULL,
#	data_emissao date NOT NULL);

class Cartao:

    def __init__(self,id_cartao, id_user, creditos, tipo, data_emissao):
        self.id_cartao=id_cartao
        self.id_user = id_user
        self.creditos =creditos
        self.tipo = tipo
        self.data_emissao = data_emissao

    def set_cartao(self, id_cartao, id_user, creditos, tipo, data_emissao):
        import conectar
        from datetime import datetime
        conexao=conectar.conectar()
        data_convert = datetime.strptime(self.data_emissao, '%Y-%m-%d')

        comando = f"""INSERT INTO ana_rodrigues.cartao 
        VALUES( {self.id_cartao}, {self.id_user},{self.creditos},'{self.tipo}','{data_convert}');"""
        cursor = conexao.cursor()
        cursor.execute(comando)
        conexao.commit()
        conectar.desconectar(cursor, conexao)

    def novo_cartao (self):
        import conectar
        from datetime import datetime

        RED = "\033[1;31m"
        RESET = "\033[0;0m"

        id_cartao = int(input('Qual o ID do cartão?'))
        id_user = int(input('Informe o ID do proprietário'))
        creditos = float(input('Quantos créditos?'))

        #conferindo o tipo.
        tipo = input('Qual o tipo do cartão? \n Comum, estudante, vale-transporte ou idoso?')
        tipos_passageiros=['COMUM','ESTUDANTE', 'VALE-TRANSPORTE', 'IDOSO']
        while True:
            if tipo.upper() not in tipos_passageiros:
                tipo= input(RED+'Insira um tipo válido'+ RESET +
                        '\n Comum, estudante, vale-transporte ou idoso?')
            elif tipo.upper() == 'ESTUDANTE' or tipo.upper() =='IDOSO':
                conexao = conectar.conectar()
                comando = f'''SELECT year(data_de_nascimento) from ana_rodrigues.usuario
                        where id_user = {id_user} ;'''
                cursor = conexao.cursor()
                cursor.execute(comando)

                anoatual = int(datetime.today().strftime('%Y'))
                idade=anoatual-cursor.fetchone()[0]

                if tipo.upper() == "IDOSO" and idade<60:
                        print(f'passageiro tem {idade} anos, não é apto para essa modalidade')
                        tipo = input(RED + 'Insira um tipo válido, e autorizado' + RESET)
                if tipo.upper() == "ESTUDANTE" and idade>21:
                    docum=input('Conferir documentação de estudante \n é válida? s/n')
                    if docum.upper() == 'S':
                        break
                    else:
                         tipo = input(RED + 'Insira um tipo válido, e autorizado' + RESET)
            elif tipo.upper() in tipos_passageiros:
                break


        data_emissao = datetime.today().strftime('%Y-%m-%d')
        Cartao(id_cartao, id_user, creditos, tipo, data_emissao).set_cartao(id_cartao, id_user, creditos, tipo, data_emissao)

    def get_cartao(self):
        import conectar
        import pandas as pd

        conexao = conectar.conectar()
        comando = "SELECT * from ana_rodrigues.cartao;"
        cursor = conexao.cursor()
        cursor.execute(comando)
        print([column[0] for column in cursor.description])
        for row in cursor:
            print(row)
        conectar.desconectar(cursor, conexao)