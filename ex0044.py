print('{:=^40}'.format('Lojas Guanabara'))
preço = float(input('Preço das compras: R$'))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2 x no cartão
[ 4 ] 3 x no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros' .format(totparc, parcela))
else:
    total = 0
    print('Opção invalida de pagamento, tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preço, total))
