"""
Quetão 13 - Faça uma função que receba dois valores numéricos e um símbolo. Este simbolo representa a operação que
deseja efetuar com os números. Se for '+' deverá somar, '-' subatrair, '/' dividir, '*' multiplicar
"""
resultado = 0


def calculadora(simbolo, num1, num2):
    global resultado
    if simbolo == '+':
        resultado = num1 + num2
    if simbolo == '-':
        resultado = num1 - num2
    if simbolo == '/':
        resultado = num1 / num2
    if simbolo == '*':
        resultado = num1 * num2
    return resultado


print(calculadora('+', 3, 5))
print(calculadora('-', 3, 5))
print(calculadora('/', 3, 5))
print(calculadora('*', 3, 5))
