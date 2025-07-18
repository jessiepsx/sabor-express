# 1) Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:

    livros = []
    def __init__(self, autor,titulo, ano_publicacao):
        self._autor = autor
        self._titulo = titulo
        self._ano_publicacao = ano_publicacao
        self._disponivel= True
        Livro.livros.append(self)

# 2) Na classe Livro, adicione um método especial __str__ que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}' 


# 3) Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.   
    def emprestar(self):
        self._disponivel = False 

# 4) Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis
    
livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
livro3 = Livro('Python', 'Jess', 2021)

print(f"Antes de emprestar: Livro disponível? {livro3._disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3._disponivel}")

Livro.livros = [livro1, livro2, livro3] 