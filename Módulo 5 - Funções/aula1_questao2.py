import random
import math

# Solicita ao usuário a quantidade de números a serem gerados
n = int(input("Digite a quantidade de números a serem gerados: "))

# Lista para armazenar os números gerados
valores = []

# Gera n números aleatórios entre 0 e 100 e os adiciona à lista
for _ in range(n):
    numero = random.randint(0, 100)
    valores.append(numero)

# Calcula a soma dos valores
soma = sum(valores)

# Calcula a raiz quadrada da soma
raiz_quadrada = math.sqrt(soma)

# Exibe os valores gerados
print("Valores gerados:", valores)

# Exibe a raiz quadrada da soma
print(f"A raiz quadrada da soma dos valores é: {raiz_quadrada:.2f}")
