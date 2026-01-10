# Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
print("-"*50)  # utilizei apenas para decorar a saída do programa
print("Vamos brincar de adivinhação de número de 0 a 5")
print("-"*50)
n = randint(0, 5) # Faz o computador "PENSAR" num número aleatório antes do usuário tentar adivinhar
numero = int(input('Digite um número: '))
if numero == n:
    print('Você acertou!')
else:
    print(f'Você errou! O número escolhido foi {n}.')

# modulo random - randint() é usado para gerar números inteiros aleatórios dentro de um intervalo especificado. Sempre pesquise para saber qual módulo usar em cada situação.

