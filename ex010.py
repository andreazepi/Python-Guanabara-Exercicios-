# Desafio 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

carteira = float(input('Quanto dinheiro você tem no total? R$ '))
r = 3.27 # (1 dolar em real equivale a 3.27)
total = carteira / r
# dolar = carteira / 3.27 (esse é o valor do dolar)

print(f'Com R$ {carteira} você pode comprar US$ {total:.2f}c.')
