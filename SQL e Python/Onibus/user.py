class Usuario:

    def __init__(self, id_user, nome, sobrenome,
                 email, bairro, data_nascimento):
        self.id_user = id_user
        self.nome =nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.data_nascimento = data_nascimento

    def set_usuario(self, id_user, nome, sobrenome, email, bairro, data_nascimento):
        import conectar
        from datetime import datetime
        conexao = conectar.conectar()

        # convert datetime string to object, specifying input format
        #o data_nascimento não vai, pelo o que eu entendi, precisa ter hora(??)
        data_convert = datetime.strptime(self.data_nascimento, '%Y-%m-%d')

        comando = f"""INSERT INTO ana_rodrigues.usuario 
        VALUES( {self.id_user}, '{self.nome}',
        '{self.sobrenome}' ,'{self.email}',
        '{self.bairro}', '{data_convert}');"""

        cursor = conexao.cursor()
        cursor.execute(comando)
        cursor.commit()
        conectar.desconectar(cursor, conexao)

    def novo_usuario (self):
        id_user = int(input('Informe o ID do proprietário'))
        nome=input('Informe o nome do proprietário ')
        sobrenome = input ('Informe o sobrenome do proprietário')
        email = input('Informe o email do proprietário')
        bairro = input ('Informe o bairro do proprietário')
        data_nascimento = input('Informe a data de nascimento \n formato: aaaa-mm-dd')
        Usuario(id_user, nome, sobrenome, email, bairro, data_nascimento).\
            set_usuario(id_user, nome, sobrenome, email, bairro, data_nascimento)

    def get_usuario(self):
        import conectar
        import pandas as pd

        conexao = conectar.conectar()
        comando = "SELECT * from ana_rodrigues.usuario;"
        cursor = conexao.cursor()
        cursor.execute(comando)

        print([column[0] for column in cursor.description])
        for row in cursor:
            print(row)
        #DF=pd.DataFrame(cursor.fetchall())
        #print(DF)
        #DF.to_excel("FileExample.xlsx", sheet_name='Results')
        conectar.desconectar(cursor, conexao)