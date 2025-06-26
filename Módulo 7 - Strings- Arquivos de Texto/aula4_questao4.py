import random
import os

CAMINHO = r"C:\Módulo 7 - Strings- Arquivos de Texto"

def carregar_palavra():
    caminho = os.path.join(CAMINHO, "gabarito_forca.txt")
    with open(caminho, "r", encoding="utf-8") as f:
        palavras = [linha.strip().lower() for linha in f if linha.strip()]
    return random.choice(palavras)

def carregar_enforcado():
    caminho = os.path.join(CAMINHO, "gabarito_enforcado.txt")
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()
    estagios = conteudo.strip().split("=========")
    return [estagio.strip() + "\n=========" for estagio in estagios if estagio.strip()]

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogar():
    palavra = carregar_palavra()
    estagios = carregar_enforcado()
    letras_certas = ["_" for _ in palavra]
    tentativas = 6
    erros = 0
    letras_usadas = set()

    print("Bem-vindo ao Jogo da Forca!")
    print(" ".join(letras_certas))

    while erros < tentativas and "_" in letras_certas:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_certas[i] = letra
        else:
            erros += 1
            imprime_enforcado(erros, estagios)

        print(" ".join(letras_certas))
        print("Letras usadas:", " ".join(sorted(letras_usadas)))

    if "_" not in letras_certas:
        print("Parabéns! Você venceu!")
    else:
        print("Você perdeu. A palavra era:", palavra)

jogar()
