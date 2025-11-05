from funcoes import *

listaLivros = []

while True:
    print(f"Adicionar livro = {1}")
    print(f"Exibir todos os livros = {2}")
    print(f"Emprestar livro = {3}")
    print(f"Devolver livro = {4}")
    print(F"Sair = {0}")
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        adicionar_livro(listaLivros)
    elif op == 2:
        exibir_livros(listaLivros)
    elif op == 3:
        emprestar_livro(listaLivros)
    elif op == 4:
        devolver_livro(listaLivros)
    elif op == 0:
        print("Finalizando...")
        break
    else:
        print("Essa opção não existe. Por favor, use as que foram mostradas no começo.")
        
