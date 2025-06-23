def encontrar_anagramas(frase, objetivo):
    objetivo_ordenado = sorted(objetivo.lower())
    palavras = frase.split()
    anagramas = []

    for palavra in palavras:
        limpa = ''.join(filter(str.isalpha, palavra))  # remove pontuações
        if sorted(limpa.lower()) == objetivo_ordenado:
            anagramas.append(palavra)

    return anagramas


# Programa principal
frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

resultado = encontrar_anagramas(frase, objetivo)

print("Anagramas:", resultado)
