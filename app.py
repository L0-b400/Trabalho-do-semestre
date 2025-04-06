# from flask import Flask, render_template, request
# from Function import addLivro, buscaLivro, listLivro
# from Obj import books, liv_all
# from Classes import Livros

# app = Flask(__name__)

# # Rota para exibir o formulário de cadastro de livros
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Rota para processar o envio do formulário
# @app.route('/cadastro', methods=['POST'])
# def cadastro():
#     # Pegando os dados do formulário
#     titulo = request.form['titulo']
#     codigo = request.form['codigo']
#     editora = request.form['editora']
#     area = request.form['area']
#     ano = request.form['ano']
#     valor = request.form['valor']
#     estoque = request.form['estoque']
    
#     # Criando o novo livro
#     novo_livro = Livros(titulo, codigo, editora, area, ano, valor, estoque)
    
#     # Adicionando o livro ao dicionário
#     addLivro(books, novo_livro)
    
#     return render_template('index.html', message="Livro cadastrado com sucesso!")

# # Rota para buscar um livro pelo código
# @app.route('/busca', methods=['POST'])
# def busca():
#     codigo_busca = request.form['codigo_busca']
#     livro = buscaLivro(books, codigo_busca)
#     return render_template('index.html', livro=livro)

# if __name__ == "__main__":
#     app.run(debug=True)
