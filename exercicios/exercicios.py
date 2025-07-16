nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
print (f'Meu nome é {nome} e tenho {idade} anos')

#-------------------------------------------------------------

print ('A\n')
print ('L\n')
print ('U\n')
print ('R\n')
print ('A\n')

#-------------------------------------------------------------

pi = 3.14159
print (f'O valor arredondado de pi é: {pi:.2f}')

#-------------------------------------------------------------

#print('A','L','U','R','A',sep='\n')
# O separador sep é definido como \n, que representa uma quebra de linha.

# Abordagem de f-string
#print(f'O valor arredondado de pi é: {pi:.2f}')

#-------------------------------------------------------------

numero = int(input('digite um número: '))
if numero % 2 == 0:
    print('o numero é par')

else:
    print("o numero é impar")

#-------------------------------------------------------------

idade = int(input("digite sua idade: "))
if 0 < idade <= 12:
    print("Criança")

elif 12 < idade < 18:
    print('adolescente')

elif idade >= 18:
    print("Adulto")

else: 
    print("Valor inválido!")

#-------------------------------------------------------------

nome_correto = "alura"
senha_correta = "alura123"

nome = input('digite seu nome de usuario: ')
senha = input("digite sua senha: ")

if nome == nome_correto and senha == senha_correta:
    print("Login bem sucedido!")

else:
    print("Credenciais inválidas. Tente novamente.")

#-------------------------------------------------------------

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")

#-------------------------------------------------------------

# Crie uma lista para cada informação a seguir:
numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['jess','bia','deb','joao']
nascimento = [2007,2025]

#Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print (numero)

#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
impares = 0
for i in range (1,11,2):
    impares += i
    print(impares)

#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for i in range(10,0,-1):
    print (i)

#utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
tabuada = int(input('Digite um número para a tabuada: '))
for i in range(1,11):
    resultado = tabuada * i
    print(f'{tabuada} x {i} = {resultado}')


#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
lista_numeros = [10, 5, 8, 3, 7]
try:
    soma = sum(lista_numeros)
    print(f"Soma dos elementos: {soma}")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

# Construa um código que calcule a média dos valores em uma lista.
valores = [15, 20, 25, 30]
try:
    media = sum(valores) / len(valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#-------------------------------------------------------------