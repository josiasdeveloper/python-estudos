n = {num if len([i for i in range(2, num+1) if num % i == 0]) != 1 else f"{num} (primo)":
         [i for i in range(2, num+1) if num % i == 0] for num in range(2, 100)}
k = 0
for i,j in n.items():
    print(f"{i} : {j} | ", end = "")
    k+=1
    if k == 3:
        k = 0
        print(' ')

