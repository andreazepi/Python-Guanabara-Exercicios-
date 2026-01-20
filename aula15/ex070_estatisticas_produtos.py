# Desafio 070: Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

# PARTE 1: Preparação das Variáveis





total = 0   # total = Soma de todos os preços
tot1000 = 0 # tot1000 = Quantos produtos custam mais de mil
menor = 0 # menor = Guarda o preço do mais barato
cont = 0 # cont = Conta quantos produtos foram cadastrados
barato = ''  # barato = Guarda o NOME do produto mais barato

while True:
    print('-' * 30)
    print('LOJA SUPER BARATÃO')
    print('-' * 30)
    
    # PARTE 2: Coleta de Dados
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    
    # PARTE 3: Análise (Processamento Matemático)
    cont += 1       # Conta que passamos mais um produto
    total += preco  # Acumula o valor no total da compra
    
    # Verifica se custa mais de mil
    if preco > 1000:
        tot1000 += 1
        
    # Lógica do Menor Preço:
    # Se for o 1º produto (cont == 1) OU se o preço atual for menor que o menor que eu já tinha guardado
    if cont == 1 or preco < menor: 
        menor = preco     # Atualiza o menor preço
        barato = produto  # Atualiza o nome do produto mais barato
        
    # PARTE 4: O Freio (O Porteiro da Validação)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        
    if resp == 'N':
        break
        
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')