distância = float(input('Qual é a distância de sua viagem? '))
print('Você está prestes a começar uma viagem de {}KM.' .format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('O preço de sua passagem será de R${:.2f}' .format(preço))