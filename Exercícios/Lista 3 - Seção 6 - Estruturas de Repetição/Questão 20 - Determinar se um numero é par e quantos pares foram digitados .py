# Questão 20 - Ler uma sequencia de numeros inteiros e determinar se são pares ou não.
# Deverá informar o nº de dados lidos e nº de valores pares. O processo termina quando
# for digitado o número 1000

numero = 0
i = 0
j = 0
while numero != 1000:
    numero = int(input('Digite os valores, e digite 1000 quando quiser parar\n'))
    if numero != 1000:
        i = i + 1
        if numero % 2 == 0:
            j = j + 1
print(f'Foram lidos {i} números, sendo entre eles {j} numeros pares')
