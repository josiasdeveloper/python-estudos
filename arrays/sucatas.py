m = {}
while True:
    n = input("Digite a identifiação do mouse: ")
    p = input("Digite o reparo necessário: ")
    m[n] = {'reparo': p}
    s = input("Deseja continuar? (S/N)")
    if s.upper() == "N":
        break
mouses = {}
for j in m.values():
    reparo = j['reparo']
    if reparo in mouses:
        mouses[reparo] += 1
    else:
        mouses[reparo] = 1
s = sum(mouses.values())
porcentagens = {}
for i, j in mouses.items():
    porcentagens[i] = j / s * 100
print(f"Quantidade de mouses: {len(m)}")
print("Situação        Quantidade   Percentual")
for i, j in mouses.items():
    print(f"{i}        {j}  {porcentagens[i]: .2f}")
