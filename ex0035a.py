# Lê os comprimentos das retas informados pelo usuário
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

# Verifica se as retas formam um triângulo
if a + b > c and a + c > b and b + c > a:
    print("As retas formam um triângulo.")
else:
    print("As retas não formam um triângulo.")
