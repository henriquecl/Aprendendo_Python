"""
Any e All

All() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
Any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se tiver vazio, retorna False
# Ex 1 - All
print(all([0, 1, 2, 3, 4]))     # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))     # Todos os números são verdadeiros? True
print(all([]))  # O iterável está vazio? True

# Ex 2 - All, utilização legal
nomes = ['Carlos', 'Camile', 'Carla', 'Cassiano', 'Cristina']
print(all(nome[0] == 'C' for nome in nomes))

# OBS: Um iterável vazio convertido em boolean é false, mas convertido no all é true
print(all([letra for letra in 'eiof' if letra in 'qpk']))

# Ex 3 - print(all(numero for numero in [4, 2, 10, 6, 8] if numero % 2 == 1))
"""
print(any([0, 1, 2, 3, 4, 5]))
print(any([0, False, (), {}, []]))
print(any([0, 1, False, (), {}, []]))
nomes = ['Carlos', 'Camile', 'Carla', 'Cassiano', 'Cristina', 'João']
print(any([nome[0] == 'C' for nome in nomes]))
print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))


