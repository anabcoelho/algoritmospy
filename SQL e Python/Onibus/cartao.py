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

        # Métodos getter para cada atributo
    def get_cartao(self):
            return self.id_cartao, self.id_user, self.creditos, self.tipo, self.data_emissao


        # Métodos setter para cada atributo
    def set_id_cartao(self, ic):
            self.id_cartao =ic
    def set_id_user(self, iu):
            self.id_user = iu
    def set_creditos(self, c):
            self.creditos = c
    def set_tipo(self, t):
            self.tipo=t
    def set_data_emissao(self,de):
        self.data_emissao = de



    def insert_cartao(self):
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

    def select_cartao(self, save):
        import conectar

        conexao = conectar.conectar()
        comando = "SELECT * from ana_rodrigues.cartao;"
        cursor = conexao.cursor()
        cursor.execute(comando)
        headers = [column[0] for column in cursor.description]
        print(headers)
        for row in cursor:
            print(row)

        if save is True:
            import csv
            cursor.execute(comando)
            results = cursor.fetchall()
            with open(r'cartao.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                    quoting=csv.QUOTE_ALL, escapechar='\\')
                writer.writerow(headers)
                writer.writerows(results)
            print('salvo')
        conectar.desconectar(cursor, conexao)

    def salvar_usuario(self):
        pass