def extenso(n):
        numeros = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5 :'cinco', 6: 'seis', 7: 'sete', 8 : 'oito', 9: 'nove',
                   10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'catorze', 15: 'quinze', 16: 'dezesseis', 17:  'dezessete',
                   18: 'dezoito', 19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta',
                   70: 'setenta', 80: 'oitenta', 90: 'noventa'}
        if n in numeros:
            return numeros[n]
        else:
            d = int(n / 10) * 10
            u = n % 10
            return f"{extenso(d)} e {extenso(u)}"
n = int(input())
e = extenso(n)
print(e)
