"""
Try / Except / Else / Finally

Dica de quando e onde tratar o código:
TODA ENTRADA DEVE SER TRATADA!!!
OBS: A função do usuário é DESTRUIR seu sistema.

Else -> É executado somente se NÃO ocorrer o erro.

# Exemplo 1
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um número')
else:
    print(f'Você digitou: {num}')


# Finally -> O bloco finally é SEMPRE executado, independente se houve exceção ou não.
# Geralmente é utilizado para fechar ou desalocar recursos.

try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Você não digitou um número')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# Exemplo mais complexo ERRADO
def dividir(a, b):
    return a/b
try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    print(dividir(num1, num2))
except ValueError:
    print('O valor precisa ser númerico')




# Exemplo mais complexo CERTO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!!!!


def dividir(a, b):
    try:
        return int(a)/int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possivel dividir por 0'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))
"""
# Exemplo mais complexo - Tratamento Semi-Genérico


def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorrou o problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')
print(dividir(num1, num2))