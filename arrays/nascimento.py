def meses(mes):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
             'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    return meses[mes - 1]
d = input()
dL = d.split('/')
mes = meses(int(dL[1]))
print(f"Você nasceu em {dL[0]} de {mes} de {dL[2]}")
