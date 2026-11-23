class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

ex1 = Carro("Toyota", "Corolla", 2020)
ex2 = Carro("Honda", "Civic", 2021)

ex1.exibir()
print("-" * 20)
ex2.exibir()

class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def get_saldo(self):
        return self.__saldo    
    
print("-" * 20)

ex1 = Conta(100)
ex1.depositar(50)
print(ex1.get_saldo())

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, qtd):
        if qtd <= self.estoque:
            self.estoque -= qtd
            print(f"Venda realizada! Estoque atual: {self.estoque}")
        else:
            print("Estoque insuficiente.")

ex1 = Produto("Notebook", 3000, 10)

print("-" * 20)

ex1.vender(5)
ex1.vender(6)