def ListarLivros(bib):
    livros = bib.carregar()
    if not livros:
        print("Não há livros no banco de dados.")
        return
    print("\nLivros cadastrados:\n")
    for livro in livros.values():
        print(livro)

def BuscaNome(bib):
    livros = bib.carregar()
    nome_busca = input("Digite o nome do livro que deseja buscar: ").lower()
    encontrados = [livro for livro in livros.values() if nome_busca in livro.titulo.lower()]
    if encontrados:
        print(f"\n{len(encontrados)} livro(s) encontrado(s) com o nome '{nome_busca}':\n")
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado com esse nome.")

def BuscaCat(bib):
    livros = bib.carregar()
    categoria = input("Digite a categoria do livro para buscar: ").lower()
    encontrados = [livro for livro in livros.values() if categoria in livro.area.lower()]
    if encontrados:
        print(f"\n{len(encontrados)} livro(s) encontrado(s) na categoria '{categoria}':\n")
        for livro in encontrados:
            print(livro)
    else:
        print("Livro não encontrado nessa categoria.")

def BuscaPrice(bib):
    livros = bib.carregar()
    try:
        maxp = float(input("Digite o valor máximo: "))
    except ValueError:
        print("Valor inválido.")
        return
    encontrados = [livro for livro in livros.values() if livro.valor <= maxp]
    if encontrados:
        print(f"\n{len(encontrados)} livro(s) com valor até R${maxp:.2f}:\n")
        for livro in encontrados:
            print(livro)
    else:
        print("Não achamos livro mais barato que o valor informado.")

def BuscaEstoque(bib):
    livros = bib.carregar()
    try:
        estoque_min = int(input("Digite a quantidade mínima em estoque: "))
    except ValueError:
        print("Quantidade inválida.")
        return
    encontrados = [livro for livro in livros.values() if livro.estoque >= estoque_min]
    if encontrados:
        print(f"\n{len(encontrados)} livro(s) com estoque mínimo de {estoque_min} unidades:\n")
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado com esse estoque.")

def BuscaValue(bib):
    livros = bib.carregar()
    try:
        valor_min = float(input("Digite o valor mínimo total de estoque: "))
    except ValueError:
        print("Valor inválido.")
        return
    encontrados = [livro for livro in livros.values() if (livro.estoque * livro.valor) >= valor_min]
    if encontrados:
        print(f"\n{len(encontrados)} livro(s) com valor total de estoque a partir de R${valor_min:.2f}:\n")
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado com esse valor de estoque.")
