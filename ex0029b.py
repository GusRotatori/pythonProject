velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado em R${:.2f} por exceder o limite de velocidade.".format(multa))
else:
    print("Você está dentro do limite de velocidade permitido.")