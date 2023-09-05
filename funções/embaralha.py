from random import sample


def anagrama(string):
    embaralha = sample(string, len(string))
    a = ''.join(embaralha)
    print(a.lower())


palavra = input("Digite uma palavra: ")
anagrama(palavra)
