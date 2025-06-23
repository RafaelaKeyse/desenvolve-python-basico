frase = input("Digite uma frase: ")

vogais = sorted([letra for letra in frase if letra.lower() in 'aeiou'])
consoantes = [letra for letra in frase if letra.lower() not in 'aeiou' and letra != ' ']

print("Vogais:", vogais)
print("Consoantes:", consoantes)
