def calcula_digito(cpf_parcial):
    """
    Recebe uma string com os primeiros dígitos do CPF (9 para o primeiro dígito,
    10 para o segundo dígito) e calcula o dígito verificador conforme a regra.
    """
    tamanho = len(cpf_parcial) + 1
    multiplicadores = list(range(tamanho, 1, -1))  # Ex: para 9 dígitos: 10..2

    soma = 0
    for digito, mult in zip(cpf_parcial, multiplicadores):
        soma += int(digito) * mult

    resto = soma % 11
    if resto < 2:
        return '0'
    else:
        return str(11 - resto)

def valida_cpf(cpf):
    # Remove os pontos e o hífen
    cpf_numeros = cpf.replace('.', '').replace('-', '')
    if len(cpf_numeros) != 11 or not cpf_numeros.isdigit():
        return False

    # Primeiros 9 dígitos
    primeiros_nove = cpf_numeros[:9]
    digito1 = calcula_digito(primeiros_nove)
    digito2 = calcula_digito(primeiros_nove + digito1)

    # Compara com os dígitos fornecidos
    return cpf_numeros[-2:] == digito1 + digito2

# Programa principal
cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

if valida_cpf(cpf_usuario):
    print("Válido")
else:
    print("Inválido")
