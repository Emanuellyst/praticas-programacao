# Conversor de temperatura

print("Olá! Escolha a temperatura que gostaria de converter.")
print("Opção 1: Celsius (°C) para Fahrenheit (°F)")
print("Opção 2: Fahrenheit (°F) para Celsius (°C)")

opcao =input("Escolha a sua opção: ")

if opcao == "1":
    temp_c = float(input("Qual é a temperatura em (°C) atual? ")) # Python aceita apenas ponto (.) como separador decimal

    f = temp_c*1.8+32
    print(f"Está fazendo aproximadamente {f:.1f} °F")

elif opcao == "2":
    temp_f = float(input("Qual é a temperatura em (°F) atual? "))
    c = (temp_f-32)/1.8
    print(f"Está fazendo aproximadamente {c:.1f} °C")

else:
    print("Digite uma opção válida (1 ou 2).")
