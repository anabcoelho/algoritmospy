tipo = input('Qual o tipo do cartão? \n Comum, estudante, vale-transporte ou idoso?')
tipos_passageiros=['COMUM','ESTUDANTE', 'VALE-TRANSPORTE', 'IDOSO']
ba=9
while True:
    if tipo.upper() not in tipos_passageiros:
        tipo= input('Insira um tipo válido'
                   '\n Comum, estudante, vale-transporte ou idoso?')
    #if tipo.upper() in tipos_passageiros:
        #break
    if ba == 9:
        print("oi")
        tipo="3"