def imprimir(b,h):
    print("+", end="")
    for i in range(b-2):
        print("---", end="")
    print("+")
    for i in range(h-2):
        print("|",end ="")
        for j in range(b-2):
            print("   ",end="")
        print("|")
    print("+",end="")
    for i in range(b-2):
        print("---", end="")
    print("+")


x = int(input("Digite o valor da base: "))
y = int(input("Digite o valor da altura: "))
imprimir(x, y)
