import os
import Classes

espaco = "-" * 30

class Livros:
    def __init__(self, loc, titulo, code, edit, area, ano, valor, estoque, ttestoque):
        self.loc = loc
        self.titulo = titulo
        self.code = code
        self.edit = edit
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
        self.ttestoque = ttestoque


    def __str__(self):
        return (f'Empresa/Filial: {self.loc}\n'
                f'>>>>> Cod#: {self.code}\n'
                f'Título: {self.titulo}\n'
                f'Ano: {self.ano}\n'
                f'Editora: {self.edit}\n'
                f'Área: {self.area}\n'
                f'Valor: {self.valor}\n'
                f'Estoque: {self.estoque} Un\n'
                f'Total em Estoque: {self.ttestoque}\n'
                f'{espaco}')

    def to_txt(self):
        return (f'{self.loc}\n{self.code}\n{self.titulo}\n{self.ano}\n{self.edit}\n{self.area}\n{self.valor}\n{self.estoque}\n{self.ttestoque}\n\n')

    @classmethod
    def from_txt(cls, bloco):
        linhas = bloco.strip().split('\n')
        if len(linhas) < 9:
            return None  
        loc = linhas[0]
        code = linhas[1]
        titulo = linhas[2]
        ano = linhas[3]
        edit = linhas[4]
        area = linhas[5]
        valor = float(linhas[6])
        estoque = int(linhas[7])
        ttestoque = float(linhas[8])
        return cls(loc, titulo, code, edit, area, ano, valor, estoque, ttestoque)


# criei um algo que gera 1 doc pra cada filial
# mas preciso conseguir ler eles nas buscas kkkk
class Biblioteca:
    def __init__(self, filialCode):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_file = os.path.join(base_dir, f"Livros_{filialCode}.txt")
   
    # utilizar json
    # def carregar(self):
    #     if not os.path.exists(self.db_file):
    #         return {}
    #     with open(self.db_file, "r", encoding="utf-8") as file:
    #         data = json.load(file)
    #     return {titulo: Livros.from_dict(info) for titulo, info in data.items()}

    def carregar(self):
        livros = {}
        if not os.path.exists(self.db_file):
            return livros
        with open(self.db_file, "r", encoding="utf-8") as file:
            data = file.read()
            block = data.strip().split('\n\n')
            for block in block:
                livro = Livros.from_txt(block)
                if livro:
                    livros[livro.titulo] = livro
        return livros
    
    # utilizar json
    # def salvar(self, livros):
    #     with open(self.db_file, "w", encoding="utf-8") as file:
    #         json.dump({titulo: livro.to_dict() for titulo, livro in livros.items()}, file, indent=4, ensure_ascii=False)

    def salvar(self, livros):
        with open(self.db_file, "w", encoding="utf-8") as file:
            for livro in livros.values():
                file.write(livro.to_txt())

    def adicionar(self):
        while True:
            filiais = Classes.Empresas.listar_filiais()
            if not filiais:
                return

            loc = input("Digite o código da filial desejada: ")
            if loc not in filiais:
                print("Filial não encontrada. Tente novamente.")
            else:
                break

        titulo = input("Titulo: ")
        code = input("Código: ")
        edit = input("Editora: ")
        area = input("Área: ")
        ano = input("Ano: ")
        valor = float(input("Valor: "))
        estoque = int(input("Quantidade em Estoque: "))
        ttestoque = valor * estoque

        livros = self.carregar()

        # Verifica se já existe um livro com o mesmo título e na mesma filial
        livro_existente = livros.get(titulo)
        if livro_existente and livro_existente.loc == loc:
            print("Livro já cadastrado para essa filial!")
            add = input('Digite "s" ou "n": ')
            if add == "s":
                print("função a implementar kkkkk")
        else:
            novo_livro = Livros(loc, titulo, code, edit, area, ano, valor, estoque, ttestoque)
            livros[titulo] = novo_livro
            self.salvar(livros)
            print("Livro cadastrado com sucesso!")


class Empresas:
    def __init__(self, code, name, adress, phone, books):
        self.code = code
        self.name = name
        self.adress = adress
        self.phone = phone
        self.books = books

    def to_txt(self):
        return f"{self.code}|{self.name}|{self.adress}|{self.phone}\n"
    
    @staticmethod
    def criar():
        print("Cadastro de nova Filial")
        code = input("Código da Filial: ")
        name = input("Nome da Filial: ")
        adress = input("Endereço: ")
        phone = input("Telefone: ")
        
        # Salvar em txt
        with open("filiais.txt", "a", encoding="utf-8") as f:
            f.write(f"{code}|{name}|{adress}|{phone}\n")
        
        print("Filial cadastrada com sucesso!")

    @staticmethod
    def listar_filiais():
        if not os.path.exists("filiais.txt"):
            print("Nenhuma filial cadastrada ainda.")
            return []
        
        with open("filiais.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        
        filiais = []
        print("\n--- Filiais Cadastradas ---")
        for linha in linhas:
            partes = linha.strip().split("|")
            if len(partes) == 4:
                code, name, adress, phone = partes
                print(f"Código: {code} | Nome: {name} | Endereço: {adress} | Telefone: {phone}")
                filiais.append(code)
        print(espaco)
        return filiais



# tentei usar o chat pra resolver o problema de o filiais.txt #ficar fora e so piorou
# mas eu confesso que foi preguiça minha de rever as functions.

# class Empresas:
#     def __init__(self, code, name, adress, phone, books):
#         self.code = code
#         self.name = name
#         self.adress = adress
#         self.phone = phone
#         self.books = books

#     def to_txt(self):
#         return f"{self.code}|{self.name}|{self.adress}|{self.phone}\n"

#     @staticmethod
#     def get_filiais_path():
#         # Caminho absoluto para o arquivo filiais.txt no mesmo diretório deste script
#         return os.path.join(os.path.dirname(__file__), "filiais.txt")

#     @staticmethod
#     def criar():
#         print("Cadastro de nova Filial")
#         code = input("Código da Filial: ")
#         name = input("Nome da Filial: ")
#         adress = input("Endereço: ")
#         phone = input("Telefone: ")

#         path = Empresas.get_filiais_path()
#         with open(path, "a", encoding="utf-8") as f:
#             f.write(f"{code}|{name}|{adress}|{phone}\n")

#         print("Filial cadastrada com sucesso!")

#     @staticmethod
#     def listar_filiais():
#         path = Empresas.get_filiais_path()
#         if not os.path.exists(path):
#             print("Nenhuma filial cadastrada ainda.")
#             return []

#         with open(path, "r", encoding="utf-8") as f:
#             linhas = f.readlines()

#         filiais = []
#         print("\n--- Filiais Cadastradas ---")
#         for linha in linhas:
#             partes = linha.strip().split("|")
#             if len(partes) == 4:
#                 code, name, adress, phone = partes
#                 print(f"Código: {code} | Nome: {name} | Endereço: {adress} | Telefone: {phone}")
#                 filiais.append(code)
#         print(espaco)
#         return filiais
