def deposit_values():
    arrDeposits = []
    
    while True:
        value = input('Qual valor você quer depositar ? (Digite "sair" para finalizar)\n')
        if value.lower() == 'sair':
            break 
        arrDeposits.append(float(value))
    return arrDeposits

def withdraw_value(deposits):
    withdrawa_limit = 0  
    balance = sum(deposits)

    if deposits:
        while True:
            print(f'Saldo disponivel para saque: R$ {balance}'.replace('.', ','),)
            value = float(input('Qual o valor do saque:'))

            if withdrawa_limit > 3:
                print('Excedeu o limite de 3 saques. Tente novamente mais tarde!')
                break

            if value > 500:
                print('Valor do saque não pode ser maior que R$ 500,00')
                break

            balance -= value
            withdrawa_limit +=1
            print('withdrawa_limit: ', withdrawa_limit)

            print('============ SAQUE REALIZADO COM SUCESSO! ============')
            print(f'Saldo Atual: R$ {balance}')
        return [balance] 
                       
    else:
        print('Nenhum valor para sacar.')


def extract_values(deposits):
    if deposits:        
        print('Valores depositados:')
        for deposit in deposits:
            print(f'R$ {deposit}'.replace('.', ','))
        print('=======================')    
        print(f'Total R$: {sum(deposits)}'.replace('.', ','),)    
    else:
        print('Nenhum valor depositado ainda.')
