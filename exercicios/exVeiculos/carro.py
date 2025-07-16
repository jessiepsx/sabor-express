from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca,modelo,portas):
        super().__init__(marca,modelo)
        self._portas = portas

# 4- Implemente o Método Especial __str__ na Classe Filha: Adicione um método especial __str__ à classe Carro que estenda o método da classe pai (Veiculo).

    def __str__(self):
        return f"{super().__str__()} - Portas: {self._portas}"