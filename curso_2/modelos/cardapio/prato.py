# Importando a classe ItemCardapio, que é a classe base
from .item_cardapio import ItemCardapio

# Definindo a classe Prato que herda de ItemCardapio
class Prato(ItemCardapio):
    def __init__(self,nome, preco,descricao):

# Chamando o construtor da classe base para inicializar nome e preço
        super().__init__(nome,preco)
        self.descricao=descricao

    def __str__(self):
            return self._nome
    
    def aplicar_desconto(self):
        self._preco -=  (self._preco * 0.05)


#Super permite acesso a informaçoes de outra classe
#Quando você cria uma subclasse, pode querer inicializar atributos que estão definidos na classe pai. Usando super().__init__(...), você chama o construtor da classe pai, garantindo que todos os atributos necessários sejam configurados corretamente.