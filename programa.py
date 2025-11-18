from funcoes import *

Cardapio = []
Pedido = []

carregar_cardapio(Cardapio)

while True:
    print("1 - Ver cardápio \n2 - Adicionar item ao pedido \n3 - Ver pedido \n4 - Remover item \n0 - Finalizar")
    op = int(input("Digite o número da operação desejada: "))
    if op == 1:
        exibir_cardapio(Cardapio)
    elif op == 2:
        adicionar_pedido(Cardapio, Pedido)
    elif op == 3:
        exibir_pedido(Pedido)
    elif op == 4:
        remover_item(Pedido)
    elif op == 0:
        print("Finalizando...")
        break
