preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5/100)
print('O preço do produto que custava R${:.2f}, na promoção com desconto de 5 por cento vai custar R${:.2f}' .format(preço, novo))

