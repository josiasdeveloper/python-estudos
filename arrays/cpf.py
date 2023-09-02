import random
def verificarcpf (cpf):
    s = 0
    j = 0
    for i, j in zip(range(10, 1, -1), range(9)):
        s += int(cpf[j]) * i
    verificador1 = 11 - (s % 11)
    s = 0
    for i, j in zip(range(11, 1, -1), range(10)):
        s += int(cpf[j]) * i
    verificador2 = 11 - (s % 11)
    if verificador1 == int(cpf[9]) and verificador2 == int(cpf[10]):
        return True
    else:
        return False

n = [0] * 11
i = 0
while True:
    n[i] = random.randint(0, 11)
    i += 1
    if i == 7:
        print("x", end = "")
        if verificarcpf(n):
            break
        else:
            i = 0
            n = [0] * 11
print(n)



