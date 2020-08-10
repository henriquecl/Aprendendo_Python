# Questão 19 - Leia número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos
# que compõem o número

numero = int(input('Digite um número entre 100 e 999\n'))
unidade = 0
dezena = 0
centena = 0


while numero > 999 or numero < 100:
    numero = int(input('Digite um número entre 100 e 999\n'))

centena = (numero // 100)
dezena = ((numero//10) % 10)
unidade = (numero % 10)

print(f'A centena foi:{centena} \nA dezena foi:{dezena} \nA unidade foi:{unidade}')
