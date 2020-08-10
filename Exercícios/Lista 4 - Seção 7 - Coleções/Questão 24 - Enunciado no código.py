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
