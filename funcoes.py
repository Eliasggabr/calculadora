def carregar_cardapio(Cardapio):
    dictCardapio = {"id": 1, "nome": "Café", "preço": 13},
    {"id": 2, "nome": "Salgado", "preço": 14},
    {"id": 3, "nome": "Refrigerante", "preço": 5}
    Cardapio.append(dictCardapio)
    return Cardapio

def exibir_cardapio(Cardapio):
    print(Cardapio)
    return Cardapio

def adicionar_pedido(Cardapio, Pedido):
    id = input("Digite o ID do item: ")
    qtd = int(input("Qual a quantidade? "))
    for i in Cardapio:
        if id == i["id"]:
            total = i["preço"] * qtd
            dictPedido = {
                "nome": i["nome"],
                "qtd": qtd,
                "total": total
            }
    Pedido.append(dictPedido)
    return Cardapio, Pedido

def exibir_pedido(Pedido):
    print(Pedido)
    return Pedido

def remover_item(Pedido):
    id = int(input("Digite o ID do item: "))
    for i in Pedido:
        i
