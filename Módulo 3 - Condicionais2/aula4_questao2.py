# Classificação de filmes

# Solicita a avaliação do usuário (entre 1 e 5)
nota = int(input("Digite a avaliação do filme (1 a 5): "))

# Verifica a avaliação e imprime a mensagem correspondente
if nota == 5:
    print("Excelente!")
elif nota == 4:
    print("Muito Bom!")
elif nota == 3:
    print("Bom!")
elif nota == 2:
    print("Regular.")
elif nota == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, digite um número de 1 a 5.")
