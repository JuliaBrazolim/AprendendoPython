nescau = float(input('Qual o valor do Nescau? '))
toddy = float(input('Qual o valor do Toddy? '))
xocopinho = float(input('Qual o valor do Xocopinho? '))

if nescau > toddy > xocopinho:
    print('O Xocopinho é mais barato, pois custa R$:', xocopinho)
elif toddy > xocopinho > nescau:
    print('O Toddy é mais barato que os outros, pois custa R$:', nescau)
elif nescau and toddy < xocopinho:
    print('O Nescau e o Toddy são mais baratos que o Xocopinho')
elif xocopinho and toddy < nescau:
    print('O Xocopinho e o Toddy são mais baratos que o Nescau')
elif nescau == toddy == xocopinho:
    print('Todos os achocolatados custam o mesmo preço, R$:', nescau, ', R$', toddy, ', R$', xocopinho)
else:
    print('O Toddy é o mais barato, pois custa R$', toddy)
