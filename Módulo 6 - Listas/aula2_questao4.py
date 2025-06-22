# Intercalar duas listas dadas pelo usuário
# Entrada da lista 1
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
print("Digite os", n1, "elementos da lista 1:")
lista1 = [int(input()) for _ in range(n1)]

# Entrada da lista 2
n2 = int(input("Digite a quantidade de elementos da lista 2: "))
print("Digite os", n2, "elementos da lista 2:")
lista2 = [int(input()) for _ in range(n2)]

# Intercalação
intercalada = []
for i in range(max(n1, n2)):
    if i < n1:
        intercalada.append(lista1[i])
    if i < n2:
        intercalada.append(lista2[i])

print("Lista intercalada:", *intercalada)
