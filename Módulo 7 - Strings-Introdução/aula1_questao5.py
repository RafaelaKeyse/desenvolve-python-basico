frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
indices_vogais = [i + 1 for i, letra in enumerate(frase) if letra in vogais]

print(f"{len(indices_vogais)} vogais")
print(f"Índices {indices_vogais}")

