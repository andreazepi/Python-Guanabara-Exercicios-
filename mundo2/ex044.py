# Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(f'{(" LOJAS GUANABARA "):=^40}')
preco = float(input('Digite o preço do produto: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco / 2
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 0.20)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS')
else:
    total = preco
    print('Opção inválida. Tente novamente.')
print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
