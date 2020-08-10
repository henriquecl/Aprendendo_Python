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
