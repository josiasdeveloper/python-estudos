def imprimir(n1,n2):
    print("Jogadores      Votos     Porcentagem")
    for i,j in n1.items():
        print(f"{i}               {j}        {n2[i]: .2f}%")


n = []
i = 0

while True:
    n.append(int(input("Digite seu voto: (0=sair) ")))
    if n[i] != 0:
        while n[i] < 1 or n[i] > 23:
            n.remove(n[i])
            n.append(int(input("Voto inválido. Digite seu voto: (0=sair) ")))
    else:
        n.remove(n[i])
        break
    i += 1

votos = {}

for j in n:
    if j in votos:
        votos[j] += 1
    else:
        votos[j] = 1

porcentagem = {}
s = sum(votos.values())

for chave, valor in votos.items():
    porcentagem[chave] = votos[chave] / s * 100

imprimir(votos, porcentagem)
maior= max(votos, key=votos.get)
print(f"O craque do jogo foi o camisa {maior} com {votos[maior]} votos e {porcentagem[maior]: .2f}% dos votos")