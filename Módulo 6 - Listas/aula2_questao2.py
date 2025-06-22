# Soma e média de lista com tamanho aleatório
import random

# Número de elementos entre 5 e 20
num_elementos = random.randint(5, 20)

# Gera os valores entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma = sum(elementos)
media = soma / len(elementos)

print("Lista de elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", round(media, 2))
