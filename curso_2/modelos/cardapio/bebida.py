# Definindo a classe Bebida que também herda de ItemCardapio
from .item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome,preco,tamanho):
# Chamando o construtor da classe base para inicializar nome e preço
        super().__init__(nome,preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome 
    
    def aplicar_desconto(self):
        #self.preco = self._preco - (self._preco * 0.05)
        self._preco -=  (self._preco * 0.08)