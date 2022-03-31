
       #Gerar a matriz

import Gerador_matriz as gm
L=8
C=5
objm = gm.Matriz(L, C)
onibus = objm.fazer_matriz(0,2)
objm.print_matriz(onibus)

RED = "\033[1;31m"
RESET = "\033[0;0m"

while True:

    compra_lugar=list(input('''
    Digite o assento sendo comprado, ex: 1A: 
    para sair, digite um E 
    Para consultar, digite consulta'''))
    err=False

#momento possíveis erros
    if compra_lugar[0].upper() == 'E':
        err = True
        break
    if ''.join(compra_lugar).upper() == 'CONSULTA':
        err=True
        objm.print_matriz(onibus)



    elif len(compra_lugar) != 2 or compra_lugar[0] == '0' or compra_lugar[1].upper() == 'C' :
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
            print(RED+'digite um lugar válido'+RESET)
            print(' ')
            err=True
    if err != True:
        if onibus[fileira][coluna] != 1:
            onibus[fileira][coluna] = 1
            print('Assento comprado')
        else:
            print(RED+'Lugar ocupado'+RESET)

#é hora de salvar

with open('assentos.txt', 'w') as f:
    f.writelines('A  B  C  D  E\n')

    for i in range(L):
        for j in range(C):
            f.write(str(onibus[i][j]))
            f.write('  ')
        f.write('\n')
    f.writelines('Legenda: \n 0: disponível, 1: comprado e I: não disponível')
    f.close()
    print('Salvo')