# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# listagem = 'Pão', 1, 'Leite', 2


# e no final a lista de preços

# ('-'*20)
# Listagem de preços
# ('-'*20)

# Pão......R$ 1.75
# Leite....R$ 2



listagem = ('Lápis', 1.75, 
            'Borracha', 2.00, 
            'Caderno', 15.00, 
            'Estojo', 25.00, 
            'Transferidor', 4.00, 
            'Compasso', 9.99, 
            'Mochila', 120.32, 
            'Canetas', 22.30, 
            'Livro', 34.90)

print('-='*20)
print(f'{"Listagem de preços":^40}')
print('-='*20)

for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f'R${listagem[c]:>7.2f}')

print('-='*20)

