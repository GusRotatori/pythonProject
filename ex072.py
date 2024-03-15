cont = ('zero' , 'um' , 'dois' , 'tres' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' ,
        'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezesseis' , 'dezessete' ,
        'dezenove' , 'vinte')
while True:
    núm = int(input('Digite um número 0 e 20:  '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente.' , end='')
print(f'Você digitou o número {cont[núm]}')