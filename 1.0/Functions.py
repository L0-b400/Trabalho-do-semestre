def ListarLivros(bib):
    livros = bib.carregar()
    if not livros:
        print("Não há livros no banco de dados.")
        return
    for livro in livros.values():
        print(livro)

def BuscaNome(bib):
    livros = bib.carregar()
    nome_busca = input("Digite o nome do livro que deseja buscar: ").lower()
    encontrados = [livro for livro in livros.values() if nome_busca in livro.titulo.lower()]
    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado com esse nome.")

def BuscaCat(bib):
    livros = bib.carregar()
    catega = input("Digite a categoria do livro para buscar: ")
    encontrados = [livro for livro in livros.values() if catega.lower() in livro.area.lower()]
    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else:
        print("Livro não encontrado nessa categoria")

def BuscaPrice(bib):
    livros = bib.carregar()
    maxp = float(input("Digite o valor máximo: "))
    encontrados = [livro for livro in livros.values() if livro.valor <= maxp]
    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else:
        print("Não achamos livro mais barato que o valor informado")

def BuscaEstoque(bib):
    livros = bib.carregar()
    estoque_min = int(input("Digite a quantidade mínima em estoque: "))
    encontrados = [livro for livro in livros.values() if livro.estoque >= estoque_min]
    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else:
        print("Nenhum livro encontrado com esse estoque.")

def BuscaValue(bib):
    livros = bib.carregar()
    valor_min = float(input("Digite o valor mínimo total de estoque: "))
    encontrados = [livro for livro in livros.values() if (livro.estoque * livro.valor) >= valor_min]
    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else:
        print("Nenhum livro encontrado com esse valor de estoque.")
