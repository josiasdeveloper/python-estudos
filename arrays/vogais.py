n = input()
c = ['a','e','i','o','u']
v = {}
v[" "] = 0
for i in c:
    v[i] = 0
for i in n:
    if i == " ":
        v[" "] += 1
    if i.lower() in c:
        v[i.lower()] += 1
print(v)


