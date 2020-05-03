# Exercício 3 - Leia um numero real. Se for >0 imprima a raiz, se nao eleve ao quadrado

numero = float(input("Digite um valor\n"))

if numero >= 0:
    print(f"A raiz desse numero é {numero**(1/2)}")
else:
    print(f"O valor desse número ao quadrado é {numero**2}")