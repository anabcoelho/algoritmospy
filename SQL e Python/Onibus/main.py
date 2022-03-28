
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

#vamo conectar logo
import conectar
conexao = conectar.conectar()
cursor = conexao.cursor()

while True:
    acao = input('O que deseja fazer? \n Cadastrar, consultar dados, atualizar ou sair?')

    if acao.upper() == 'SAIR':
        break


    elif acao.upper() == 'CADASTRAR':

        while True:
            cl=input('O que deseja cadastrar?\n digite sair para sair')

            if cl.upper() == ('CARTAO' or 'CARTÃO'):
                import conectar
                from datetime import datetime

                card=cartao.Cartao(0,0,0,0,0)
                RED = "\033[1;31m"
                RESET = "\033[0;0m"

                id_cartao = int(input('Qual o ID do cartão?'))
                card.set_id_cartao(id_cartao)
                id_user = int(input('Informe o ID do proprietário'))
                card.set_id_user(id_user)
                creditos = float(input('Quantos créditos?'))
                card.set_creditos(creditos)


                tipo = input('Qual o tipo do cartão? \n Comum, estudante, vale-transporte ou idoso?')
                # conferindo o tipo.
                tipos_passageiros = ['COMUM', 'ESTUDANTE', 'VALE-TRANSPORTE', 'IDOSO']
                while True:
                    if tipo.upper() not in tipos_passageiros:
                        tipo = input(RED + 'Insira um tipo válido' + RESET +
                                     '\n Comum, estudante, vale-transporte ou idoso?')
                    elif tipo.upper() == 'ESTUDANTE' or tipo.upper() == 'IDOSO':
                        print("checando informações")

                        idade=cartao.Cartao.checar_tipo(0,cursor)

                        if tipo.upper() == "IDOSO" and idade < 60:
                            print(f'passageiro tem {idade} anos, não é apto para essa modalidade')
                            tipo = input(RED + 'Insira um tipo válido, e autorizado' + RESET)
                        if tipo.upper() == "ESTUDANTE" and idade > 21:
                            docum = input('Conferir documentação de estudante \n é válida? s/n')
                            if docum.upper() == 'S':
                                break
                            else:
                                tipo = input(RED + 'Insira um tipo válido, e autorizado' + RESET)
                    elif tipo.upper() in tipos_passageiros:
                        break
                card.set_tipo(tipo)
                data_emissao = datetime.today().strftime('%Y-%m-%d')
                card.set_data_emissao (data_emissao)

                card.insert_cartao(cursor)

                print('Cartão cadastrado')
                break

            elif cl.upper() == 'MOTORISTA':

                mot=motorista.Motorista(0,0,0,0,0)
                RED = "\033[1;31m"
                RESET = "\033[0;0m"

                id_motorista = int(input('Informe o ID do motorista'))
                mot.set_id_motorista(id_motorista)

                nCNH = int(input('Informe CNH do motorista'))
                while len(str(nCNH)) != 11:
                    nCNH = int(input(f'{RED}Insira um número de CNH válido (11 dígitos): {RESET}'))
                mot.set_CNH(nCNH)

                nome = input('Informe o nome do proprietário ')
                mot.set_nome(nome)
                sobrenome = input('Informe o sobrenome do proprietário')
                mot.set_id_sobrenome(sobrenome)
                data_nascimento = input('Informe a data de nascimento \n formato: aaaa-mm-dd')
                mot.set_data_nascimento(data_nascimento)

                mot.insert_motorista(cursor)
                print('motorista cadastrado')
                break

            elif cl.upper() == ('ONIBUS' or 'ÔNIBUS'):
                bus=onibus.Onibus(0,0,0,0,0)
                placa = int(input('Informe o número da placa'))
                bus.set_placa(placa)
                linha = int(input('Informe o número da linha '))
                bus.set_linha(linha)
                modelo = input('Informe o modelo do ônibus')
                bus.set_modelo(modelo)
                ano = input('Informe o ano do õnibus (4 dígitos)')
                bus.set_ano(ano)
                id_motorista = int(input('Informe o ID do motorista'))
                bus.set_id_motorista(id_motorista)

                bus.insert_onibus(cursor)

                print('Ônibus cadastrado')
                break

            elif cl.upper() == ('USUARIO' or 'USUÁRIO'):
                U=user.Usuario(0,0,0,0,0,0)
                id_user = int(input('Informe o ID do usuário'))
                U.set_id_user(id_user)
                nome = input('Informe o nome do usuário ')
                U.set_nome(nome)
                sobrenome = input('Informe o sobrenome do usuário')
                U.set_sobrenome(sobrenome)
                email = input('Informe o email do usuário')
                U.set_email(email)
                bairro = input('Informe o bairro do usuário')
                U.set_bairro(bairro)
                data_nascimento = input('Informe a data de nascimento \n formato: aaaa-mm-dd')
                U.set_data_nascimento(data_nascimento)
                U.insert_usuario(cursor)


                print('usuário cadastrado')
                break

            elif cl.upper() == 'SAIR':
                break
            else:
                print(RED+ f'{RED} Selecione uma classe válida {RESET}')



    elif acao.upper() == 'CONSULTAR':


        while True:
            cl = input('O que deseja consultar? \n digite sair para sair')

            if cl.upper() == 'SAIR':
                break

            save = input('Deseja salvar um CSV da consulta? sim ou não')


            if cl.upper() == ('USUARIO' or 'USUÁRIO'):
                usu = user.Usuario
                retornou = usu.select_usuario(0,cursor)
                print(retornou[1])
                for row in retornou[0]:
                    print(row)

                if save.upper() == 'SIM':
                    import salvarcsv
                    salvarcsv.salvar_csv(cl, retornou[0], retornou[1])
                break


            elif cl.upper() == ('CARTAO' or 'CARTÃO'):

                card = cartao.Cartao
                retornou = card.select_cartao(0, cursor)
                print(retornou[1])
                for row in retornou[0]:
                    print(row)

                if save.upper() == 'SIM':
                    import salvarcsv

                    salvarcsv.salvar_csv(cl, retornou[0], retornou[1])
                break

            elif cl.upper() == 'MOTORISTA':
                mot=motorista.Motorista
                retornou = mot.select_motorista(0,cursor)
                print(retornou[1])
                for row in retornou[0]:
                    print(row)

                if save.upper() == 'SIM':
                    import salvarcsv

                    salvarcsv.salvar_csv(cl, retornou[0], retornou[1])
                break

            elif cl.upper() == ('ONIBUS' or 'ÔNIBUS'):
                on=onibus.Onibus
                retornou = on.select_onibus(0,cursor)
                print(retornou[1])
                for row in retornou[0]:
                    print(row)

                if save.upper() == 'SIM':
                    import salvarcsv

                    salvarcsv.salvar_csv(cl, retornou[0], retornou[1])
                break



            else:
                print(f'{RED} Selecione uma classe válida {RESET}')
    elif acao.upper() == 'ATUALIZAR':
        while True:
            cl=input('O que deseja atualizar? \n bairro ou créditos')
            if cl.upper() == 'BAIRRO':
                id_user= int(input('Insira o ID do usuário '))
                bairro=input('Qual é o novo bairro? ')
                user.Usuario.atualizar_bairro(0,bairro,id_user,cursor)
                break

            elif cl.upper() == ('CREDITOS' or 'CRÉDITOS'):
                id_cartao=int(input('Informe o ID do cartão: '))
                c=float(input('Quantos créditos foram adicionados? '))
                cartao.Cartao.atualizar_saldo(0,id_cartao,c,cursor)
                break

            else:
                print('Tente de novo')
    else:
        print(f'{RED} Digite uma ação válida {RESET}')

conectar.desconectar(cursor, conexao)
print('Finalizando...')
