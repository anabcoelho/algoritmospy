class Onibus:

    def __init__(self, placa, linha, modelo,
                 ano, id_motorista):
        self.placa = placa
        self.linha = linha
        self.modelo = modelo
        self.ano = ano
        self.id_motorista=id_motorista

    # Métodos getter
    def get_onibus(self):
        return self.placa, self.linha, self.modelo, self.ano, self.id_motorista

    # Métodos setter para cada atributo

    def set_placa(self, p):
        self.placa = p

    def set_linha(self,l):
        self.linha = l

    def set_modelo(self,m):
        self.modelo = m

    def set_ano(self, a):
        self.ano = a

    def set_id_motorista(self, idm):
        self.id_motorista = idm





    def insert_onibus(self):
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


    def select_onibus(self):
        import conectar

        conexao = conectar.conectar()
        comando = "SELECT * from ana_rodrigues.onibus;"
        cursor = conexao.cursor()
        cursor.execute(comando)
        results = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        conectar.desconectar(cursor, conexao)
        return results, headers