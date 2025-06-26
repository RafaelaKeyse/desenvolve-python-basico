# aula4_questao3.py

arquivo = "estomago.txt"

with open(arquivo, "r", encoding="latin1") as f:
    linhas = f.readlines()

# Primeiras 25 linhas
print("Primeiras 25 linhas:")
print("".join(linhas[:25]))

# Número total de linhas
print("\nNúmero de linhas:", len(linhas))

# Linha com mais caracteres
linha_maior = max(linhas, key=len)
print("\nLinha com mais caracteres:")
print(linha_maior)

# Contagem dos nomes "Nonato" e "Íria" (ignorando maiúsculas/minúsculas)
texto = "".join(linhas).lower()

# Contagem de ocorrências exatas como palavra
import re
nonato_count = len(re.findall(r"\bnonato\b", texto))
iria_count = len(re.findall(r"\bíria\b", texto))

print(f"\nMenções a 'Nonato': {nonato_count}")
print(f"Menções a 'Íria': {iria_count}")
