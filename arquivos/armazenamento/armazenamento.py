def converter(x):
    return float(f"{x / (2 ** 20) : .2f}")


def percentual(y):
    espTotal = 0
    for k in range(len(y)):
        y[k] = converter(y[k])
        espTotal += y[k]
    for k in range(len(y)):
        y[k] = float(f"{y[k] / espTotal * 100 : .2f}")
    return y


def media(z):
    m = sum(z) / len(z)
    return float(f"{m:.2f}")


dados = open("dados.txt", "r")
lista = dados.readlines()
inf = []
dic = []
total = []

#for i in range(len(lista)):
    #inf.append(lista[i].split(" "))

#for i in range(len(lista)):
    #total.append(int(inf[i][1]))

porcentagem = percentual(total)

for i, (usuario, armazenamento, perc) in enumerate(zip(inf, total, porcentagem), start = 1):
    dic.append({
        "Nr": i,
        "Usuario": usuario[0],
        "Espaço utilizado": armazenamento,
        "% do uso": perc
    })

relatorio = open("relatorio.txt", "w")

relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n"
                "------------------------------------------------------------------------\n"
                "Nr.  Usuário        Espaço utilizado     % do uso\n")

for item in dic:
    relatorio.write(f"{item['Nr']: 2}   {item['Usuário']: < 15}    {item['Espaço utilizado']: < 18}")


relatorio.write(f"Espaço total ocupado: {converter(sum(total))} MB\n")
relatorio.write(f"Espaço médio ocupado: {media(total)} MB")

dados.close()
relatorio.close()
