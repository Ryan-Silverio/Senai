class Livro:
    # Construtor da classe Livro
    def __init__(self, titulo, autor, paginas, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = disponivel

    def descricao(self):
        # Exibe as informações do livro
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print(f"Disponível: {'Sim' if self.disponivel else 'Não'}")

    def emprestar(self):
        # Verifica se o livro está disponível
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        # Altera o status de disponibilidade do livro para disponível
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível na biblioteca.")


# Criação do objeto
ex1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1178, True)

# Chamadas dos métodos
print("-" * 50)

ex1.descricao()

print("-" * 50)

ex1.emprestar()

print("-" * 50)

# Verifica a disponibilidade após o empréstimo
ex1.descricao()

print("-" * 50)

#Devolvendo o livro
ex1.devolver()

print("-" * 50)

# Verifica a disponibilidade após a devolução
ex1.descricao()