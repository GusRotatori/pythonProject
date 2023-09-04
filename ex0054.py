from datetime import date


def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade


maiores_idade = 0
menores_idade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Informe o ano de nascimento da pessoa {i}: "))
    idade = calcular_idade(ano_nascimento)

    if idade >= 21:
        maiores_idade += 1
    else:
        menores_idade += 1

print(f"\n{maiores_idade} pessoas são maiores de idade.")
print(f"{menores_idade} pessoas ainda não atingiram a maioridade.")

