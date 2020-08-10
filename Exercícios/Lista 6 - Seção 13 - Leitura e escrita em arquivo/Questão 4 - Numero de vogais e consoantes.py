"""
Questão 4 - Receba um texto e mostre quantas são vogais e quantas são consoantes
"""

numero_de_vogais = 0
num_letra = 0
num_de_espacos = 0
with open('questao2.txt', 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()

for vogal in texto:
    if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
        numero_de_vogais = numero_de_vogais + 1
    if vogal == 'A' or vogal == 'E' or vogal == 'I' or vogal == 'O' or vogal == 'U':
        numero_de_vogais = numero_de_vogais + 1
for letra in texto:
    num_letra = num_letra + 1
for espacos in texto:
    if espacos == ' ':
        num_de_espacos = num_de_espacos + 1
print(f'O texto possui {numero_de_vogais} vogais e {num_letra - numero_de_vogais - num_de_espacos} consoantes')




