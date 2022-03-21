#Agora que você criou as tabelas, comece a desenvolver o seu sistema em Python levando em consideração as orientações acima para classes e suas entidades e a conexão com o banco
#crie uma interface no terminal para que o usuário possa cadastrar e visualizar as informações
def conectar():
    import pyodbc
    import dados_conexao #por segurança todos os dados de conexão estão em um arquivo dados_conexão.py
    conexao = pyodbc.connect(dados_conexao.connect_data())
    print('conexão bem sucedida')
    return conexao


