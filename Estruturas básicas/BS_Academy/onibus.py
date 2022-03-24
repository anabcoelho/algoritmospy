
        # A B C D E
onibus= [[7,7,7,7,7],  #0 linha do motorista
         [0,0,7,0,0],  #1
         [0,0,7,0,0],  #2
         [0,0,7,0,0],  #3
         [0,0,7,0,0],  #4
         [0,0,7,0,0],  #5
         [0,0,7,0,0],  #6
         [0,0,7,0,0],  #7
         ] #eis o nosso busão, 0 está disponível, 1 está comprado e 7 não está disponível, pq 7 é um número legal
#vamos por uma corzinha nesses erros
RED = "\033[1;31m"
RESET = "\033[0;0m"

while True:

    compra_lugar=list(input('Digite o assento comprado, ex: 1A: \n para sair, digite um E'))
    err=False

#momento possíveis erros
    if compra_lugar[0].upper() == 'E':
        err = True
        break

    if len(compra_lugar) != 2 or compra_lugar[0] == '0' or compra_lugar[1].upper() == 'C':
        err=True
        print(' ')
        print(RED+'digite um lugar válido'+RESET)
        print(' ')


#modificação dos
    if err == False:


        fileira = int(compra_lugar[0])
        coluna = compra_lugar[1]

        if coluna.upper() == 'A' and fileira<8:
             coluna=0
        elif coluna.upper() == 'B' and fileira<8:
             coluna=1
        elif coluna.upper() == 'D' and fileira<8:
             coluna=3
        elif coluna.upper() == 'E' and fileira<8:
             coluna=4
        else:
            print(' ')
            print(RED+'digite um lugar válido'+reset)
            print(' ')
            err=True
    if err != True:
        if onibus[fileira][coluna] != 1:
            onibus[fileira][coluna] = 1
        else:
            print(RED+'Lugar ocupado'+RESET)

#é hora de salvar

with open('assentos.txt', 'w') as f:
    f.writelines(' A  B  C  D  E\n')
    f.writelines("%s\n" % l for l in onibus)
    f.writelines('Legenda: \n 0: disponível, 1: comprado e 7: não disponível')
    f.close()