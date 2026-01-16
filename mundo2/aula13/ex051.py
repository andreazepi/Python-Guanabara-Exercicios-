# Desafio 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: ')) # Razão é pular de casa em casa de acordo com oque voce quer
decimo = primeiro + (10 - 1) * razao   # formula décimo termo
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' → ')
print('ACABOU') 