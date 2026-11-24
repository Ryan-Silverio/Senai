def celsius_para_fahrenheit(c): #Conversão de Celsius para Fahrenheit
    return (c * 9 / 5) + 32

def km_para_milhas(km): #Conversão de km para milhas
    return km * 0.621371

def kg_para_libras(kg): #Conversão de kg para libras
    return kg * 2.20462

def calcular_area_retangulo(base, altura): #Calcula a área de um retângulo
    return base * altura

def maior_de_tres(a, b, c): #Retorna o maior de três números
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def eh_primo(n): #Verifica se um número é primo
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    print("Escolha a conversão desejada: ") #Menu
    print("1 - Celsius para Fahrenheit")
    print("2 - Km para Milhas")
    print("3 - Kg para Libras")
    print("4 - Calcular area retangulo")
    print("5 - Maior de três números")
    print("6 - Verificar se um número é primo")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1": #Celsius para Fahrenheit
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit}")

    elif opcao == "2": #Km para Milhas
        km = float(input("Digite a distância em Km: "))
        milhas = km_para_milhas(km)
        print(f"A distância em Milhas é: {milhas}")

    elif opcao == "3": #Kg para Libras
        kg = float(input("Digite o peso em Kg: "))
        libras = kg_para_libras(kg)
        print(f"O peso em Libras é: {libras}")

    elif opcao == "4": #Calcular área do retângulo
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = calcular_area_retangulo(base, altura)
        print(f"A área do retângulo é: {area}")

    elif opcao == "5": #Retorna o maior de três números
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        c = float(input("Digite o terceiro número: "))
        maior = maior_de_tres(a, b, c)
        print(f"O maior número é: {maior}")

    elif opcao == "6": #Verifica se um número é primo
        n_ = int(input("Digite um número inteiro: "))
        if eh_primo(n_):
            print(f"O número {n_} é primo.")
        else:
            print(f"O número {n_} não é primo.")

    else:
        print("Opção inválida!")

    continuar = input("Deseja fazer outra conversão? (s/n): ")
    if continuar.lower() != "s":
        break