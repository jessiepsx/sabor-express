from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{"Nome do restaurante".ljust(17)} | {"Categoria".ljust(17)} | {"Avaliação".ljust(17)} | {"Status"}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(19)} | {restaurante._categoria.ljust(17)} | {str(restaurante.media_avaliacoes).ljust(17)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

# Verifica se o item a ser adicionado é uma instância da classe itemCardapio ou de suas subclasses.
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):

            # hasattr(objeto, 'atributo') verifica se o 'objeto' possui um atributo chamado 'atributo'.
            
            # Retorna True se o atributo existir e False caso contrário, sendo útil para evitar erros ao acessar atributos.
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)

            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
                    



# Sempre que pensarmos em uma classe, temos que pensar quais são os atributos, ou seja, as características dessa entidade que queremos criar. Vamos supor que queremos criar uma entidade chamada pessoa, então precisamos pensar nas características de uma pessoa que queremos dentro de um sistema, como o RG e o CPF.

# O dir() mostrará tudo: os atributos, métodos e propriedades de um objeto. Quando o substituímos por vars(), queremos um dicionário desses atributos e métodos

# __init__ → É o construtor da classe. Serve para criar e inicializar os atributos de um objeto. 
# Tradução simples: "O que precisa ser definido quando um objeto for criado?"

# __str__ → Define como o objeto será exibido ao usar print()Serve para mostrar uma versão “bonita” e legível do objeto.
#Tradução simples: "O que eu quero que apareça quando alguém usar print nesse objeto?"