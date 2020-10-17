a = float(input('Insira um numero: '))
b = float(input('Insira um numero: '))
c = float(input('Insira um numero: '))

if a > b and c:
    print('o numero', a, 'é o maior')
elif c > a and b:
    print('o numero', c, 'é o maior')
else:
    print('o maior numero é', b)
