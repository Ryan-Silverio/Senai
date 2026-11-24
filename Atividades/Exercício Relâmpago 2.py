#1 - Hierarquia Veículo
class Veiculo: #Classe base
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max

    def mover(self): 
        print("O veículo está se movendo")

class Carro(Veiculo): #Subclasse
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas

class Bicicleta(Veiculo): #Subclasse
    def __init__(self, marca, velocidade_max, num_marchas):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas

#Criando objetos.
carro1 = Carro("Toyota", 180, 4)
bicicleta1 = Bicicleta("Caloi", 40, 21)

#Menu.
print("-" * 50)
print("| Informações do Carro |")
print("Marca do carro:", carro1.marca)
print("Velocidade máxima do carro:", carro1.velocidade_max)
print("Número de portas do carro:", carro1.num_portas)
print("-" * 50)

print("| Informações da Bicicleta |")
print("Marca da bicicleta:", bicicleta1.marca)
print("Velocidade máxima da bicicleta:", bicicleta1.velocidade_max)
print("Número de marchas da bicicleta:", bicicleta1.num_marchas)
print("-" * 50)

#2 - Figuras Geométricas
class Figura:  #Classe base
    def calcular_area(self):
        pass  #Método que será implementado nas subclasses

class Retangulo(Figura):  #Subclasse
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Circulo(Figura):  #Subclasse
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)


#Lista com figuras mistas
figuras = [
    Retangulo(5, 10),
    Circulo(3),
    Retangulo(4, 6),
    Circulo(5)
]

#Polimorfismo: cada figura calcula sua própria área
for figura in figuras:
    print(f"Área: {figura.calcular_area():.2f}")



#3 - Funcionários
class Funcionario:  #Classe base
    def __init__ (self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

class Gerente(Funcionario):  #Subclasse
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
        self.bonus = salario_base * 0.20

    def calcular_salario(self):
        return self.salario_base + self.bonus

class Estagiario(Funcionario):  #Subclasse
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_salario(self):
        return self.salario_base

#Criando objetos.
funcionario1 = Funcionario("Carlos", 3000)
gerente1 = Gerente("João", 5000)
estagiario1 = Estagiario("Maria", 1500)

#Menu.
print("-" * 50)
print("| Informações do Funcionário |")
print("Nome do funcionário:", funcionario1.nome)
print("Salário base do funcionário:", funcionario1.salario_base)
print("-" * 50)

print("| Informações do Gerente |")
print("Nome do gerente:", gerente1.nome)
print("Salário base do gerente:", gerente1.salario_base)
print("Salário total do gerente (com bônus):", gerente1.calcular_salario())
print("-" * 50)

print("| Informações do Estagiário |")
print("Nome do estagiário:", estagiario1.nome)
print("Salário base do estagiário:", estagiario1.salario_base)
print("Salário total do estagiário:", estagiario1.calcular_salario())
print("-" * 50)