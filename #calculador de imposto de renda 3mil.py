#calculador de imposto de renda 3mil

salario = float(input("Digite o valor do salário: "))

# Calcula o imposto de renda
if salario <= 1903.98:
    imposto = 0
elif salario <= 2826.65:
    imposto = (salario * 0.075) - 142.8
elif salario <= 3751.05:
    imposto = (salario * 0.15) - 354.8
elif salario <= 4664.68:
    imposto = (salario * 0.225) - 636.13
else:
    imposto = (salario * 0.275) - 869.36

# Calcula o valor restante após a retirada do imposto
valor_restante = salario - imposto

# Informa o valor restante após o imposto
print(f"O valor restante após o imposto de renda é: R${valor_restante:.2f}")