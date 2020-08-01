'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

print("Digite seu salário atual:")
salario_atual = float(input())

if salario_atual <= 280:
    aumento = salario_atual*20/100
    novo_salario = salario_atual + aumento
    porcentagem = 20

elif 280 < salario_atual and salario_atual <= 700:
    aumento = salario_atual*15/100
    novo_salario = salario_atual + aumento
    porcentagem = 15

elif 700 < salario_atual and salario_atual <= 1500:
    aumento = salario_atual*10/100
    novo_salario = salario_atual + aumento
    porcentagem = 10

elif salario_atual >= 1500:
    aumento = salario_atual*5/100
    novo_salario = salario_atual + aumento
    porcentagem = 5

print("Salário antes do reajuste: R$", salario_atual)
print("Percentual de aumento aplicado:", porcentagem, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário, após o aumento: R$", novo_salario)







