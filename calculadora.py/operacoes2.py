def soma ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print (f"{n1} + {n2} = {n1 + n2}") 


def subtracao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print (f"{n1} - {n2} = {n1 - n2}") 


def multiplicacao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print (f"{n1} x {n2} = {n1 * n2}") 


def divisao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        if n1 or n2 == 0:
            print("Esta é uma divsão por zero. O resultado é indeterminado. Por favor, tente outro cálculo.")
        else:
            print (f"{n1} / {n2} = {n1 / n2}")
