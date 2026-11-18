print("-" * 30)

def saudar(nome):
    print(f"Olá, {nome}! Bem-vindo(a)!")

saudar("Ana")
saudar("Bruno")
saudar("Carlos")

print("-" * 30)

def estatisticas(nums):
    total = sum(nums)
    media = total / len(nums)
    return total, media

t, m = estatisticas([8, 9, 7])
print(f"Total: {t}, Média: {m:.2f}")

print("-" * 30)

def somar (a, b): return a + b
def subtrair (a, b): return a - b
def multiplicar (a, b): return a * b
def dividir (a, b):
        if b == 0: return "Erro!"
        return a / b

while True:
    op = input("Escolha a operação (+, -, *, /) ou '0' para encerrar: ")
    if op == '0':
        print("Encerrando o programa...")
        break
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    if op == '+':
        print(f"Resultado: {somar(a, b)}")
    elif op == '-':
        print(f"Resultado: {subtrair(a, b)}")
    elif op == '*':
        print(f"Resultado: {multiplicar(a, b)}")
    elif op == '/':
        print(f"Resultado: {dividir(a, b)}")
