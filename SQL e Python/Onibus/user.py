class Usuario:


    def __init__(self, id_user, nome, sobrenome,
                 email, bairro, data_nascimento):
        self.id_user = id_user
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.data_nascimento = data_nascimento


    # Métodos setter para cada atributo
    def set_id_user(self, sid_user):
        self.id_user = sid_user

    def set_nome(self, snome):
        self.nome = snome

    def set_sobrenome(self, ssobrenome):
        self.sobrenome = ssobrenome

    def set_email(self, semail):
        self.email = semail

    def set_bairro(self, sbairro):
        self.bairro = sbairro

    def set_data_nascimento(self, sdata_nasc):
        self.data_nascimento = sdata_nasc

    def get_usuario(self):
        return self.id_user, self.nome, self.sobrenome, self.email, self.bairro, self.data_nascimento

    def insert_usuario(self,cursor):

        from datetime import datetime

        # convert datetime string to object, specifying input format

        data_convert = datetime.strptime(self.data_nascimento, '%Y-%m-%d')

        comando = f"""INSERT INTO ana_rodrigues.usuario 
        VALUES( {self.id_user}, '{self.nome}',
        '{self.sobrenome}' ,'{self.email}',
        '{self.bairro}', '{data_convert}');"""

        cursor.execute(comando)
        cursor.commit()


    def select_usuario(self,cursor):
        comando = "SELECT * from ana_rodrigues.usuario;"

        cursor.execute(comando)
        results = cursor.fetchall()
        headers = [column[0] for column in cursor.description]
        return results, headers

    def atualizar_bairro(self,bairro,id_user,cursor):
        comando = f"""UPDATE ana_rodrigues.usuario
                    set bairro = '{bairro}'
                    where id_user = '{id_user}'
                  ;"""

        cursor.execute(comando)
        cursor.commit()
        print('valor atualizado')

