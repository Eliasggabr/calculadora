from funcoes import *

listaViagens = []

while True:
    print("1 - Registrar nova viagem \n2 - Exibir todas as viagens \n3 - Buscar viagens por motorista \n4 - Exibir viagem mais cara \n5 - Mostrar média geral de consumo \n0 - Sair")
    op = int(input("Digite a operação desejada: "))
    if op == 1:
        registrar_viagens(listaViagens)
    elif op == 2:
        exibir_viagens(listaViagens)
    elif op == 3:
        buscar_motorista(listaViagens)
    elif op == 4:
        viagem_mais_cara(listaViagens)
    elif op == 5:
        media_consumo(listaViagens)
    elif op == 0:
        break
    else: ValueError