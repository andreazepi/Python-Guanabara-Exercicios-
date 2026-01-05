# Desafio 12
# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o valor deste produto: R$ '))
desconto = produto * 0.05
final = produto - desconto

print(f'Você ganhara um desconto de R$-{desconto} e terá um produto com valor final de R$ {final}.')

'''
Solução do Guanabara:

preço = float(input('Qual o valor do produto: R$ '))
novo = (preço * 5 / 100)
print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}')
'''
