n1 = input()
n2 = input()
for i in range(len(n2)):
    n1 = n1.replace(n2[i], "")
print(n1)


