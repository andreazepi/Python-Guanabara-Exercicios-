# Desafio 065: Maior e Menor valores
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# ==============================================================================
# OPÇÃO 1: Utilizando BREAK (Lógica "SAIR")
# ==============================================================================
soma = cont = maior = menor = 0
print('Digite números inteiros para calcular. Digite "SAIR" para encerrar.')

while True:
    entrada = input('Digite um número: ').strip().upper()
    
    if entrada == 'SAIR':
        break
    
    numero = int(entrada)
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

if cont > 0:
    media = soma / cont
    print(f'Você digitou {cont} números e a média foi {media}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
else:
    print('Nenhum número foi digitado.')
# print('FIM')

# ==============================================================================
# OPÇÃO 2: Sem BREAK (Lógica Padrão com Flag "Quer continuar?")
# ==============================================================================
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')