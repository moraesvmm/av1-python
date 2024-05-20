print('''Seja bem vindo ao nosso sistema bancário!
      Qual das operações deseja realizar?

      ============================================
      
      1. Saque.
      2. Depósito.
      3. Extrato.
      4. Sair''')

SALDO = 0  # Saldo inicial
LIMITE_SAQUES_DIA = 3
LIMITE_SAQUE = 500
QUANTIDADE_SAQUES_DIA = 0
extrato = []

while True:
    opcao = input("Por favor, selecione uma opção acima com o referendo número.\n")

    if opcao == "1": 
        if QUANTIDADE_SAQUES_DIA >= LIMITE_SAQUES_DIA:
            print("Desculpe, você atingiu o limite máximo de saques para hoje.\n")
        else:
            saque = float(input("Qual o valor do saque?\n"))
            if saque > SALDO:
                print("Desculpe, você não tem saldo suficiente para realizar este saque.\n")
            elif saque > LIMITE_SAQUE:
                print("Desculpe, você excedeu o limite de saque.\n")
            else:
                SALDO -= saque
                QUANTIDADE_SAQUES_DIA += 1
                extrato.append(f"Saque de R${saque:.2f}")
                print(f"Você sacou R${saque:.2f}. Seu novo saldo é R${SALDO:.2f}.\n")
    elif opcao == "2": 
        deposito = float(input("Qual o valor do depósito?\n"))
        SALDO += deposito
        extrato.append(f"Depósito de R${deposito:.2f}")
        print(f"Você acaba de depositar R${deposito:.2f} em sua conta bancária. Seu novo saldo é R${SALDO:.2f}.\n")
    elif opcao == "3":
        print("Extrato:")
        for operacao in extrato:
            print(operacao)
        print(f"Saldo atual: R${SALDO:.2f}\n")
    elif opcao == "4":
        print("Ok, até mais!")
        break
    else:
        print("Opção inválida. Por favor, selecione uma opção válida.\n")

