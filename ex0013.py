salário = float(input('Qual o salário do funcionário? R$ '))
novo = salário + (salário * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com 15 por cento de aumento, passa a receber R${:.2f}' .format(salário, novo))