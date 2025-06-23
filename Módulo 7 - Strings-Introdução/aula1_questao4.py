numero = input("Digite o número: ")

# Se o número tiver 8 dígitos, adiciona o 9 no início
if len(numero) == 8:
    numero = '9' + numero
elif len(numero) == 9 and numero[0] != '9':
    print("Número inválido: números de 9 dígitos devem começar com 9.")

# Formata com o hífen entre o 5º e 6º dígito
if len(numero) == 9:
    numero_formatado = numero[:5] + '-' + numero[5:]
    print(f"Número completo: {numero_formatado}")
else:
    print("Número inválido.")
