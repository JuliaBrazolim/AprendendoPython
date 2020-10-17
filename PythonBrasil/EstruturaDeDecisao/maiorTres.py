a = float(input('Insira um numero: '))
b = float(input('Insira um numero: '))
c = float(input('Insira um numero: '))

if a > b > c:
    print('o numero', a, 'é o maior dos três valores')
elif b > a < c:
    print('o numero', b, 'é o maior dos três valores')
else:
    print('o maior numero dos três é', c)
