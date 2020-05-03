# Questão 18 - Calculadora

operacao = input("Digite qual operação você quer fazer entre "
                 "soma,diferença,divisão ou multiplicação\n")
num1 = float(input("Digite um número\n"))
num2 = float(input("Digite outro número\n"))

if operacao == 'soma':
    print(f"O resultado da soma é: {num1+num2}")
elif operacao == 'diferença':
    print(f"O resultado da diferença é: {num1-num2}")
elif operacao == 'divisão':
    print(f"O resultado da divisão é: {num1/num2}")
elif operacao == 'multiplicação':
    print(f"O resultado da multiplicação é: {num1*num2}")
else:
    print("Operação inválida.")
