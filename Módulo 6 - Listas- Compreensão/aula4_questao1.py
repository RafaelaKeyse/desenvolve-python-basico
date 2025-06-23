# Todos os números pares entre 20 e 50

pares = [x for x in range(20, 51) if x % 2 == 0]
print("Pares entre 20 e 50:", pares)

# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in valores]
print("Quadrados de 1 a 9:", quadrados)

# Todos os números entre 1 e 100 que sejam divisíveis por 7
div7 = [x for x in range(1, 101) if x % 7 == 0]
print("Divisíveis por 7 entre 1 e 100:", div7)

# Para valores em range(0,30,3), escrever "par" ou "ímpar"
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print("Paridade dos números de 0 a 30 de 3 em 3:", paridade)
