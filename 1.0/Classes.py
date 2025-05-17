import os

espaco = "-" * 30

class Livros:
    def __init__(self, titulo, code, edit, area, ano, valor, estoque, ttestoque):
        self.titulo = titulo
        self.code = code
        self.edit = edit
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque
        self.ttestoque = ttestoque

    def __str__(self):
        return (f'>>>>> Cod#: {self.code}\n'
                f'Título: {self.titulo}\n'
                f'Ano: {self.ano}\n'
                f'Editora: {self.edit}\n'
                f'Área: {self.area}\n'
                f'Valor: {self.valor}\n'
                f'Estoque: {self.estoque} Un\n'
                f'Total em Estoque: {self.ttestoque}\n'
                f'{espaco}')

    def to_txt(self):
        return (f'{self.code}\n{self.titulo}\n{self.ano}\n{self.edit}\n{self.area}\n{self.valor}\n{self.estoque}\n{self.ttestoque}\n\n')

    @classmethod
    def from_txt(cls, bloco):
        linhas = bloco.strip().split('\n')
        if len(linhas) < 7:
            return None  # Ignora blocos incompletos
        code = linhas[0]
        titulo = linhas[1]
        ano = linhas[2]
        edit = linhas[3]
        area = linhas[4]
        valor = float(linhas[5])
        estoque = int(linhas[6])
        ttestoque = float(linhas[7])
        return cls(titulo, code, edit, area, ano, valor, estoque, ttestoque)



class Biblioteca:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_file = os.path.join(base_dir, "Livros.txt")

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

    # def salvar(self, livros):
    #     with open(self.db_file, "w", encoding="utf-8") as file:
    #         json.dump({titulo: livro.to_dict() for titulo, livro in livros.items()}, file, indent=4, ensure_ascii=False)

    def salvar(self, livros):
        with open(self.db_file, "w", encoding="utf-8") as file:
            for livro in livros.values():
                file.write(livro.to_txt())

    def adicionar(self):
        titulo = input("Titulo: ")
        code = input("Código: ")
        edit = input("Editora: ")
        area = input("Área: ")
        ano = input("Ano: ")
        valor = float(input("Valor: "))
        estoque = int(input("Quantidade em Estoque: "))
        ttestoque = valor * estoque

        livros = self.carregar()

        if titulo in livros:
            print("Livro já cadastrado!")
        else:
            novo_livro = Livros(titulo, code, edit, area, ano, valor, estoque, ttestoque)
            livros[titulo] = novo_livro
            self.salvar(livros)
            print("Livro cadastrado com sucesso!")
