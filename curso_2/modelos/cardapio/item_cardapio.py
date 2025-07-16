from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass

# ABC (Abstract Base Class) permite criar classes base abstratas que definem métodos obrigatórios para subclasses.

# O decorador @abstractmethod indica que um método deve ser implementado nas classes que herdam dessa classe abstrata.

# Polimorfismo: permite que o mesmo método, chamado 'aplicar_desconto', 
# tenha implementações diferentes em classes distintas (como 'Bebida' e 'Prato').

# Assim, cada classe pode aplicar seu próprio cálculo de desconto, 
# mesmo que o método tenha o mesmo nome.