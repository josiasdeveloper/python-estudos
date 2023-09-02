import random
f = ['banana', 'carro', 'computador', 'programação', 'jesus', 'mitsubishi']
s = random.choice(f)
f1 = ['_'] * len(s)
k = 0
while True:
    a = input('Digite uma letra: ')
    if a in s:
        j = [i for i, letra in enumerate(s) if letra == a]
        for i in j:
            f1[i] = a
        f1 = "".join(f1)
        print(f"Correto! {f1}")
        f1 = list(f1)
    else:
        print('Incorreto! Tente novamente')
        k += 1
    if "".join(f1) == s:
        print("Parabéns!!")
        break
    if k == 6:
        print("Perdeu!")
        break
