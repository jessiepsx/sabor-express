class Veiculo:
    def __init__(self,marca,modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

# 2- Construa o Método Especial __str__: Adicione um método especial __str__ à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'marca: {self._marca}, modelo: {self._modelo}, status: {status}'