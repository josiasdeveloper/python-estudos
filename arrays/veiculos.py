v = {}
for i in range(5):
    print(f"Veículo {i+1}: ")
    nome = input("Nome: ")
    consumo = float(input("Consumo: "))
    l = float(f"{1000/consumo:.2f}")
    veiculo = {'Nome': nome, 'Consumo': consumo, 'Litros para cada 1000km': l, 'Gasto': f"{l * 5.4: .2f}"}
    chave = f"Veículo {i+1}"
    v[chave] = veiculo
menorConsumo = float('inf')
vMenorConsumo = None
for i, j in v.items():
    consumo = j['Consumo']
    if consumo > menorConsumo:
        menorConsumo = consumo
        vMenorConsumo = i
print("Relatório final: ")
for k in v.items():
    print(k)
print(f"Veiculo com menor consumo: {v[i]['Nome']}")
