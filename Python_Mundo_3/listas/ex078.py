# Desafio 078: Maior e Menor valores na Lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    # aqui guarda tudo na lista os valores digitados, depois é só usar as funções max() e min() para descobrir o maior e menor valor, respectivamente, e depois usar um laço de repetição para mostrar as posições onde eles aparecem na lista.

print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')

for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')

for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end='')
print() 
