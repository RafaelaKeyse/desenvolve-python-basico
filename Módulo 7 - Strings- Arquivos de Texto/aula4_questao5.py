# Cria o arquivo CSV com dados sobre livros
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Cabeçalho da planilha
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Dados dos livros
    livros = [
        ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
        ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
        ["Dom Casmurro", "Machado de Assis", 1899, 256],
        ["1984", "George Orwell", 1949, 328],
        ["A Revolução dos Bichos", "George Orwell", 1945, 112],
        ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
        ["Capitães da Areia", "Jorge Amado", 1937, 272],
        ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
        ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1178],
        ["Orgulho e Preconceito", "Jane Austen", 1813, 416]
    ]

    # Escreve os dados no arquivo
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso!")
