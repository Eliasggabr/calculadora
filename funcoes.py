def registrar_viagens(listaViagens):
    motorista = input("Digite o nome o motorista: ")
    destino = input("Digite o destino da viagem: ")
    distancia = input("Digite a distância da partida até o destino(km): ")
    gasto = input("Digite o gasto com o combutível(R$): ")
    consumo = gasto / distancia
    dictViagem = {
        "Motorista": motorista,
        "Destino": destino,
        "Distância(km)": distancia,
        "Gasto": gasto,
        "Consumo médio": consumo
    }
    listaViagens.append(dictViagem)
    return listaViagens

def exibir_viagens(listaViagens):
    print(listaViagens)

def buscar_motorista(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    for i in listaViagens:
        if motorista == i["Motorista"]:
            print(i)
    return listaViagens
