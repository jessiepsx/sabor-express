from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca,modelo,tipo):
        super().__init__(marca,modelo)
        self._tipo = tipo

# 6- Implemente o Método Especial __str__ na Classe Filha (Moto): Adicione um método especial __str__ à classe Moto que estenda o método da classe pai (Veiculo).
    def __str__(self):
        return f"{super().__str__()} - Tipo: {self._tipo}"