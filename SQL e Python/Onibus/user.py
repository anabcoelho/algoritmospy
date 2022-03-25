class Usuario:

    def __init__(self, id_user, nome, sobrenome,
                 email, bairro, data_nascimento):
        self.id_user = id_user
        self.nome =nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.data_nascimento = data_nascimento

#Métodos setter para cada atributo
    def set_id_user (self,sid_user):
        self.id_user= sid_user
    def set_nome (self, snome):
        self.nome = snome
    def set_sobrenome(self,ssobrenome):
        self.sobrenome = ssobrenome
    def set_email(self,semail):
        self.email =semail
    def set_bairro(self,sbairro):
        self.bairro = sbairro
    def set_data_nascimento (self,sdata_nasc):
        self.data_nascimento = sdata_nasc

    def get_usuario(self):
        return self.id_user, self.nome, self.sobrenome,self.email, self.bairro, self.data_nascimento

    def insert_usuario(self):
        import conectar
        from datetime import datetime
        conexao = conectar.conectar()

        # convert datetime string to object, specifying input format

        data_convert = datetime.strptime(self.data_nascimento, '%Y-%m-%d')

        comando = f"""INSERT INTO ana_rodrigues.usuario 
        VALUES( {self.id_user}, '{self.nome}',
        '{self.sobrenome}' ,'{self.email}',
        '{self.bairro}', '{data_convert}');"""

        cursor = conexao.cursor()
        cursor.execute(comando)
        cursor.commit()
        conectar.desconectar(cursor, conexao)

    def select_usuario(self,save):
        import conectar

        conexao = conectar.conectar()
        comando = "SELECT * from ana_rodrigues.usuario;"
        cursor = conexao.cursor()
        cursor.execute(comando)
        headers=[column[0] for column in cursor.description]

        for row in cursor:
            print(row)



        if save is True:
            import csv
            cursor.execute(comando)
            results = cursor.fetchall()
            with open(r'usuario.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',', lineterminator='\r',
                                    quoting=csv.QUOTE_ALL, escapechar='\\')
                writer.writerow(headers)
                writer.writerows(results)
            print('salvo')
        conectar.desconectar(cursor, conexao)


