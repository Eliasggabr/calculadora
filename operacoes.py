
operacao = input("Digite a operação: ")

if operacao == "soma":
    
    def soma ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print (f"{n1} + {n2} = {n1 + n2}") 
    soma()

if operacao == "subtração":

    def subtracao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print (f"{n1} - {n2} = {n1 - n2}") 
    subtracao()

if operacao == "multiplicação":

    def multiplicacao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print (f"{n1} x {n2} = {n1 * n2}") 
    multiplicacao()

if operacao == "divisão":

    def divisao ():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        if n1 or n2 == 0:
            print("Essa é uma divião por zero. O resultado é indeterminado. Por favor, tente outra operação.")
        else:
            print (f"{n1} / {n2} = {n1 / n2}")
    divisao()
