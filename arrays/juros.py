n = input()
n_str = n.split()
numeros = [float(numero) for numero in n_str]
a = int((4 * numeros[2]+1))
m = [0] * a
r = [0] * a
m[0] = numeros[0]

for i in range(1, a):
    r[i] = m[i - 1] * numeros[1]
    m[i] = r[i] + m[i - 1]

m = [format(item, '.2f') for item in m]
r = [format(item, '.2f') for item in r]
for i in range(1,a):
    print(f"Rendimento: {r[i]} Montante: {m[i]}")
print("eu")