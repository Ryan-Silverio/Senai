while True:
    print("1 - Par ou Ímpar")
    print("2 - Múltiplos de 3")
    print("3 - Média de Notas")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1: #Par ou Ímpar

        n = int(input("Digite um número inteiro: "))

        if n % 2 == 0:
            print(f"O número {n} é par.")
        else:
            print(f"O número {n} é ímpar.")
    
    if opcao == 2: #Múltiplos de 3

        for n in range(1, 51):
            if n % 3 == 0:
                print(n)
                
    if opcao == 3: #Média de Notas

        n = [float(input(f"Nota do aluno {i+1}: ")) for i in range(3)]

        print("\n===== RESULTADO DOS ALUNOS =====")
        print("--------------------------------")

        for i, nota in enumerate(n):
            if nota >= 7:
                situacao = "Aprovado"
            elif nota >= 5:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

        print(f"| Aluno {i+1} | Nota: {nota:.1f} | {situacao} |")
        print("--------------------------------")

    if opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")