s = input()
j = 0
invertida = []
invertida = [" "] * len(s)
for i in range(len(s)-1, -1, -1):
    invertida[j] = s[i]
    j+= 1
invertida = "".join(invertida)
print(invertida) # só pra não usar fatiador e ficar muito fácil