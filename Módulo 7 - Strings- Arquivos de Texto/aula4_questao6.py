import random

def eh_valida(linha):
    """
    Retorna True se a linha não tiver campos entre aspas (que indicam múltiplos artistas
    ou músicas com vírgulas no nome) - ou seja, se não tiver aspas na linha.
    """
    return '"' not in linha

import os

def eh_valida(linha):
    """Retorna True se a linha NÃO contiver aspas (")"""
    return '"' not in linha

def processar_arquivo(nome_arquivo):
    mais_tocadas_por_ano = {}

    with open(nome_arquivo, encoding='latin-1') as arquivo:
        linhas = arquivo.readlines()

    if not linhas:
        print("Arquivo vazio!")
        return []

    cabecalho = linhas[0].strip().split(',')

    # Pega índices das colunas importantes
    idx_track_name = cabecalho.index('track_name')
    idx_artist_name = cabecalho.index('artist(s)_name')
    idx_released_year = cabecalho.index('released_year')
    idx_streams = cabecalho.index('streams')

    for linha in linhas[1:]:
        linha = linha.strip()
        if not eh_valida(linha):
            # Ignora linhas com aspas
            continue
        
        campos = linha.split(',')

        try:
            track_name = campos[idx_track_name]
            artist_name = campos[idx_artist_name]
            released_year = int(campos[idx_released_year])
            streams = int(campos[idx_streams])
        except (IndexError, ValueError):
            continue

        if 2012 <= released_year <= 2022:
            if (released_year not in mais_tocadas_por_ano) or (streams > mais_tocadas_por_ano[released_year][3]):
                mais_tocadas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

    # Monta lista ordenada por ano
    resultado = [mais_tocadas_por_ano[ano] for ano in range(2012, 2023) if ano in mais_tocadas_por_ano]
    return resultado

# Defina o caminho correto para o arquivo CSV aqui:
arquivo = os.path.join(os.getcwd(), "spotify-2023.csv")

if not os.path.isfile(arquivo):
    print(f"Arquivo não encontrado: {arquivo}")
else:
    musicas_mais_tocadas = processar_arquivo(arquivo)
    print(musicas_mais_tocadas)


