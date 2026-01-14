# ## Desafio 023
# - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1


num = int(input('Digite um numero de 0 a 9999: '))
n = str(num).zfill(4) # Preenche com zeros à esquerda até ter 4 dígitos (ex: 35 vira "0035")
# .zfill(4) garante que sempre teremos 4 caracteres
print(f'Analisando o numero {num}')
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')

# Solução Guanabara
# num = int(input('Digite um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'Analisando o número {num}')
# print(f'Unidade: {u}')
# print(f'Dezena: {d}')
# print(f'Centena: {c}')
# print(f'Milhar: {m}')

# Outra solução Guanabara
# num = input('Digite um número: ')
# print(f'Analisando o número {num}')
# print(f'Unidade: {num[-1]}')
# print(f'Dezena: {num[-2]}')
# print(f'Centena: {num[-3]}')
# print(f'Milhar: {num[-4]}')


