import os

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Nome do arquivo
nome_arquivo = "frase.txt"

# Abre o arquivo no modo escrita e salva a frase
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Pega o caminho absoluto do arquivo
caminho_completo = os.path.abspath(nome_arquivo)

# Mostra o caminho completo
print(f"Frase salva em {caminho_completo}")
