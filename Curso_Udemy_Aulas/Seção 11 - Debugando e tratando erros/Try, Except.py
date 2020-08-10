"""
O bloco try/except

Utilizamos esse bloco para tratar erros que podem ocorrer no nosso código. Previnindo assim, que o programa pare de fun-
cionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas

# Exemplo 1 - Tratando um erro genérico
try:
    geek()
except:
    print('Deu alguma merda')

# Tente executar a função geek(), caso você encontre algum erro, vá para o bloco except
# Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma especifica

# Exemplo 2 - Tratando um erro especifico
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 3 - Tratando um erro que não existe, o erro irá ocorrer igual
try:
    len(5)
except NameError:
    print('Você está utilizando uma função inexistente.')

# Exemplo 4 - Tratando um erro específico com os detalhes do erro
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez
try:
    print('Geek'[9])
    geek()
    len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, 9))



