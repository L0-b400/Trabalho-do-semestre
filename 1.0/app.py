import Classes
import Functions
from Main import menu


def menuHome():
    while True:
        print("Bem-vindo ao Sistema de Livrarias")
        print("1. Selecionar a Empresa/Filial:")
        print("2. Para Criar uma Empresa/Filial")
        print("3. Pesquisar livros em todas as Empresas/Filiais")
        print("0 - Sair")
        print(Classes.espaco)

        op = input("Digite a opção desejada: ")

        if op == "0":
            print("Encerrando o sistema...")
            break

        elif op == "1":
            filiais = Classes.Empresas.listar_filiais()
            if not filiais:
                continue

            fl = input("Digite o código da filial desejada: ")
            if fl not in filiais:
                print("Filial não encontrada. Tente novamente.")
                continue

            biblioteca = Classes.Biblioteca(fl)
            menu(biblioteca)

        elif op == "2":    
            Classes.Empresas.criar()
        
        elif op == "3":
            Functions.buscaGlobal()
        else:
            print("Opção inválida. Tente novamente.")
            print(Classes.espaco)


if __name__ == "__main__":
    menuHome()
