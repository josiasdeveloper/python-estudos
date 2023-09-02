n = int(input())
p = []
c = " "
for i in range(n):
    p.append(input())
    p[i] = p[i].replace(c, "")
    p[i] = p[i].lower()
    invertida = p[i][::-1]
    if invertida == p[i]:
        print("SIM")
    else:
        print("NAO")
