import Classes
import Functions

def menu(bib):
    while True:
        print(f"Bem vindo à livraria")
        print("Selecione uma das opções abaixo")
        print()
        print("1 - Cadastrar Livro")
        print("2 - Listar")
        print("Para Buscas, digite um dos códigos abaixo:")
        print("3 - Buscar por Nome")
        print("4 - Buscar por Categoria")
        print("5 - Buscar por Preço (abaixo do informado)")
        print("6 - Buscar por Estoque")
        print("7 - Buscar por Total do Estoque em R$")
        print("0 - Para finalizar o sistema")
        print()

        op = input("Digite a opção desejada: ")
        print("-" * 30)
        print()

        if op == "1":
            bib.adicionar()
        elif op == "2":
            Functions.ListarLivros(bib)
        elif op == "3":
            Functions.BuscaNome(bib)
        elif op == "4":
            Functions.BuscaCat(bib)
        elif op == "5":
            Functions.BuscaPrice(bib)
        elif op == "6":
            Functions.BuscaEstoque(bib)
        elif op == "7":
            Functions.BuscaValue(bib)
        elif op == "0":
            print("Saindo")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    empresa = input("Digite o codigo da filial: ")
    biblioteca = Classes.Biblioteca()
    menu(biblioteca)
