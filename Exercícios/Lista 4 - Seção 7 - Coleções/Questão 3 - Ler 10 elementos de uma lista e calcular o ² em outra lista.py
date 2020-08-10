# Questão 3 - Ler um conj de numeros reais, armezanando em uma lista e calcular o quadrado das componentes desse vetor
# armazenando o result em outra lista. O conjunto tem 10 elementos cada

i = 0
j = 0
soma_dos_quadrados = 0
lista = []

while i != 10:
    print('Digite um valor')
    numero = int(input())
    lista.append(numero)
    i = i + 1

while j != len(lista):
    soma_dos_quadrados = soma_dos_quadrados + (lista[j]**2)
    j = j + 1
print(f'A soma dos quadrados dos numeros inseridos foi: {soma_dos_quadrados}')