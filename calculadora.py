# First Calculator - Exercício SoloLearn
inicio = "iniciar"
q = "finalzar"
print('Calculadora Simples')
print('_________')
print('Esocolha o símbolo da expressão para realizar o cálculo ')
print('+')
print('-')
print('*')
print('/')

while inicio != 'w':
    num1 = float(input("Insira um numero: "))
    num2 = float(input("Insira outro numero: "))
    inicio = input('Insira uma expressão: ')
    try:
        if inicio == '+':
            resultado = num1 + num2
            print('O Resultado é ', float(resultado))
        elif inicio == '-':
            resultado = num1 - num2
            print('O resultado é ', float(resultado))
        elif inicio == '*':
            resultado = num1 * num2
            print('O resultado é ', float(resultado))
        elif inicio == '/':
            resultado = num1 / num2
            print('O resultado é ', float(resultado))
        else:
            print('Finalizando...', q)
    except:
        print("Errooou")
