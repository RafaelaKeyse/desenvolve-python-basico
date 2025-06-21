# Lê a quantidade de respondentes
n = int(input("Quantos respondentes? "))

# Inicializa a soma das idades
soma_idades = 0

# Lê as idades e soma
for i in range(n):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    soma_idades += idade

# Calcula a média
media = soma_idades / n

# Imprime a média formatada
print(f"Média das idades: {media:.2f}")
