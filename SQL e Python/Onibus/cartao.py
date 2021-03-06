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



    def insert_cartao(self,cursor):

        from datetime import datetime

        data_convert = datetime.strptime(self.data_emissao, '%Y-%m-%d')

        comando = f"""INSERT INTO ana_rodrigues.cartao 
        VALUES( {self.id_cartao}, {self.id_user},{self.creditos},'{self.tipo}','{data_convert}');"""

        cursor.execute(comando)
        cursor.commit()

    def checar_tipo(self, id_user, cursor):
        from datetime import datetime
        comando = f'''SELECT year(data_de_nascimento) from ana_rodrigues.usuario
                                                where id_user = {id_user} ;'''
        cursor.execute(comando)

        anoatual = int(datetime.today().strftime('%Y'))
        idade = anoatual - cursor.fetchone()[0]
        return (idade)

    def select_cartao(self,cursor):

        comando = "SELECT * from ana_rodrigues.cartao;"

        cursor.execute(comando)
        results = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        return results, headers

    def atualizar_saldo(self,id_cartao,creditos,cursor):
        comando = f"""UPDATE ana_rodrigues.cartao
                    set creditos = creditos + {creditos} 
                    where id_cartao = {id_cartao} ;"""

        cursor.execute(comando)
        cursor.commit()
        print('valor atualizado')

