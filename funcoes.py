
def carregar_cardapio(Cardapio):
    
    dictCardapio = [
        {"id": 1, "nome": "Café", "preço": 13},
        {"id": 2, "nome": "Salgado", "preço": 14},
        {"id": 3, "nome": "Refrigerante", "preço": 5}
    ]
    
    Cardapio.extend(dictCardapio)
    return Cardapio


def exibir_cardapio(Cardapio):
    print(Cardapio)
    return Cardapio


def adicionar_pedido(Cardapio, Pedido):
    id_item = int(input("Digite o ID do item: "))
    qtd = int(input("Qual a quantidade? "))

    dictPedido = None

    for item in Cardapio:
        if item["id"] == id_item:
            total = item["preço"] * qtd
            dictPedido = {
                "nome": item["nome"],
                "quantidade": qtd,
                "total": total
            }
            Pedido.append(dictPedido)
            break

    return Cardapio, Pedido


def exibir_pedido(Pedido):
    print(Pedido)
    return Pedido


def remover_item(Pedido):
    nome = input("Digite o nome do item: ")

    for i in Pedido:
        if nome == i["nome"]:
            Pedido.remove(i)
            break

    return Pedido
