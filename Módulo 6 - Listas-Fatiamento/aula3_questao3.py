# Remover intervalo com mais negativos

# aula3_questao3.py

import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontrar o maior intervalo com negativos consecutivos
inicio = fim = max_inicio = max_fim = 0
max_negativos = cont = 0

while fim < len(lista):
    if lista[fim] < 0:
        cont += 1
        fim += 1
    else:
        if cont > max_negativos:
            max_negativos = cont
            max_inicio = inicio
            max_fim = fim
        fim += 1
        inicio = fim
        cont = 0

# Checa se terminou com sequência negativa
if cont > max_negativos:
    max_inicio = inicio
    max_fim = fim

# Remove intervalo
del lista[max_inicio:max_fim]

print("Editada:", lista)
