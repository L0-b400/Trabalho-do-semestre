import json
import os
import Classes

# json: Permite trabalhar com arquivos JSON, que armazenam dados estruturados (como dicionários em Python).

# os: Fornece funções para manipular caminhos de arquivos e diretórios, garantindo compatibilidade entre diferentes sistemas operacionais.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "Livros.json")

# os.path.abspath(__file__): Obtém o caminho absoluto do script que está sendo executado.

# os.path.dirname(...): Extrai apenas o diretório onde o script está salvo.

# os.path.join(BASE_DIR, "Livros.json"): Cria o caminho completo do arquivo Livros.json dentro da mesma pasta do script.

def CarregaLivros():
    """Carrega os dados do arquivo JSON"""
    if not os.path.exists(DB_FILE):
        return {}  # Se o arquivo não existir, retorna um dicionário vazio.

    with open(DB_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Converte os dicionários carregados para objetos Livros
    return {titulo: Classes.Livros.from_dict(info) for titulo, info in data.items()}

# Se o arquivo Livros.json não existir, a função retorna um dicionário vazio {}.

# Se o arquivo existir, ele é aberto e lido, convertendo os dados JSON para um dicionário Python usando json.load(file).

# O parâmetro encoding="utf-8" garante que caracteres especiais sejam interpretados corretamente.

def SaveLivros(Livros):
    """Salva os livros no JSON"""
    with open(DB_FILE, "w", encoding="utf-8") as file:
        # Converte os objetos Livros para dicionário antes de salvar
        json.dump({titulo: livro.to_dict() for titulo, livro in Livros.items()}, file, indent=4, ensure_ascii=False)

def AddLivros():
    """Adiciona um novo livro ao JSON"""
    titulo = input("Titulo: ")
    code = input("Código: ")
    edit = input("Editora: ")
    # presumi que area seria a categoria
    area = input("Área: ")
    ano = input("Ano: ")
    valor = float(input("Valor: "))
    estoque = int(input("Quantidade em Estoque: "))

    livros = CarregaLivros()
    
    if titulo in livros:
        print("Livro já cadastrado!")
    else:
        novo_livro = Classes.Livros(titulo, code, edit, area, ano, valor, estoque)
        livros[titulo] = novo_livro
        SaveLivros(livros)
        print("Livro cadastrado com sucesso!")

# O método AddLivros agora exige os parâmetros completos necessários para criar um objeto Livros.
# Ele primeiro carrega os livros já existentes, verifica se o título não está cadastrado, e adiciona um novo livro se necessário.
# Em seguida, ele salva os dados atualizados no JSON.
