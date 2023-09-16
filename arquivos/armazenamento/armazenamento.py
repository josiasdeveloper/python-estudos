import re
def converter(x):
    return float(f"{x / (2 ** 20) : .2f}")


def percentual(y):
    espTotal = 0
    percentuais = []

    for valor in y:
        espTotal += converter(valor)

    for valor in y:
        percentual_calculado = float(f"{converter(valor) / espTotal * 100 : .2f}")
        percentuais.append(percentual_calculado)

    return percentuais



def media(z):
    m = sum(z) / len(z)
    return float(f"{m:.2f}")


dados = open("dados.txt", "r")
lista = dados.readlines()
total = []
for i in range(len(lista)):
    lista[i] = (re.sub(" +", " ", lista[i]))
    lista[i] = (lista[i].replace("\n", "")).split(" ")
    total.append(int(lista[i][1]))
dic = []
porcentagem = percentual(total)
for i, (inf, perc) in enumerate(zip(lista, porcentagem), start=1):
    dic.append({
       'Nr': i,
        'Usuario': inf[0],
        'Armazenamento': converter(int(inf[1])),
        'Percentual': perc
    })

relatorio = open("relatorio.txt", "w")

relatorio.write('''ACME Inc. -> Uso do espaço em disco pelos usuários\n
------------------------------------------------------------------------\n
Nr.    Usuário       Espaço utilizado     % do uso\n''')

for item in dic:
    relatorio.write(f"{item['Nr'] : 2}     {item['Usuario'] : <10}    {item['Armazenamento'] : <17}   {item['Percentual'] : < 6}%\n")

relatorio.write(f"\nEspaço total utilizado: {converter(sum(total))} MB")
relatorio.write(f"\nMedia de uso: {converter(media(total)): .2f} MB")

dados.close()
relatorio.close()
