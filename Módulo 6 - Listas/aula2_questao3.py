# Interseção de duas listas sem duplicatas e contagem
import random

# Gera duas listas com 20 números entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Interseção sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Contagem dos elementos da interseção
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)
print("Contagem:")
for valor in interseccao:
    print(f"{valor}: (lista1={lista1.count(valor)}, lista2={lista2.count(valor)})")
