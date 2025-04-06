import Base
import Functions

def menu():
    while True:
        print("Bem vindo a livraria do papi")
        print("selecione uma das opções a baixo")
        print()
        print("1 - Cadatrar Livro")
        print("2 - Listar")
        print("Para Buscas, digite um dos codigos a baixo:")
        print()
        print("3 - Buscar por Nome")
        print("4 - Buscar por Categoria")
        print("5 - Buscar por Preço (abaixo do informado)")
        print("6 - Buscar por Estoque")
        # print("7 - Buscar por Total do Estoque em R$")
        print()
        print("0 - Para finalizar o sitema")

        op = input("Digite a opção desejada: ")
        print("-" * 30)
        print()

        if op == "1":
            Base.AddLivros()
        elif op == "2":
            Functions.ListarLivros()
        elif op == "3":
            Functions.BuscaNome()
        elif op == "4":
            Functions.BuscaCat()
        elif op == "5":
            Functions.BuscaPrice()
        elif op == "6":
            Functions.BuscaEstoque()
        # elif op == "7":
        #     Functions.BuscaValue()
        elif op == "0":
           print("saindo")
           break

if __name__ == "__main__":
    menu()