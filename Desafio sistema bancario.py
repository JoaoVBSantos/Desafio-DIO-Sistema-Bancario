menu = '''

[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair

-- '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = str(input(menu))

    opcao = opcao.upper()

    if opcao == 'D':
        valor = int(input('Digite o valor para depósito'))
        validacao = str(input(f'Deseja realmente realizar um deposito de R$ {valor:.2f}? S ou N'))

        if validacao.upper() == 'S':
            saldo += valor
            print(f'Deposito de R$ {valor:.2f} realizado com sucesso!')
            extrato += f'Deposito efetuado de R$ {valor:.2f} - Saldo R$ {saldo:.2f}\n'

        elif validacao.upper() == 'N':
            print('Opereção não realizada')

        else:
            print('Opcão inválida')

    elif opcao == 'S':
        valor = int(input('Digite o valor de saque: '))

        if numero_saques == LIMITE_SAQUES:
            print('Você excedeu seu limite de saques hoje.')

        elif valor > limite:
            print('Valor acima do limite de saque.')

        else:
            validacao = str(input(f'Tem certeza que quer efetuar um saque de R$ {valor:.2f}? S ou N'))
            if validacao.upper() == 'S':
                if valor > saldo:
                    print('Você não tem saldo suficiente!')

                else:
                    saldo -= valor
                    print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
                    numero_saques += 1
                    extrato += f'Saque efetuado de R$ {valor:.2f} - Saldo R$ {saldo:.2f}\n'

            elif validacao == 'N':
                print('Operação não realizada!')

            else:
                print('Opcão inválida')

    elif opcao == 'E':
        print('''
========== Extrato ==========
    ''')
        print(extrato)

        print(f'Saldo final: R${saldo:.2f}')
        print('==================')

    elif opcao == 'Q':
        exit()
