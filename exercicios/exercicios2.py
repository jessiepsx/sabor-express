class Musica:
    musicas = []

    def __init__(self, nome_musica, artista, duracao):
        self.nome_musica = nome_musica
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome_musica} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for  musica in Musica.musicas:
            print(f'{musica.nome_musica} | {musica.artista} | {musica.duracao}')

musicas_pop = Musica('God is a Woman','Ariana Grande', 239)
Musica.listar_musicas()

# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro: 
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
# Instanciando um carro e atribuindo valores aos seus atributos
carro1 = Carro('civic', 'rosa', 2007 )

# 2) Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, estado, avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.estado = estado
        self.avaliacao = avaliacao
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante1 = Restaurante('Praça', 'Tradicional', 'SP', '5,3')

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Praca', categoria='Tradicional' , estado='SP', avaliacao='5,3')
print(restaurante_formatado)


# 5) Crie uma classe chamada `Cliente` e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, altura, telefone):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente('Jess', 18, 1.55, '119273-69275')
cliente2 = Cliente(nome='Bob', idade=30, altura= 1.67, telefone='987-654-3210')

class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        if self.profissao:
            return print(f'Olá, sou {self.nome}! Trabalho como {self.profissao}')
        else:
            return f'Olá, sou {self.nome}!'

# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22, profissao= '')

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)