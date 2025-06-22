# Solicita os dois números decimais ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a diferença absoluta entre os números
diferenca = abs(numero1 - numero2)

# Arredonda o resultado para duas casas decimais
diferenca_arredondada = round(diferenca, 2)

# Exibe o resultado
print(f"A diferença absoluta entre os números é: {diferenca_arredondada}")
