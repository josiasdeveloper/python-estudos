ips = open("ips.txt", 'r')
lista = ips.readlines()
validos = []
invalidos = []
for i in range(len(lista)):
    ip = lista[i].split(".")
    v = True
    if len(ip) != 4:
        v = False
    else:
        for j in range(len(ip)):
            if not (0 <= int(ip[j]) <= 255):
                v = False
    if v:
        validos.append(lista[i])
    else:
        invalidos.append(lista[i])

relatorio = open("relatorio.txt", "w")
relatorio.write("[Endereços válidos]\n")
for i in range(len(validos)):
    relatorio.write(f"{validos[i]}\n")
relatorio.write("\n[Endereços inválidos]\n")
for i in range(len(invalidos)):
    relatorio.write(f"{invalidos[i]}\n")
ips.close()
relatorio.close()
