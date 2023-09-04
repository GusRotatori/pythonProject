num = int(input("Digite um número inteiro: "))
base = int(input("Escolha a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal: "))

if base == 1:
    print(f"O número {num} em binário é: {bin(num)[2:]}")
elif base == 2:
    print(f"O número {num} em octal é: {oct(num)[2:]}")
elif base == 3:
    print(f"O número {num} em hexadecimal é: {hex(num)[2:]}")
else:
    print("Opção inválida.")
