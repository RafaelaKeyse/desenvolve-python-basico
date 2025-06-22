# Lista com 20 valores entre -100 e 100
import random

# Gera 20 valores entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Lista ordenada (sem alterar a original)
ordenada = sorted(valores)

# Maior e menor valor (índices)
indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

print("Lista ordenada:", ordenada)
print("Lista original:", valores)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
