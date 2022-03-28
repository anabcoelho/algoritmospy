#ID motorista: int
#Número CNH: int
#Nome: string
#Sobrenome: stirng
#Data de nascimento: date

class Motorista:

    def __init__(self, id_motorista, nCNH, nome,
                 sobrenome, data_nascimento):
        self.id_motorista = id_motorista
        self.nCNH=nCNH
        self.nome =nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

        # Métodos getter
    def get_motorista(self):
            return self.id_motorista, self.nCNH, self.nome, self.sobrenome, self.data_nascimento



    # Métodos setter para cada atributo
    def set_id_motorista(self,v):
        self.id_motorista = v
    def set_CNH(self,c):
        self.nCNH = c
    def set_nome(self, n):
        self.nome = n
    def set_id_sobrenome(self, s):
        self.sobrenome = s
    def set_data_nascimento(self, d):
        self.data_nascimento = d

    def insert_motorista(self,cursor):

        from datetime import datetime


        # convert datetime string to object, specifying input format

        data_convert = datetime.strptime(self.data_nascimento, '%Y-%m-%d')

        comando = f"""INSERT INTO ana_rodrigues.motorista 
        VALUES( {self.id_motorista}, {self.nCNH},'{self.nome}',
        '{self.sobrenome}', '{data_convert}');"""

        cursor.execute(comando)
        cursor.commit()



    def select_motorista(self,cursor):


        comando = "SELECT * from ana_rodrigues.motorista;"
        cursor.execute(comando)
        results = cursor.fetchall()
        headers = [column[0] for column in cursor.description]

        return results, headers
