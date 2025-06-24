# aula2_questao1.py

# Lista de meses por extenso
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Entrada do usuário
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Separando a data
dia, mes, ano = data.split("/")

# Convertendo mês para nome
mes_extenso = meses[int(mes) - 1]

# Exibindo resultado
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
