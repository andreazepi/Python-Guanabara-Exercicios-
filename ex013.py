# Desafio 13
# Faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário: '))
aumento = salario * 0.15            # 15%
novo_salario = salario + aumento
                
print(f'Você recerá um aumento de 15% que equivale a R$ {aumento} a mais no seu salário,\n e o seu novo salário será de R$ {novo_salario:.2f}.')

'''
Solução do Guanabara:

salario = float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}')
'''