""""
# Questão 1 - Faça um programa que possua um vetor denominado A, que armazene 6 numeros inteiros

A = [1, 0, 5, -2, -5, 7]
print(A)
# letra b)

soma = A[0] + A[1] + A[5]
print(soma)

# letra c)

A.pop(3)
A.insert(3, 100)
print(A)

# letra d)
i = 0
while i != len(A):
    i = i + 1
    print(A[i])

Questão 2 - Crie um programa que leia 6 valores inteiros , e em seguida, mostre na tela os valores lidos

i = 0
lista = []
while i != 6:
    print('Digite um valor inteiro')
    numero = input()
    lista.append(numero)
    i = i + 1
print(f'{lista}')

Questão 3 - Ler um conj de numeros reais, armezanando em uma lista e calcular o quadrado das componentes desse vetor
armazenando o result em outra lista. O conjunto tem 10 elementos cada

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


Questão 4 - Faça um programa que leia uma lista[8], e em seguida leia dois valores X,Y que sejam correspondente a duas
posições da lista. Ao final, o programa deve escrever a smoma dos valores encontrados nas posições X e Y
lista = []
numero = 0

for i in range(8):
    print(f'Digite {8- i} valores')
    numero = int(input())
    lista.append(numero)
X = int(input('Digite um valor entre 0 e 7 \n'))
Y = int(input('Digite outro valor entre 0 e 7 \n'))
print(lista)
lista[X] = (X+Y)
lista[Y] = (X+Y)
print(lista)

Questão 5 - Leia uma lista de 10 valores. Conte e escreva quantos valores pares ele possui
lista = []
numero = 0
contagem = 0
for i in range(10):
    print(f'Digite {10- i } valor(es)')
    numero = int(input())
    lista.append(numero)

for j in range(len(lista)):
    if lista[j] % 2 == 0:
        contagem = contagem + 1
print(f'A lista tem {contagem} numer(os) par(es)')

# Questão 6 - Faça um programa que receba do usúario uma lista de 10 valores, e em seguida imprimir o maior e menor
# elemento da lista
numero = 0
lista = []
for i in range(10):
    print(f'Digite {10 - i} valor(es)')
    numero = int(input())
    lista.append(numero)
lista.sort()
maior_valor = lista[9]
menor_valor = lista[0]
print(f'O maior valor foi {maior_valor}, e o menor valor foi {menor_valor}')


# Questão 7 n faz nem sentido fazer

# Questão 8 - Crie um programa q lê 6 valores inteiros e mostre na tela os vlaores lidos na ordem inversa

lista = []
numero = 0
for i in range(6):
    print(f'Digite {6-i} valor(es)')
    numero = int(input())
    lista.append(numero)
print(lista)
lista.reverse()
print(lista)

# Questão 9 - Crie um programa q lê 6 valores pares e mostre na tela os valores lidos na ordem inversa
lista = []
numero = 0

for i in range(6):
    print(f'Digite {6-i} valor(es) pares')
    numero = int(input())
    while numero % 2 != 0:
        print('Digite um valor par')
        numero = int(input())
    lista.append(numero)
lista.reverse()
print(lista)

Questão 10 - Faça um progrmaa para ler a nota da prova de 15 alunos, calcule e imprima a média geral

notas = []
nota_individual = 0

for i in range(15):
    print(f'Digite as {15-i} notas')
    nota_individual = float(input())
    notas.append(nota_individual)
media_geral = (sum(notas))/(len(notas))
print(f'A média geral foi {media_geral}')

Questão 11 - Faça um programa que lista 10 valores reais, calcule e mostre a quantidade de negativos e a
soma dos números positivos dessa lista

lista = []
numero = 0
qtd_num_negativos = 0
soma_num_positivos = 0
for i in range(10):
    print(f'Digite {10-i} valores:')
    numero = float(input())
    lista.append(numero)

for j in range(len(lista)):
    if lista[j] < 0:
        qtd_num_negativos = qtd_num_negativos + 1

for j2 in range(len(lista)):
    if lista[j2] >= 0:
        soma_num_positivos = soma_num_positivos + lista[j2]
print(f'Dos valores inseridos {qtd_num_negativos} são negativos,e a soma dos positivos foi:{soma_num_positivos}')

# Questão 12 - Faça um programa para ler 5 valores, mostrar todos os valores lidos, junto com o maior valor,
# o menor e a média dos valores
numero = 0
lista = []
for i in range(5):
    print(f'Digite {5-i} valor(es)')
    numero = float(input())
    lista.append(numero)

print(f'Os valores inseridos foram {lista} maior valor inserido foi {max(lista)}, o menor {min(lista)}')
print(f'Já a media dos valores inseridos foi {sum(lista)/len(lista)}')

# Questão 13 - Não faz nem sentido fazer

# Questão 14 - Faça um progrmaa que leia 10 valores e verifique se existem valores iguais e os escreva na tela

lista = []
numero = 0

for i in range(10):
    print(f'Digite {10-i} valor(es)')
    numero = float(input())
    lista.append(numero)

for j in range(11):
    if lista.count(lista[j]) > 1:
        print(f'O valor {lista[j]} se repetiu {lista.count(lista[j])} vezes ')

# Questão 15 - Leia 20 valores. Escreva os elementos do vetor eliminando elementos repetidos

lista = []
numero = 0

for i in range(20):
    print(f'Digite {20-i} numer(os)')
    numero = float(input())
    lista.append(numero)
print(lista)
for j in range(20):
    if lista.count(lista[j]) > 1:
        lista[j] = 0
print(lista)


# Questão 16 - Faça um progrmama que leia 5 numeros reais, e depois um código inteiro.
# Se o código for 0: Para
# Se o código for 1: Mostre o vetor na ordem direta
# Se o código for 2: Mostre o vetor na ordem inversa
# Caso o código for diferente de 1 e 2 escreva uma mensagem informando q oc ódigo é invalido

lista = []
numero = 0


for i in range(5):
    print(f'Digite {5 - i} numer(os)')
    numero = float(input())
    lista.append(numero)
i = int(input('Digite a operação que deseja\n'))

if i != 1 or i != 2 or i !=0:
    print('Código inválido')

if i == 1:
    print(f'Os valores inseridos foi: {lista}')

if i == 2:
    lista.reverse()
    print(f'Os valores interidos foi {lista}')

if i == 0:
    print('O programa foi finalizado')

# Questão 17  - Leia 10 valores e atribua o valor 0 para todos os elementos que forem negativos

lista = []
numero = 0

for i in range(20):
    print(f'Digite {20-i} numer(os)')
    numero = float(input())
    lista.append(numero)
print(lista)
for j in range(20):
    if lista[j] < 0:
        lista[j] = 0
print(lista)

Questão 18 - Faça um prog q leia 10 numeros, leia o numero x. Conte os múltiplos de um número inteiro X e mostre-os
na tela

lista = []
lista_dos_multiplos = []
numero = 0

for i in range(10):
    print(f'Digite {10-i} valor(es)')
    numero = float(input())
    lista.append(numero)
X = int(input('Digite um valor para que eu diga quem são seus multiplos\n'))

for j in range(10):
    if lista[j] % X == 0:
        lista_dos_multiplos.append(lista[j])
print(f'O número na lista que são multiplos de {X} são: {lista_dos_multiplos}')

# Questão 19 - Faça um vetor de tamanho 50 ser preenchido com (i+5*i)%(i+1), sendo i a posição. Imprima o vetor

lista = []
numero = 0

for i in range(50):
    numero = (i+(5*i)) % (i+1)
    lista.append(numero)
print(lista)

# Questão 20 - Escreva um programa que leia numeros inteiros no intervalo de [0,50] e os armazene em umalista de 10 posi
# ções. Preencha uma segunda lista apenas com os números impares.

lista1 = []
lista2 = []
numero = 0

for i in range(10):
    numero = float(input('Digite um valor de 0 a 50\n '))
    while numero > 50 or numero < 0:
        numero = float(input('Digite um valor de 0 a 50 teste\n '))
    lista1.append(numero)
print(lista1)  # Só teste
for j in range(10):
    if lista1[j] % 2 != 0:
        lista2.append(lista1[j])
print(f'Os numeros impares foram:{lista2}')


# Questão 21 - Faça um programa que receba dois vetores, A e B, com 10 numeros cada, Crie um novo vetor C. C = A - B
# Mostre na tela os dados do vetor C

A = []
B = []
C = []
numero = 0

for i1 in range(10):
    print(f'Digite {10-i1} numer(os)')
    numero = float(input())
    A.append(numero)

for i2 in range(10):
    print(f'Digite {10-i2} numer(os)')
    numero = float(input())
    B.append(numero)

for i3 in range(10):
    C.append(A[i3]-B[i3])
print(A)
print(B)
print(C)


# Questão 22 - Faça um programa que elia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares
# os valores do primeiro vetor, e nas impares os valores do segundo

A = []
B = []
C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numero = 0

for i1 in range(10):
    print(f'Digite {10-i1} numer(os)')
    numero = float(input())
    A.append(numero)

for i2 in range(10):
    print(f'Digite {10-i2} numer(os)')
    numero = float(input())
    B.append(numero)

for i3 in range(0, 10, 2):
    C.pop(i3)
    C.insert(i3, A[i3])

for i4 in range(1, 10, 2):
    C.pop(i4)
    C.insert(i4, B[i4])

print(A)
print(B)
print(C)


# Questão 23 - Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
# imprimir os dois conjuntos e o produto escalar

A = []
B = []
numero = 0
produto_escalar= 0

for i1 in range(5):
    print(f'Digite {5-i1} numer(os)')
    numero = float(input())
    A.append(numero)

for i2 in range(5):
    print(f'Digite {5-i2} numer(os)')
    numero = float(input())
    B.append(numero)

for i3 in range(5):
    produto_escalar = produto_escalar + (A[i3]*B[i3])
print(f'Os vetores digitados foram:{A} e {B}')
print(f'O resultado do produto escalar foi:{produto_escalar}')


# Questão 24 - Faça um programa que leia 10 conjuntos de 2 valores, o primeiro representando o número do aluno.
# O segunto sua altura em metros. Encontre o mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais
# alto, juntamente com suas alturas
# Fiz só pra 3 alunos, para 10 era só repetir o programa mudando os indices
A1 = []
A2 = []
A3 = []
roll_de_alturas = []
numero1 = 0
numero2 = 0
numero3 = 0

for i1 in range(1):
    print(f'Digite sua altura:')
    numero1 = float(input())
    A1.append(1)
    A1.append(numero1)
    roll_de_alturas.append(numero1)

for i2 in range(1):
    print(f'Digite sua altura:')
    numero2 = float(input())
    A2.append(2)
    A2.append(numero2)
    roll_de_alturas.append(numero2)

for i3 in range(1):
    print(f'Digite sua altura:')
    numero3 = float(input())
    A3.append(3)
    A3.append(numero2)
    roll_de_alturas.append(numero2)

if max(roll_de_alturas) == numero1:
    print(f'O aluno de numero 1 é o mais alto e mede {max(roll_de_alturas)}')
elif min(roll_de_alturas) == numero1:
    print(f'O aluno de numero 1 é o mais baixo e mede {min(roll_de_alturas)}')

if max(roll_de_alturas) == numero2:
    print(f'O aluno de numero 2 é o mais alto e mede {max(roll_de_alturas)}')
elif min(roll_de_alturas) == numero2:
    print(f'O aluno de numero 2 é o mais baixo e mede {min(roll_de_alturas)}')

if max(roll_de_alturas) == numero3:
    print(f'O aluno de numero 2 é o mais alto e mede {max(roll_de_alturas)}')
elif min(roll_de_alturas) == numero3:
    print(f'O aluno de numero 2 é o mais baixo e mede {min(roll_de_alturas)}')


# Questão 25 - Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são múltiplos
# ou que terminam com 7

lista = []

for i1 in range(100):
    if i1 % 7 != 0 and i1 % 10 != 7:
        lista.append(i1)

print(lista)


# Questão 26 - Faça um programa que calcule o desvio padrão de um vetor (só escrever mt coisa mas lógica simples, pulei)


# Questão 27 - Leia 10 num e armazene num vetor. Em seguia escreva os elementos que são primos e suas respectivas
# posições no vetor

lista = []
divisores = []
for j in range(10):
    print(f'Digite {10 - j} numeros para que eu diga quais são primos:')
    numeros1 = int(input())
    lista.append(numeros1)

for i in range(10):
    for j1 in range(1, lista[i]+1):
        teste = lista[i] / j1
        if int(teste) == teste:
            divisores.append(teste)
    if len(divisores) == 2:
        print(f'O número {lista[i]} é primo e sua posição é {i}')
        divisores.clear()
    elif len(divisores) > 2:
        divisores.clear()


# Questão 28 - Leia 10 números inteiros e armazene em v. Crie dois novos vetores v1 e v2. Copie os impares para v1 e par
# para v2.

v = []
v1 = []
v2 = []
for i in range(10):
    numero = int(input('Digite um número\n'))
    v.append(numero)

for i2 in range(10):
    if v[i2] % 2 != 0:
        v1.append(v[i2])

for i3 in range(10):
    if v[i3] % 2 == 0:
        v2.append(v[i3])

print(v1)
print(v2)

# Questão 29 - Faça um programa que receba 6 números inteiros e mostre:
# Os númeors pares digitados.
# A soma dos números pares
# Os números impares
# A quantidade de números impares

lista = []
numeros_pares = []
numeros_impares = []

for i in range(6):  # Recebendo os dados
    numero = int(input('Digite um número\n'))
    lista.append(numero)

for i2 in range(6):  # Números pares
    if lista[i2] % 2 == 0:
        numeros_pares.append(lista[i2])

for i3 in range(6): # Números impares
    if lista[i3] % 2 != 0:
        numeros_impares.append(lista[i3])

print(f'Os números pares digitados foram: {numeros_pares}, e a soma deles foi {sum(numeros_pares)}')
print(f'Os números impares digitados foram: {numeros_impares}, e a quantidade deles foi {len(numeros_pares)}')

# Questão 30 - Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2
# Ou seja, contem apenas os numeros que estão em ambos os vetores.
# PAROU AQUI A PARTE DE LISTA. TEM Q VER AS OUTRAS AULAS.
lista1 = []
lista2 = []
lista_de_intersecao = []

for i in range(10):

    numero = int(input('Digite um número\n'))
    lista1.append(numero)


for i2 in range(10):
    numero = int(input('Digite um número\n'))
    lista2.append(numero)

lista_de_intersecao = (set(lista1).intersection(set(lista2)))

print(lista1)
print(lista2)
print(lista_de_intersecao)



# Questão 31 - Faça um prg q leia 2 vetores de 10 elementos. Crie um vetor que seja a união de ambos sem repetição

lista1 = []
lista2 = []
lista_de_uniao = []

for i in range(10):
    numero = int(input(f'Digite {10-i} valores\n'))
    lista1.append(numero)

for i2 in range(10):
    numero = int(input(f'Digite {10-i2} valores\n'))
    lista2.append(numero)

lista_de_uniao = set(lista1).union(set(lista2))

print(lista1)
print(lista2)
print(lista_de_uniao)


# Questão 32 - Leia dois vetores inteiro x e y, cada um com 5 elementos (assuma que o usuário não informe repetidos)
# Calcule e mostre os vetores resultantes em cada passo abaixo:
# a) soma entre x e y;
# b) produto entre x e y;
# c) diferença entre x e y;
# d) interseção entre x e y;
# e) união entre x e y.


x = []
y = []
uniao = []
intersecao = []
elementos_que_nao_existem = []
# Coletando os dados
for i in range(5):
    numero = int(input(f'Digite {5-i} valor(es)\n'))
    x.append(numero)

for i2 in range(5):
    numero = int(input(f'Digite {5-i2} valor(es)\n'))
    y.append(numero)

# soma, diferença e produto

for i3 in range(5):
    soma = x[i3] + y[i3]
    diferenca = x[i3] - y[i3]
    produto = x[i3] + y[i3]
    print(f'A soma dos valores na posição {i3} foi {soma}, a diferença entre eles {diferenca}'
          f' e o produto entre eles é {produto}')

# intereseção e união

intersecao = (set(x).intersection(set(y)))
uniao = (set(x).union(set(y)))
elementos_que_nao_existem = set(x).difference(set(y))
print(f'Os elementos que tem em X que não tem em Y são {elementos_que_nao_existem}')
print(f'A interseção dos dois conjuntos é:{intersecao}')
print(f'A união dos dois conjuntos é:{uniao}')


# Questão 33- Faça um programa que leia um vetor de 15 posições  e o compacte, ou seja, elimine posições com valor 0.
# para isso, todos os elementos a frente do zero devem ir para esquerda.

lista = []
lista_compactada = []
for i in range(15):
    numero = int(input(f'Digite {15-i} valores:\n'))
    lista.append(numero)

for i2 in range(len(lista)):
    if (lista[i2]) != 0:
        lista_compactada.append(lista[i2])
print(lista_compactada)

# Questão 34 - Faça um prog para ler 10 num diferentes a serem armazenados em um vetor. Os dados devem ser amazenados
# no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que ja foi digitado anteriormente
# o programa deverá pedir para ele digitar outro numero. Exibir na tela o vetor final digitado

conjunto = set()

while len(conjunto) != 10:
    numero = int(input(f'Digite {10 - len(conjunto)} valores diferentes:\n'))
    conjunto.add(numero)
print(conjunto)

# Questão 35 - Faça um prog q leia dois numeros a e b (positivos menores que 10000) e:
# crie um vetor onde cada posição é um algarismo do numero. A primeira posição é o alg. menos. sig
# crie um vetor que a soma de a e b, mas faça-o usando apenas os vetores contruidos anteriormente
# PREGUIÇA

# Questão 36 - Leia um vetor com 10 numeros reais, ordene os elementos desse vetor e no final escreva os elementos
# do vetor ordenado
# JÁ FEITO ANTERIORMENTE


# Questão 37 - Considerar um vetor de 11 elementos, imprimir o vetor de 0a6 em ordem crescente e de 711 decrescente
lista = []
lista_final = []
lista_crescente = []
lista_decrescente = []

for i in range(11):
    numero = int(input(f'Digite {11 - i} valores\n'))
    lista.append(numero)

lista.sort()

lista_crescente = list(lista.copy()[0:6])
lista_decrescente = list(lista.copy()[11:6:-1])
lista_final = lista_crescente.copy() + lista_decrescente.copy()
print(lista_final)


# Questão 38 - Peça ao usuário 10 numeros e ordene por ordem crescente. Ordene assim que digitar. Mostre na tela
lista = []
for i in range(10):
    numero = float(input(f'Digite {10 - i } numeros.\n'))
    lista.append(numero)
    lista.sort()
    print(lista)



# Questão 39 - Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado triang
# ulo de pascal

# PREGUIÇA
"""
