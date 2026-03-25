# Desafio 081: Extraindo dados de uma Lista
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Você digitou os valores {lista}')

if 5 in lista:
    print(f'O valor 5 foi adicionado e esta na posição {lista.index(5)}')
else:
    print('Nenhum valor com número 5 foi encontrado!!')
print('-=' * 30)




