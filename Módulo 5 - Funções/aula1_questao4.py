import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

# Formata os valores com dois dígitos onde necessário
data_formatada = f"{agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_formatada = f"{agora.hour:02d}:{agora.minute:02d}"

# Exibe a data e hora
print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
