def exibir_menu():
    return """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """


def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")


def sacar(conta, valor):
    if valor > conta["saldo"]:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif valor > conta["limite"]:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif conta["numero_saques"] >= conta["LIMITE_SAQUES"]:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        conta["numero_saques"] += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    if conta["extrato"]:
        print("\n".join(conta["extrato"]))
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================\n")


def main():
    conta = {
        "saldo": 0,
        "limite": 500,
        "extrato": [],
        "numero_saques": 0,
        "LIMITE_SAQUES": 3
    }

    while True:
        opcao = input(exibir_menu()).strip().lower()

        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: "))
            depositar(conta, valor)

        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: "))
            sacar(conta, valor)

        elif opcao == "e":
            exibir_extrato(conta)

        elif opcao == "q":
            print("\nObrigado por utilizar nosso sistema. Até logo!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
