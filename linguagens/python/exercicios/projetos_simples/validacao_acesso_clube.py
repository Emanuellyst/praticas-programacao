"""
Teste de validação para entrada em clube.
Valida nome (somente letras e espaços).
Verifica idade mínima de 21 anos.
"""

from datetime import datetime

ano_atual = datetime.now().year

while True:
    nome = input("Digite seu nome: ").strip() 
    if nome == "":
        print("O nome não pode estar vazio.")
        continue

    valido = True

    for caractere in nome:
        if not caractere.isalpha() and caractere != " ":
            valido = False
            break

    if valido:
        break
    else:
        print("Digite apenas letras.")

while True:
    try:
        ano_nascimento =int(input("Em que ano você nasceu? "))
        if 1900 <= ano_nascimento <= ano_atual:
            idade = ano_atual - ano_nascimento
            break

        else:
            print(f"Ano inválido. Digite um ano entre 1900 e {ano_atual}")
    except ValueError:
        print("Digite apenas números inteiros")

print(f"\nVocê tem {idade} anos")

if idade >= 21:
    print(f"Seja bem-vindo(a) ao nosso clube, {nome}!")
else:
    print(f"Desculpe {nome}, você não tem idade suficiente para entrar.\nvolte daqui {21-idade} anos.")
