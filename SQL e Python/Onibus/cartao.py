#create table ana_rodrigues.cartao(
#	id_cartao int PRIMARY KEY NOT NULL,
#	id_user int FOREIGN KEY references ana_rodrigues.usuario(id_user),
#	creditos decimal (25,2) NOT NULL,
#	tipo varchar(15) NOT NULL,
#	data_emissao date NOT NULL);

class Cartao:

    def __init__(self):
        self.id_cartao=0
        self.id_user = 0
        self.creditos =0
        self.tipo = 0
        self.data_emissao =0

    def set_cartao(self, id_cartao, id_user, creditos, tipo, data_emissao):
        from conectar import conectar
        conexao=conectar()
        comando = f"""INSERT INTO ana_rodrigues.cartao 
        VALUES( {self.id_cartao}, {self.id_user},{self.creditos},'{self.tipo}','{self.data_emissao}');"""
        cursor = conexao.cursor()
        cursor.execute(comando)
        conexao.commit()

    def novo_cartao (self):
        RED = "\033[1;31m"
        RESET = "\033[0;0m"
        from datetime import datetime
        id_cartao = int(input('Qual o ID do cartão?'))
        id_user = int(input('Informe o ID do proprietário'))
        creditos = float(input('Quantos créditos?'))
        tipo = input('Qual o tipo do cartão? \n Comum, estudante, vale-transporte ou idoso?')
        tipos_passageiros=['comum','estudante', 'vale-transporte', 'idoso']
        while tipo not in tipos_passageiros:
            tipo= input(RED+'Insira um tipo válido'+ RESET +'\n Comum, estudante, vale-transporte ou idoso?')
        data_emissao = datetime.today().strftime('%Y%m%d')
        Cartao().set_cartao(id_cartao, id_user, creditos, tipo, data_emissao)




Cartao().novo_cartao()
