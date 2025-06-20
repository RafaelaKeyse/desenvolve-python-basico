# Ler o comprimento do terreno
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Ler a largura do terreno
largura = int(input("Digite a largura do terreno (em metros): "))

# Ler o preço do metro quadrado
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))

# Calcular área do terreno
area_m2 = comprimento * largura

# Calcular o preço total
preco_total = area_m2 * preco_m2

# Imprimir o resultado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")