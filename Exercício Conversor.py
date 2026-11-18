def celsius_para_fahrenheit(c): #Conversão de Celsius para Fahrenheit
    return (c * 9 / 5) + 32

def km_para_milhas(km): #Conversão de km para milhas
    return km * 0.621371

def kg_para_libras(kg): #Conversão de kg para libras
    return kg * 2.20462

while True:
    print("Escolha a conversão desejada: ") #Menu
    print("1 - Celsius para Fahrenheit")
    print("2 - Km para Milhas")
    print("3 - Kg para Libras")

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
    else:
        print("Opção inválida!")

    continuar = input("Deseja fazer outra conversão? (s/n): ")
    if continuar.lower() != "s":
        break

