# Desafio 074
# Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla;.
# min()
# max()


# Os valores sorteados foram: 
# O maior valor sorteado foi 
# E o menor valor foi  

from random import sample              # escolhe um elemento único de uma sequencia
numeros = tuple(sample(range(10), 5))

print(f'Os valores sorteados forma: {sorted(numeros)}')
print(f'O maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')

    