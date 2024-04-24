from actions.operations import deposit_values, extract_values, withdraw_value

options = '''
Bem-vindo ao banco .py

Escolha uma opção:

1- Depositar
2- Saque
3- Extrato
4- Encerrar
'''

deposits = []

while True:
    opt_chosen = input(options)

    if opt_chosen == '1':
        deposits += deposit_values()
           
    elif opt_chosen == '2':
        deposits = withdraw_value(deposits)

    elif opt_chosen == '3':
        extract_values(deposits)

    elif opt_chosen == '4':
        print('Encerrando o programa. Obrigado por usar nosso banco .py!')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')

        