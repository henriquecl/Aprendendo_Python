# Exercício 14 - Ponderar notas e dizer se passou ou nao
import sys
trab_lab = float(input('Digite a sua nota do trab de lab\n'))
if 10 < trab_lab or trab_lab < 0:
    print("Você inseriu a nota errada.")
    sys.exit()
av_semestral = float(input('Digite a sua nota da av semestral\n'))
if 10 < av_semestral or av_semestral < 0:
    print("Você inseriu a nota errada.")
    sys.exit()
ex_final = float(input('Digite a sua nota do ex final\n'))
if 10 < ex_final or ex_final < 0:
    print("Você inseriu a nota errada.")
    sys.exit()
media = ((trab_lab*2 + av_semestral*3 + ex_final*5)/10)

if 0 < media < 2.999:
    print(f"Você foi reprovado pois sua média foi: {media}")

elif 3 <= media < 4.999:
    print(f"Você está de recuperaçao pois sua média foi: {media}")
else:
    print(f"Você foi aprovado pois sua média foi: {media}")
