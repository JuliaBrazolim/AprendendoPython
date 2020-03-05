# -*- coding: utf-8 -*-


def calcularMultas():
    peso = int(input("Quantos kilos você pescou? "))
    excesso = peso - 50
    multas = peso * 4

    if multas >= 50 * 4:
        print('\n Você pescou ', excesso, 'kilos a mais que o permitido!')
        print("Terá que pagar: R$", float(multas), 'em multas.')
    else:
        print("Você está isento de multas!")

calcularMultas()


