def imprimir(n1,n2):
    print("Sistema     Votos    %")
    for i, j in n1.items():
        print(f"{i}      {j}     {n2[i]: .2f}")

n = ['Windows', 'MacOS', 'Unix', 'Linux','Netware', 'Outros']
x = {}
for i in n:
    x[i] = 0
while True:
    a = input("Qual o melhor Sistema Operacional para uso em servidores?\nWindows\nUnix\nLinux\nMacOS\nOutro\nNetware\n(0 = sair)\n")
    if a == '0':
        break
    else:
        x[a] += 1
s = sum(x.values())
porcentagem = {}
for i, j in x.items():
    porcentagem[i] = j / s * 100
maior = max(x, key=x.get)
imprimir(x,porcentagem)
print(f"O sistema vencedor foi {maior} com {x[maior]} votos e {porcentagem[maior]: .2f}% dos votos")


