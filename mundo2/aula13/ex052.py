# Desafio 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

# Desafio 052 - Números Primos
# Lê o número que queremos testar
num = int(input('Digite um número: '))

tot = 0 # Variável para contar quantos divisores o número tem

# Laço de 1 até o próprio número
for c in range(1, num + 1):
    # Se o resto da divisão for 0, é divisível
    if num % c == 0:
        print('\033[33m', end='') # Pinta de Amarelo
        tot += 1 # Conta +1 divisor
    else:
        print('\033[31m', end='') # Pinta de Vermelho
    
    print(f'{c}', end=' ') # Mostra o número testado

# Mostra o resultado final
print(f'\n\033[mO número {num} foi divisível {tot} vezes')

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
