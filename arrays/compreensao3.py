n = [i for i in range(2, 51) if all(i % div != 0 for div in range(2, int((i**0.5)) + 1))]
print(n)
