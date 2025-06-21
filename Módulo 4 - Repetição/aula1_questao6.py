# Lê o número de experimentos
n = int(input())

# Inicializa contadores
total = 0
coelhos = 0
ratos = 0
sapos = 0

# Lê os dados dos experimentos
for _ in range(n):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]

    total += quantia
    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

# Calcula os percentuais
perc_coelhos = (coelhos / total) * 100
perc_ratos = (ratos / total) * 100
perc_sapos = (sapos / total) * 100

# Imprime o resultado
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
print(f"Percentual de ratos: {perc_ratos:.2f} %")
print(f"Percentual de sapos: {perc_sapos:.2f} %")
