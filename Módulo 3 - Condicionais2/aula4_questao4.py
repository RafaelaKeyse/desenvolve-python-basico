# Frete com base na distância e peso

# Solicita a distância e o peso
distancia = float(input("Digite a distância da entrega (km): "))
peso = float(input("Digite o peso do pacote (kg): "))

# Calcula o valor base do frete conforme a distância
if distancia <= 100:
    preco_por_kg = 1.0
elif distancia <= 300:
    preco_por_kg = 1.5
else:
    preco_por_kg = 2.0

# Calcula o valor total do frete
frete = peso * preco_por_kg

# Adiciona taxa extra se peso > 10kg
if peso > 10:
    frete += 10

# Imprime o valor do frete com 2 casas decimais
print(f"Valor do frete: R${frete:.2f}")
