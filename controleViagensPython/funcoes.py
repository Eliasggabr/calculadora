def registrar_viagens(listaViagens):
    motorista = input("Digite o nome o motorista: ")
    destino = input("Digite o destino da viagem: ")
    distancia = int(input("Digite a distância da partida até o destino(km): "))
    gasto = int(input("Digite o gasto com o combutível(R$): "))
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
    return listaViagens


def buscar_motorista(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    for i in listaViagens:
        if motorista == i["Motorista"]:
            print(i)
    return listaViagens

def viagem_mais_cara(listaViagens):
    maior_gasto = -1
    viagem_cara = None
    for viagem in listaViagens:
        if viagem["Gasto"] > maior_gasto:
            maior_gasto = viagem["Gasto"]
            viagem_cara = viagem
    print(f"A viagem mais cara é: \n{viagem_cara}")
    return listaViagens


def media_consumo(listaViagens):
    consumos_total = None
    consumos_soma = None
    media = consumos_soma / consumos_total
    for viagem in listaViagens:
        consumos_total += 1
        consumos_soma += viagem["Consumo"]
    print(f"A média geral do consumo em R$ é: {media}")
    return listaViagens


