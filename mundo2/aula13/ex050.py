# Desafio 050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for numero_par in range(1, 7):
    numero_par = int(input(f'Digite o {numero_par}º número: '))
    if numero_par % 2 == 0:
        soma += numero_par
        cont += 1
print(f'Você informou {cont} números pares e a soma foi {soma}')