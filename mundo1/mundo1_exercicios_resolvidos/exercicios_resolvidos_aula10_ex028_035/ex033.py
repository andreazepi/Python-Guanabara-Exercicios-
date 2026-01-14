# Desafio 033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a:
    menor = b
if c < menor:
    menor = c

# Verificando quem é o maior
maior = a
if b > a:
    maior = b
if c > maior:
    maior = c

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')


# Há um exemplo mais otimizado no arquivo 'exemplo_real_frete.py' usando dicionários e ordenação.
