#Agora que você criou as tabelas, comece a desenvolver o seu sistema em Python levando em consideração as orientações acima para classes e suas entidades e a conexão com o banco
#crie uma interface no terminal para que o usuário possa cadastrar e visualizar as informações


import pyodbc
conexao_data = (
    'Driver={SQL Server};'
    'Server=sql-estudo.database.windows.net,1433;'
    'Database=db-estudos;'
    'UID=admin-azure;'
    'PWD=****;'
)

conexao = pyodbc.connect(conexao_data)
print('coneção bem sucedida')

cursor = conexao.cursor()
