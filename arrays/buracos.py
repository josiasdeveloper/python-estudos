n = int(input())
s = []
a = 0
for i in range(n):
    s.append(input())
for i in range(n):
    for j in range(len(s[i])):
        if s[i][j].upper() == "A" or s[i][j].upper() == "O" or  s[i][j].upper() == "P" or s[i][j].upper() == "R" or s[i][j].upper() == "Q" or s[i][j].upper() == "D":
            a += 1
        elif s[i][j].upper() == "B":
            a+= 2
    print(a)
    a = 0
