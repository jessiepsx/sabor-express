# 8- Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

from carro import Carro
from moto import Moto

carro1 = Carro("Toyota", "Corolla", 4)
carro2 = Carro("Honda", "Civic", 2)
carro3 = Carro("Ford", "Fusion", 4)

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "MT-09", "Esportiva")

print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)