# Lê a quantidade de números
n = int(input("Quantos números você vai digitar? "))

# Inicializa a variável 'maior'
maior = 0

# Enquanto ainda houver números a serem lidos
while n > 0:
    x = int(input("Digite um número: "))
    
    # Atualiza o maior se o número for maior que o atual
    if x > maior:
        maior = x
    
    n = n - 1

# Imprime o maior número encontrado
print("Maior número:", maior)
