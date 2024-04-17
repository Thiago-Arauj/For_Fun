contador = 0
extrato_saque = []
extrato_deposito = []
saldo = 0.0

def saque(contador, saldo, extrato_saque):
    limite_valor_saque = 500.00
    limite_diario = 3
    sacou = 1
    while sacou:
        if contador < limite_diario:
            valor_saque = float(input('Quanto deseja sacar? '))
            if valor_saque > saldo:
                print(f'Você está sem saldo para essa operação \n Seu saldo é de R$ {saldo:.2f}')
            elif valor_saque <= limite_valor_saque:
                print(f'Você sacou com sucesso o valor de R$ {valor_saque:.2f}')
                extrato_saque.append(valor_saque)
                sacou = 0
                contador += 1
            else:
                print('O limite de saque por operação é de R$ 500.00')
        else:
            print('Você já excedeu o limite diário de saques')
            break
    
    return extrato_saque

def deposito (extrato_deposito):
    entrada = float(input('Quanto deseja depositar? '))
    extrato_deposito.append(entrada)
    return extrato_deposito

def puxar_extrato (saldo, extrato_saque, extrato_deposito):
    print(f'Seu saldo é de R$ {saldo} \n')
    print('Depósitos')
    for j in extrato_deposito:
        print(f'R$ {j:.2f}')
    print('Saques:')
    for i in extrato_saque:
        print(f'R$ {i:.2f}')
    
    

def att_saldo(saldo, extrato_saque,extrato_deposito):
    soma = 0
    subtracao = 0

    for i in extrato_deposito:
        soma += i
    
    for j in extrato_saque:
        subtracao += j

    saldo = soma - subtracao

    return saldo


while True:
    
    menu = int(input('''
Qual operação deseja realizar?
[1] Saque
[2] Depósito
[3] Extrato
[0] Nenhuma
'''))

    if menu == 1:
        saque(contador, saldo, extrato_saque)
        contador += 1
    elif menu == 2:
        deposito(extrato_deposito)
    elif menu == 3:
        puxar_extrato(saldo, extrato_saque, extrato_deposito)
    elif menu == 0:
        break
    elif menu > 3:
        print('Selecione uma operação válida')
        continue

    saldo = att_saldo(saldo, extrato_saque, extrato_deposito)