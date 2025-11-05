

def adicionar_livro(listaLivros):
    titulo = input("Por favor, digite o título do livro: ")
    autor = input("Por favor, digite o autor do livro: ")
    disponível = "Disponível"
    status = disponível
    livro = [titulo, autor, status]
    listaLivros.append(livro)
    print("Sucesso! Você adicionou o livro!")
    return listaLivros

def emprestar_livro(listaLivros):
    titulo = input("Por favor, digite o título do livro: ")
    for livro in listaLivros:
        if livro[0] == titulo:
            livro[2] == "Emprestado"
            print("Sucesso! Você pegou o livro emprestado!")
            break
    return listaLivros

def devolver_livro(listaLivros):
    titulo = input("Por favor, digite o título do livro: ")
    for livro in listaLivros:
        if livro[0] == titulo:
            livro[2] == "Disponível"
            print("Sucesso! Você devolveu o livro!")
            break
    return listaLivros

def exibir_livros(listaLivros):
    print(listaLivros)
