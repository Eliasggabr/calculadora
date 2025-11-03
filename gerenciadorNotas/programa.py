lfrom funcoes import *

listaNotas = []
listaAlunos = {}

while True:
    op = int(input("Digite 1 para adicionar um aluno, 2 para mostrar o relatório, 0 para sair: "))
    if op == 1:
        nome = input("Digite um nome: ")
        for i in range(1,4):
            nota = float(input(f"Digite a {i} nota do aluno: "))
            listaNotas.append(nota)
        media = calcularMedia(listaNotas)
        status = vericacao(media)
        listaAlunos = {nome: [listaNotas, media, status]}
       
    if op == 2:
        print(listaAlunos)
    if op == 0:
        print("Encerrando...")
        break

