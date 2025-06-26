import re

# Lê o conteúdo de frase.txt
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Remove caracteres não alfabéticos, exceto espaços, e divide em palavras
palavras = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', conteudo)

# Escreve as palavras em palavras.txt, uma por linha
with open("palavras.txt", "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Mostra o conteúdo do arquivo palavras.txt
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
