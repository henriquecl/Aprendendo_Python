# Exercício 10 - programa de calcular imc se for homem uma formula
# se for mule outra formula

altura = float(input('Digite sua altura em metros\n'))
sexo = input('Digite seu sexo\n')

if sexo == 'masculino':
    print(f"Seu imc é: {((72.7*altura)-58)}")
elif sexo == 'feminino':
    print(f"Seu imc é: {((62.1*altura)-44.7)}")
else:
    print('Houve algum erro de digitação')
