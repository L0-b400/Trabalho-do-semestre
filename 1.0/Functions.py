import Classes
import Obj

def CadLivros():
    code = input("Codigo do livro: ")
    if code in Obj.books:
        print("Livro já cadastrado")
        return
    titulo = input("Titulo: ")
    editora = input("editora: ")
    area = input("area: ")
    ano = int(input("ano: "))
    valor = float(input("valor R$: "))
    estoque = int(input("estoque: "))

    NovoLivro = Classes.Livros(titulo, code, editora, area, ano, valor, estoque)
    Obj.books[code] = NovoLivro

    print("Feito!")  

def Listar():
    if not Obj.books:
        print("Não existem livros cadastrados")
        return
    for code, livro in Obj.books.items():
        print("Code")   

def BuscaNome():
    nome = input("Digite o nome do livro: ").lower()
    
    encontrados = [Obj.books for Classes.titulo in Obj.books.values() if nome in Classes.titulo.lower()]

    if not encontrados:
        print("Nenhum livro encontrado")
        return
    
    # print("Livros:")
    # for Obj.books in encontrados:
    #     print(titulo)


def BuscaCat():
    categoria = input("Digite a categoria: ").lower()

    encontrados = [Classes.titulo for Classes.titulo in Obj.books.values() if categoria in Classes.titulo.area.lower()]
    
# def BuscaPrice():
    
# def BuscaEstoque():

# def BuscaValue():


# # Função para buscar livros por categoria (área)
# def buscar_por_categoria():
#     """Filtra livros pela área (categoria)."""
#     categoria = input("Digite a categoria: ").lower()

#     encontrados = [livro for livro in livros.values() if categoria in livro.area.lower()]

#     if not encontrados:
#         print("⚠ Nenhum livro encontrado nessa categoria.")
#         return

#     print("\n📚 LIVROS DA CATEGORIA:")
#     for livro in encontrados:
#         print(livro)

# # Função para buscar livros abaixo de um preço definido pelo usuário
# def buscar_por_preco():
#     """Exibe livros com preço menor que um valor informado."""
#     preco_max = float(input("Digite o valor máximo (R$): "))

#     encontrados = [livro for livro in livros.values() if livro.valor < preco_max]

#     if not encontrados:
#         print("⚠ Nenhum livro encontrado abaixo desse preço.")
#         return

#     print("\n📚 LIVROS ABAIXO DO PREÇO:")
#     for livro in encontrados:
#         print(livro)

# # Função para buscar livros com estoque acima de um valor definido
# def buscar_por_estoque():
#     """Exibe livros que possuem quantidade em estoque maior que o indicado pelo usuário."""
#     estoque_min = int(input("Digite o estoque mínimo: "))

#     encontrados = [livro for livro in livros.values() if livro.estoque > estoque_min]

#     if not encontrados:
#         print("⚠ Nenhum livro encontrado com estoque maior que esse valor.")
#         return

#     print("\n📚 LIVROS COM ESTOQUE MAIOR QUE", estoque_min)
#     for livro in encontrados:
#         print(livro)

# # Função para calcular o valor total do estoque
# def calcular_valor_total():
#     """Calcula e exibe o valor total de todos os livros em estoque."""
#     total = sum(livro.valor * livro.estoque for livro in livros.values())

#     print(f"\n💰 Valor total em estoque: R$ {total:.2f}")