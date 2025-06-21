# Leitura das três notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Cálculo da média
m = (n1 + n2 + n3) / 3

# Condições de avaliação
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

# Finalização
print("Fim")
