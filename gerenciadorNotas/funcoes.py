
def calcularMedia (listaNotas):
    media = sum(listaNotas) / len(listaNotas)
    return media

def vericacao (media):
    if media >=7:
        return "Aprovado"
    elif 5 < media <= 6.9:
        return "Recuperação"
    elif media < 5:
        return "Reprovado"