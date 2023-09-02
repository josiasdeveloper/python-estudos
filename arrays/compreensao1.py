n = ['cristo','ana','jantar','mulher','planeta','sexo','computador','cristianismo','estudos']
a = ['a','e','i','o','u']
n1 = [vogal for palavra in n for vogal in palavra if vogal in 'aeiouAEIOU' ]
print(n1)