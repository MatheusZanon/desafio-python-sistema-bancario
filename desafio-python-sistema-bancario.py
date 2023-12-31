menu = """\n
================ MENU ================
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[0]\tSair =>
====================================== 
    """
saldo = 0
limite_saque = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    try:
        opcao = int(input(menu))

        if opcao == 1:
            valor = float(input("Informe o valor que deseja depositar: "))
            
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor inserido é inválido!")

        elif opcao == 2:
            valor = float(input("Informe o valor desejado do saque: "))
        
            if valor > 500:
                print("Operação falhou! O valor inserido é maior do que R$500,00!")
            elif valor > saldo:
                print("Operação falhou! Você não possue essa quantia disponível para saque!")
            elif numero_saque > LIMITE_SAQUES:
                print("Operação falhou! Você atingiu o limite de saques diários! Tente de novo amanhã.")
            elif valor > 0 and valor < saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1
            
        elif opcao == 3:
            print("=============== EXTRATO ===============")
            print("Não há registros." if not extrato else extrato)
            print(f"\nSaldo Atual: R$ {saldo:.2f}")
            print("=======================================")

        elif opcao == 0:
            break

        else:
            print("Opção inválida! Por favor selecione uma opção válida do menu.")
    
    except:
        print("Operação inválida. Insira um valor válido!")