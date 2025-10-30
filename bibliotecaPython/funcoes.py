

def adicionar_livro(listaLivros):
    titulo = input("Por favor, digite o título do livro: ")
    autor = input("Por favor, digite o autor do livro: ")
    status = "Disponível"
    dicionario = {"Título": titulo, "Autor": autor, "Status": status}
    listaLivros.append(dicionario)

def emprestar_livro(listaLivros):
    status = "Emprestado"

def devolver_livro(listaLivros):
    status = "Disponível"

def exibir_livros(listaLivros):
    print(listaLivros)
