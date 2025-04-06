import Base

def ListarLivros():
    livros = Base.CarregaLivros()

    if not livros:
        print("Não há livros no banco de dados.")
        return
    for livro in livros.values():
        print(livro)
        

def BuscaNome():
    livros = Base.CarregaLivros()
    nome_busca = input("Digite o nome do livro que deseja buscar: ").lower()
    
    encontrados = [livro for livro in livros.values() if nome_busca in livro.titulo.lower()]
    
    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print("Nenhum livro encontrado com esse nome.")

def BuscaCat():
    livros = Base.CarregaLivros()
    catega = input("Digite a cadegoria do livro para buscar: ")

    encontrados = [livro for livro in livros.values() if catega.lower() in livro.area.lower()]

    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else:
        print("Livro nao encontrado nessa categoria")

  
def BuscaPrice():
    livros = Base.CarregaLivros()
    maxp = float(input("Digite o valor maximo: "))
    print("-" * 30)

    encontrados = [livro for livro in livros.values() if livro.valor <= maxp]

    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else: 
        print("Nao achamos livro mais barato que o valor informado")

def BuscaEstoque():
    livros = Base.CarregaLivros()
    estoque_min = int(input("Digite a quantidade mínima em estoque: "))

    encontrados = [livro for livro in livros.values() if livro.estoque >= estoque_min]

    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else:
        print("Nenhum livro encontrado com esse estoque.")

def  BuscaValue():
    livros = Base.CarregaLivros()
    valor_min = float(input("Digite o valor mínimo total de estoque: "))

    # descobri esse formato que me faz perder menos tempo pra por tudo em uma linha de codigo, usando 
    encontrados = [livro for livro in livros.values() if (livro.estoque * livro.valor) >= valor_min]

    if encontrados:
        for livro in encontrados:
            print(livro)
            print("-" * 30)
    else:
        print("Nenhum livro encontrado com esse valor de estoque.")