# Ler temperatura em Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converter para Celsius
celsius = int((fahrenheit - 32) * (5 / 9))

# Imprimir resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")