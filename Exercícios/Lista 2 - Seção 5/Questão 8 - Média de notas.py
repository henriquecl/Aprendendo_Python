# Exercício 8 - Ler 2 notas, verifica se as notas são válidas e
# exibir na tela a média. A nota deve ser entre 0 e 10, onde caso
# nao seja válida o fato deve ser informado e prog termina

nota1 = float(input('Digite a nota do seu 1º EE\n'))
nota2 = float(input('Digite a nota do seu 2º EE\n'))

if 10 < nota1 or nota1 < 0:
    print("Você inseriu um valor incorreto")
elif 10 < nota2 or nota2 < 0:
    print("Você inseriu um valor incorreto")
else:
    print(f"A média das suas notas foi: {(nota1+nota2)/2}")
