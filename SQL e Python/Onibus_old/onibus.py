class Onibus:

    def __init__(self, placa, linha, modelo,
                 ano, id_motorista):
        self.placa = placa
        self.linha = linha
        self.modelo = modelo
        self.ano = ano
        self.id_motorista=id_motorista


    def insert_onibus(self, placa, linha, modelo, ano, id_motorista):
        import conectar
        from datetime import datetime
        conexao=conectar.conectar()

        # convert datetime string to object, specifying input format
        #o data_nascimento não vai
        data_convert  = datetime.strptime(self.ano + '-01-01', '%Y-%m-%d')


        comando = f"""INSERT INTO ana_rodrigues.onibus
        VALUES({self.placa},{self.linha},'{self.modelo}','{data_convert}',{self.id_motorista} );"""

        cursor = conexao.cursor()
        cursor.execute(comando)
        cursor.commit()
        conectar.desconectar(cursor, conexao)

    #placa: int
    #linha: int
    #Modelo str
    #Ano date
    #ID motorista: int
    def novo_onibus (self):
        placa = int(input('Informe o número da placa'))
        linha=int(input('Informe o número da linha '))
        modelo= input ('Informe o modelo do ônibus')
        ano = input('Informe o ano do õnibus (4 dígitos)')
        id_motorista = int(input('Informe o ID do motorista'))
        Onibus(placa, linha, modelo,
               ano, id_motorista).\
            insert_onibus(placa, linha, modelo, ano, id_motorista)

    def select_onibus(self):
        import conectar
        import pandas as pd

        conexao = conectar.conectar()
        comando = "SELECT * from ana_rodrigues.onibus;"
        cursor = conexao.cursor()
        cursor.execute(comando)
        print([column[0] for column in cursor.description])
        for row in cursor:
            print(row)
        conectar.desconectar(cursor, conexao)