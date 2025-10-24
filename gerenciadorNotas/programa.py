listaNotas = []
listaAlunos = []

while True:
    op = int(input("Digite a operação, 1 para adicionar um aluno, 2 para exibir relatório, 0 para sair: "))
    if op == 1:
        nome = input("Digite um nome: ")
        for i in range(1,4):
            nota = float(input(f"Digite a {i} nota do aluno: "))
            listaNotas.append(nota)
            media = calcularMedia(listaNotas)
            status = verificacao(media)
            dictAluno = { nome: [listaNotas, media, status]}
            
