numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Inicializa as variáveis de maior e menor com o primeiro número
maior = numero1
menor = numero1

# Verifica se o segundo número é maior ou menor que as variáveis
if numero2 > maior:
    maior = numero2
if numero2 < menor:
    menor = numero2

# Verifica se o terceiro número é maior ou menor que as variáveis
if numero3 > maior:
    maior = numero3
if numero3 < menor:
    menor = numero3

print("O maior número é", maior)
print("O menor número é", menor)
