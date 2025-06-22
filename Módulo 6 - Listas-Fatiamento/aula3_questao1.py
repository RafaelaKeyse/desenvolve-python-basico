#  Fatiamento de lista de números inteiros

# aula3_questao1.py

numeros = []

print("Digite pelo menos 4 números inteiros. Digite 'fim' para parar:")

while True:
    entrada = input()
    if entrada.lower() == 'fim':
        if len(numeros) >= 4:
            break
        else:
            print("Digite pelo menos 4 números.")
    else:
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Digite apenas números inteiros ou 'fim'.")

print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Índices pares:", numeros[::2])
print("Índices ímpares:", numeros[1::2])
