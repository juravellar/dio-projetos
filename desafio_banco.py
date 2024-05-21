menu = """

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    try:
        opcao = int(input(menu))
        
        if opcao == 1:
            valor = float(input("Qual valor deseja depositar? R$ "))
            
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor: .2f}\n"
                print(f"Depósito de R$ {valor: .2f} realizado com sucesso!")
            else:
                print("Operação falhou: valor inválido") 
        
        elif opcao == 2:
            valor = float(input("Qual valor deseja sacar? R$ "))
            
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print("Operação falhou: saldo insuficiente")
            
            elif excedeu_limite:
                print("Operação falhou: limite de saque excedido")
            
            elif excedeu_saques:
                print("Operação falhou: limite de saques excedido")
                
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor: .2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor: .2f} realizado com sucesso!")
                
            else:
                print("Operação falhou: valor inválido")
        
        elif opcao == 3:
            print("\n******************** EXTRATO ********************")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo: R$ {saldo: .2f}")
            print("*************************************************")
        
        elif opcao == 0:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Por favor, selecione novamente a operação desejada!")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
