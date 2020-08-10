# Questão 19 - Verificar se um inteiro é divisivel por 3 ou por 5
# mas nao pelos dois simultaneamente

num1 = int(input('Digite um número\n'))

div_por3 = num1 % 3
div_por5 = num1 % 5

if div_por3 == 0 and div_por5 == 0:
    print('O valor é divísivel por 5 e 3 simultaneamente')
elif div_por3 == 0:
    print('O número é divisível por 3')
elif div_por5 == 0:
    print('O valor é divísivel por 5')
