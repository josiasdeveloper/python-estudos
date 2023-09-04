from random import randint


def dados():
    a = randint(1, 6)
    b = randint(1, 6)
    return a + b


def craps():
    x = input("Aperte enter para lançar os dados: ")
    valor = dados()
    print(f"Valor obtido: {valor}")
    if valor in (7, 11):
        print("Você ganhou!")
    elif valor in (2, 3, 12):
        print("Você perdeu!")
    else:
        print(f"Seu ponto é {valor}! Rodada de pontuação a seguir! Lembre-se, que ao tirar 7 você recebe um come-out")
        while True:
            x = input(f"Aperte enter para lançar os dados(ponto: {valor}): ")
            valor1 = dados()
            print(f"Valor obtido: {valor1}")
            if valor1 == valor:
                print("Você ganhou!")
                break
            elif valor1 == 7:
                print("Você perdeu!")
                break
            print("Pontuação errada! Role novamente!")


craps()

