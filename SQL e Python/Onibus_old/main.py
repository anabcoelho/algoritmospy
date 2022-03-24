
# 4 classes Usuario, Cartao, Motorista, Onibus, Main
#           usuario
#           select, insert, novo
#


import user
import cartao
import motorista
import onibus

#cores para agradar o dia
RED   = "\033[1;31m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"

print(BOLD+'Seja bem-vindo ao sistema PoccoCard, o cartão de transporte municipal da PoccoBus'+RESET)

while True:
    acao = input('O que deseja fazer? \n Cadastrar, consultar dados ou sair?')

    if acao.upper() == 'SAIR':
        break


    elif acao.upper() == 'CADASTRAR':
        while True:
            cl=input('O que deseja cadastrar?\n digite sair para sair')

            if cl.upper() == ('CARTAO' or 'CARTÃO'):
                print('entrei em cartao', cl.upper())
                cartao.Cartao(0,0,0,0,0).novo_cartao()
                print('Cartão cadastrado')

            elif cl.upper() == 'MOTORISTA':
                motorista.Motorista(0,0,0,0,0).novo_motorista()
                print('motorista cadastrado')

            elif cl.upper() == ('ONIBUS' or 'ÔNIBUS'):
                onibus.Onibus(0,0,0,0,0).novo_onibus()
                print('Ônibus cadastrado')

            elif cl.upper() == ('USUARIO' or 'USUÁRIO'):
                user.Usuario(0,0,0,0,0,0).novo_usuario()
                print('usuário cadastrado')

            elif cl.upper() == 'SAIR':
                break

            else:
                print(RED+ 'Selecione uma classe válida'+RESET)

    elif acao.upper() == 'CONSULTAR':

        while True:
            cl = input('O que deseja consultar? \n digite sair para sair')

            if cl.upper() == ('USUARIO' or 'USUÁRIO'):
                user.Usuario(0, 0, 0, 0, 0, 0).select_usuario()

            elif cl.upper() == ('CARTAO' or 'CARTÃO'):
                cartao.Cartao(0, 0, 0, 0, 0).select_cartao()

            elif cl.upper() == 'MOTORISTA':
                motorista.Motorista(0, 0, 0, 0, 0).select_motorista()

            elif cl.upper() == ('ONIBUS' or 'ÔNIBUS'):
                onibus.Onibus(0, 0, 0, 0, 0).select_onibus()

            elif cl.upper() == 'SAIR':
                break

            else:
                print(RED + 'Selecione uma classe válida' + RESET)
    else:
        print(RED+'Digite uma ação válida'+ RESET)
print('Finalizando...')
