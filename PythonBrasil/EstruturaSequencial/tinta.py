# -*- coding: utf-8 -*-
metros = float(input('Quantos metros quadrados de área será pintada? '))
litros = metros / 3
precoL = 80
capacidadeL = 18
latas = litros / capacidadeL
total = latas * precoL
print('Você precisa usar', int(latas), 'de latas para pintar')
print('\n O valor total é de R$', int(total))




