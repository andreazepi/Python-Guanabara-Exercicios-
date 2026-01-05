# Desafio 15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dias e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

total_dias = dias * 60
km_total = km * 0.15
geral = total_dias + km_total

print(f'O total a pagar é de R${geral:.0f}')

'''
Solução do Guanabara

pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')
'''