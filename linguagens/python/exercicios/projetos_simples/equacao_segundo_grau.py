# Exercício: Equação do 2º grau
# Objetivo: Calcular as raízes de uma equação do segundo grau
# Conteúdos praticados: entrada de dados, operadores e condicionais

import math

a =float(input("Digite um numero: "))
print("A:", a)
b =float(input("Digite um numero: "))
print("B:", b)
c =float(input("Digite um numero: "))
print("C:", c)

delta =float((b**2)-4*a*c)
print("O Delta da equação é:", delta)

if delta<0:
    print("Delta negativo, não existem raízes reais.")
elif delta==0:
    x =-b/(2*a)
    print("Delta zero, existe uma raiz real.")
    print("X:", x)
else:
    x1 =float((-b+math.sqrt(delta))/(2*a))
    x2 =float((-b-math.sqrt(delta))/(2*a))
    print("A resposta da equação do 2º grau é:")
    print("X1:", x1)
    print("X2:", x2)
