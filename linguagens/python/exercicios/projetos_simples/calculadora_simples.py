# Exercício: Calculadora simples
# Objetivo: Realizar operações matemáticas básicas
# Conteúdos praticados: operadores e condicionais

N1 =float(input("Digite o primeiro número: "))
N2 =float(input("Digite o segundo número: "))
# Só utilizar números inteiros ou "."

print("Operações")
print("1: Adição")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")

operação =input("Escolha a operação: ")

if operação =="1":
    print("O resultado é:", N1+N2)
elif operação =="2":
    print("O resultado é:", N1-N2)
elif operação =="3":
    print("O resultado é:", N1*N2)
elif operação =="4":
    if N2 !=0:
        print("O resultado é:", N1/N2)
    else:
        print("Erro: o número 0 não pode ser dividido")
else:
    print("Operação inválida")
