i = 0
n = []
c = 0
s = 0
media = []
abaixo = []
while c != -1:
    n.append(float(input()))
    c = n[i]
    i+=1
n.remove(-1)
for j in range(len(n)):
    s += n[j]
m = s/i
for j in range(len(n)):
    if n[j] > m:
        media.append(n[j])
    if n[j] < 7.0:
        abaixo.append(n[j])
print(f"Quantidade de números lidos: {i}")
print(f"Números lidos: {n}")
print(f"Ordem inversa: {n[::-1]}")
print(f"Soma dos valores: {s}")
print(f"Média dos valores: {m:.2f}")
print(f"Valores acima da media: {media}")
print(f"Valores abaixo de 7: {abaixo}")

