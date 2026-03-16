habitos = []

while True:
    print("\nControle de Hábitos - Habit Tracker")
    print("1. Adicionar hábito")
    print("2. Ver hábitos")
    print("3. Marcar hábito")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novoHabito = input("Digite o nome do hábito: ")
        habitos.append(novoHabito)
        print("Hábito adicionado com sucesso!")

    elif opcao == "2":
        print("\nSeus hábitos:")

        if not habitos:
            print("Nenhum hábito cadastrado.")
        else:
            for numero, habito in enumerate(habitos, start=1):
                print(numero, "-", habito)

    elif opcao == "3":
        if not habitos:
            print("Nenhum hábito para marcar.")
            continue

        print("\nEscolha o hábito para marcar:")

        for numero, habito in enumerate(habitos, start=1):
            print(numero, "-", habito)

        numero = input("Qual número você quer marcar? ")

        if numero.isdigit():
            numero = int(numero)
            indice = numero - 1

            if 0 <= indice < len(habitos):
                habitos[indice] = habitos[indice] + " ✅"
                print("Hábito marcado!")
            else:
                print("Número inválido.")
        else:
            print("Digite apenas números.")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida.")