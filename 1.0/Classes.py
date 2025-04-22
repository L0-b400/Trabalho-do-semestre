espaco = "-" * 30

class Livros:
    def __init__(self, titulo, code, edit, area, ano, valor, estoque):
        self.titulo = titulo
        self.code = code
        self.edit = edit
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def __str__(self):
        return (f'>>>>> Cod#: {self.code}\n'
                f'Título: {self.titulo}\n'
                f'Ano: {self.ano}\n'
                f'Editora: {self.edit}\n'
                f'Área: {self.area}\n'
                f'Valor: {self.valor}\n'
                f'Estoque: {self.estoque} Un\n'
                f'{espaco}')

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "code": self.code,
            "edit": self.edit,
            "area": self.area,
            "ano": self.ano,
            "valor": self.valor,
            "estoque": self.estoque
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            titulo=data["titulo"],
            code=data["code"],
            edit=data["edit"],
            area=data["area"],
            ano=data["ano"],
            valor=data["valor"],
            estoque=data["estoque"]
        )

import os
import json

class Biblioteca:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_file = os.path.join(base_dir, "Livros.json")

    def carregar(self):
        if not os.path.exists(self.db_file):
            return {}
        with open(self.db_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return {titulo: Livros.from_dict(info) for titulo, info in data.items()}

    def salvar(self, livros):
        with open(self.db_file, "w", encoding="utf-8") as file:
            json.dump({titulo: livro.to_dict() for titulo, livro in livros.items()}, file, indent=4, ensure_ascii=False)

    def adicionar(self):
        titulo = input("Titulo: ")
        code = input("Código: ")
        edit = input("Editora: ")
        area = input("Área: ")
        ano = input("Ano: ")
        valor = float(input("Valor: "))
        estoque = int(input("Quantidade em Estoque: "))

        livros = self.carregar()

        if titulo in livros:
            print("Livro já cadastrado!")
        else:
            novo_livro = Livros(titulo, code, edit, area, ano, valor, estoque)
            livros[titulo] = novo_livro
            self.salvar(livros)
            print("Livro cadastrado com sucesso!")
