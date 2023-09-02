def valorPagamento(x, y):
    if y == 0:
        return x
    else:
        j = x * 0.001 ** y
        v = x * 1.03
        x = v + j
        return x


s = []
while True:
    salario = int(input())
    if salario == 0:
        break
    atraso = int(input())
    s.append(valorPagamento(salario, atraso))
totalPago = sum(s)
print("Relatorio do dia: ")
for i in range(len(s)):
    print(f"Pagamento {i+1} : {s[i]: .2f}")
print(f"Pagamentos totais: {totalPago}")
