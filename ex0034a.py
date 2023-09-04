salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
  aumento = salario * 0.1
else:
  aumento = salario * 0.15

novo_salario = salario + aumento

print(f"O novo salário do funcionário é R$ {novo_salario:.2f}, sendo um aumento de R$ {aumento:.2f}.")
