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
