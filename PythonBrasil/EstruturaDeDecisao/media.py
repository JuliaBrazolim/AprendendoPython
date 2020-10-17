nota1 = float(input('Insira o valor da sua nota: '))
nota2 = float(input('Insira a outra nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media <= 9:
    print('Aprovada!')
elif media <= 6:
    print('Reprovada')
elif media == 10:
    print('Aprovada com Louvor')
