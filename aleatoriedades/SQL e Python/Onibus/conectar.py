
def conectar():
    import pyodbc
    import dados_conexao #por segurança todos os dados de conexão estão em um arquivo dados_conexão.py
    conexao = pyodbc.connect(dados_conexao.connect_data())
    print('conexão bem sucedida')
    return conexao
def desconectar(cursor,conexao):
    cursor.close()
    conexao.close()


