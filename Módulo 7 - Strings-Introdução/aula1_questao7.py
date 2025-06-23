def encrypt(nomes, chave=5):
    nomes_cript = []

    for nome in nomes:
        cript_nome = ""
        for c in nome:
            codigo = ord(c)
            if 33 <= codigo <= 126:
                novo_codigo = 33 + ((codigo - 33 + chave) % (126 - 33 + 1))
                cript_nome += chr(novo_codigo)
            else:
                cript_nome += c
        nomes_cript.append(cript_nome)

    return nomes_cript

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave_aleatoria = 5
nomes_cript = encrypt(nomes, chave_aleatoria)

print("chave_aleatoria =", chave_aleatoria)
print("nomes_cript =", nomes_cript)
