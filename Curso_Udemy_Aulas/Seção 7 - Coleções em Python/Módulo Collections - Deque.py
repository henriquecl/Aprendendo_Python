"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performace.


"""

# Importando

from collections import deque

deq = deque('Geek')

print(deq)

# Adicionando elementos no deque

deq.append('y')
print(deq)
deq.appendleft('k')  # Adiciona e retorna no começo da lista, já na lista não é possivel
print(deq)

# Remover elementos

print(deq.pop())
print(deq.popleft())  # Remove e retorna começo da lista, já na lista não é possivel
print(deq)
