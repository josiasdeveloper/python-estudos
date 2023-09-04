def validarData(x):
    partes = x.split("/")
    diasPorMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    if mes > 12 or dia > 31:
        return False
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        diasPorMes[2] = 29
    if dia > diasPorMes[mes]:
        return False
    return True


def dataExtenso(data):
    data = data.split("/")
    datas = [0, "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
             "Agosto", "Setembro", "Outubro", "Novembro"]
    extenso = f"{data[0]} do {datas[int(data[1])]} de {data[2]}"
    print(extenso)


while True:
    entrada = input("Digite a data: ")
    if validarData(entrada):
        dataExtenso(entrada)
        break
    else:
        print("Data inválida")
