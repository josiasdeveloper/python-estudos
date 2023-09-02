import random
n = [0] * 100
for i in range(100):
    n[i] = random.randint(1,6)
c = {}
for i in n:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print(c)