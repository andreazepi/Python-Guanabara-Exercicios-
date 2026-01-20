# Desafio 060: Cálculo do Fatorial!                                                             
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120 
# faca com whie e for 


# ==============================================================================
# OPÇÃO 1: Solução com Módulo (math)
# ==============================================================================
print('\n--- OPÇÃO 1: Usando Módulo math ---')
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')

# ==============================================================================
# OPÇÃO 2: Solução com While
# ==============================================================================
print('\n--- OPÇÃO 2: Usando While ---')
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

# ==============================================================================
# OPÇÃO 3: Solução com For
# ==============================================================================
print('\n--- OPÇÃO 3: Usando For ---')
n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)