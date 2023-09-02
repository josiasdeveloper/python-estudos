print("Projeção de Gastos com Abono")
print("============================")
s = []
i = 0
while True:
    s.append(float(input()))
    if s[i] == 0:
        s.remove(s[i])
        break
    else:
        i += 1
a = {}
n = 0
k = 0
for j in s:
    if s[k] <= 500:
        a[j] = 100
        n += 1
    else:
        a[j] = s[k] * 0.2
    k += 1
t = sum(a.values())
maior = max(s)
print("Salário:      Abono:")
for chave, valor in a.items():
    print(f"{chave}R$    {valor}R$")
print(f"Foram processados {i} colaboradores\nTotal gasto com abonos: {t}R$\nValor mínimo pago à {n} colaboradores\nMaior valor pago de abono: {a[maior]}R$")

