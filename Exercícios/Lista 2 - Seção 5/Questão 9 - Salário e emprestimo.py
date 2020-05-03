# Exercício 9 - Ler o salário e o valor da prestação de um emprestimo
# Se a prestação for maior que 20% do salário: emprestimo nao concedido
# Se nao, empréstimo

salario = float(input('Digite seu salário\n'))
parcela = float(input('Digite a parcela do emprestimo\n'))

if parcela > 0.2*salario:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")

