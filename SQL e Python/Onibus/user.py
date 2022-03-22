class Usuario:

    def __init__(self, id_user, nome, sobrenome,
                 email, bairro, data_nascimento):
        self.id_user = id_user
        self.nome =nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.data_nascimento = data_nascimento

    def set_user(self, id_user, nome, sobrenome, email, bairro, data_nascimento):
        from conectar import conectar
        from datetime import datetime
        conexao=conectar()

        # convert datetime string to object, specifying input format
        #o data_nascimento não vai
        data_convert = datetime.strptime(self.data_nascimento, '%Y-%m-%d')

        comando = f"""INSERT INTO ana_rodrigues.usuario 
        VALUES( {self.id_user}, '{self.nome}',
        '{self.sobrenome}' ,'{self.email}',
        '{self.bairro}', '{data_convert}');"""

        cursor = conexao.cursor()
        cursor.execute(comando)
        cursor.commit()

    def novo_usuario (self):
        id_user = int(input('Informe o ID do proprietário'))
        nome=input('Informe o nome do proprietário ')
        sobrenome = input ('Informe o sobrenome do proprietário')
        email = input('Informe o email do proprietário')
        bairro = input ('Informe o bairro do proprietário')
        data_nascimento = input('Informe a data de nascimento \n formato: aaaa-mm-dd')
        Usuario(id_user, nome, sobrenome, email, bairro, data_nascimento).\
            set_user(id_user, nome, sobrenome, email, bairro, data_nascimento)




Usuario(0,0,0,0,0,0).novo_usuario()