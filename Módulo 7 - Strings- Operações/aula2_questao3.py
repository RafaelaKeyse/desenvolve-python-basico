import string
import unicodedata

def limpar_texto(texto):
    # Remove acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # Converte para minúsculas e remove espaços e pontuação
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto = ''.join(c for c in texto if c not in string.punctuation)
    return texto

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    
    texto_limpo = limpar_texto(frase)
    
    if texto_limpo == texto_limpo[::-1]:
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')
