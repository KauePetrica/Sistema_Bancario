menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair
=>"""


saldo = 0
limite = 500
extrato =""
numero_de_saques = 0
limite_de_saques = 3


while True:
    opcao = input(menu)
    if opcao == "d":
            valor=float(input("Digite o valor do depósito:"))
            if valor>0:
                saldo+=valor
                extrato+= f"Depósito: R$ {valor:.2f}\n"
            else:
                print("A operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))
        excedeu_saldo = valor>saldo
        excedeu_limite = valor>limite
        excedeu_saques = numero_de_saques >= limite_de_saques
        
        
        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente para essa transação") 
        elif excedeu_limite:
            print("Operação falhou! Você não possui limite suficiente para essa transação") 
        elif excedeu_saques:
            print("Operação falhou! Limite diário de saques atingido") 
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n========== Extrato ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
