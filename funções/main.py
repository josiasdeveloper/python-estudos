def converter(x):
    y = int(x.split(":")[0])
    if y > 12:
        x = x.replace(f"{y}", f"{y - 12}") + " P.M"
        return x
    else:
        x = x + " A.M"
        return x


while True:
    n = input("Digite a hora: ")
    print(converter(n))
    b = input("Deseja continuar? (S/N)")
    if b.upper() != "S":
        break
