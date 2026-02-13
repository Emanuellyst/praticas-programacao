# Cálculo básico de empréstimo com juros de 20%

while True:
    try:
        valor_emprestimo = float(input("Informe o valor desejado para o empréstimo (R$): "))
        if valor_emprestimo>0:
            break
        print("valor inválido. o valor deve ser maior que 0.")
    except ValueError:
        print("Entrada inválida. Digite um número válido")

while True:
    try:
        parcela =int(input("Em quantas parcelas deseja pagar? (1 a 12): "))
        if 1 <= parcela <= 12:
            break
        print("Quantidade inválida. O número de parcelas deve estar entre 1 e 12.")
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")


juros = 0.20 # 20% de juros
juros_emprestimo = valor_emprestimo*juros
subtotal = valor_emprestimo+juros_emprestimo
total = subtotal/parcela


print(f"\nResumo do empréstimo:")
print(f"O valor total com juros será: R$ {subtotal:.2f}")
print(f"O valor de cada parcela será: R$ {total:.2f}")
