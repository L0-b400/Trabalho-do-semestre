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
        return (f'Título: {self.titulo}\n'
                f'Ano: {self.ano}\n'
                f'Editora: {self.editora}\n'
                f'Área: {self.area}\n'
                f'Valor: {self.valor}\n'
                f'Estoque: {self.estoque} Un')

        