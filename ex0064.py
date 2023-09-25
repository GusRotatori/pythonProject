num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    soma += num
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.' .format(cont, soma - 999))
