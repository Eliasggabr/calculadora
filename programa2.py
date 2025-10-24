from operacoes2 import *

while True:
    print("Calculadora")
    print("A seguir serão informados os números de suas respectivas operações:")
    print(f"Soma = {1}")
    print(f"Subtração = {2}")
    print(f"Multiplicação = {3}")
    print(f"Divisão = {4}")
    print(F"Sair = {0}")
    n = int(input("Digite o número da operação: "))
    if n == 1:
        soma()
        sair = int(input("Deseja continuar? 1 para sim; 0 para não: "))
        if sair == 1:
            continue
        elif sair == 0:
            break
    elif n == 2:
        subtracao()
        sair = int(input("Deseja continuar? 1 para sim; 0 para não: "))
        if sair == 1:
            continue
        elif sair == 0:
            break
    elif n == 3:
        multiplicacao()
        sair = int(input("Deseja continuar? 1 para sim; 0 para não: "))
        if sair == 1:
            continue
        elif sair == 0:
            break
    elif n == 4:
        divisao()
        sair = int(input("Deseja continuar? 1 para sim; 0 para não: "))
        if sair == 1:
            continue
        elif sair == 0:
            break
    elif n == 0:
        print("Finalizando...")
        break
