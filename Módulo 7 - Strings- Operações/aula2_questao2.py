# aula2_questao2.py

# Entrada do usuário
frase = input("Digite uma frase: ")

# Substituindo vogais (maiúsculas e minúsculas) por '*'
modificada = ''.join(['*' if c.lower() in 'aeiou' else c for c in frase])

# Exibindo resultado
print("Frase modificada:", modificada)
