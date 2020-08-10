"""
Geradores (Generators)

- Generators são Iterators;
OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.
- Podem ser criados com funções geradores;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com expressões geradoras;

Diferenças entre funções e generator functions (Funções Geradoras)
------------------------------------------------------------------------------------------
| Funções                                       | Generator Functions                    |
------------------------------------------------------------------------------------------
Utilizam return                                 | Utilizam yield                         |
Retorna uma vez                                 | Pode utilizar yield múltiplas vezes    |
Quando executada retorna um valor (ou nenhum)   | Quando executada retorna um generator  |



# Exemplo Generator Function (Função Geradora)
# OBS: Uma generator function não é um generator, ela gera um generator.
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
gen = conta_ate(10)

for num in gen:
    print(num)

