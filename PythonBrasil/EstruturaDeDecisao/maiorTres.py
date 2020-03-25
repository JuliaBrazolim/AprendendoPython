a = float(input('Insira um numeros: '))
b = float(input('Insira um numeros: '))
c = float(input('Insira um numeros: '))

if a > b and c:
    print('o numero', a, 'é o maior')
elif c > a and b:
    print('o numero', c, 'é o maior')
else:
    print('o maior numero é', b)