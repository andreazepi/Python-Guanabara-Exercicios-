# Desafio 075
# Desenvolda um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No Final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares. 

# Digite um numero
# outro
# maos um
# o ultimo

# Você digitou os valores()
# O valor 3 apareceu na ___ posição
# Os valores pares digitados froma ___


numeros_lista = []
numero_par = []

print('Digite 4 Números aleatórios...')
print('-' * 30)

for c in range(4):
    
    numeros_pessoa = int(input(f'Digite o {c+1}º Número: '))
    numeros_lista.append(numeros_pessoa)

    if numeros_pessoa % 2 == 0:
        numero_par.append(numeros_pessoa)


numeros_tupla = tuple(numeros_lista)
par = tuple(numero_par)
          
print('-='*15)

if 3 in numeros_tupla:
    print(f'O Valor 3 apareceu na {numeros_tupla.index(3) + 1}º possição da tupla')
else:
    print('O número 3 não foi digitado!')

if 9 in numeros_tupla:
    print(f'O Valor 9 apareceu {numeros_tupla.count(9)} vezes')
else:
    print('O número 9 não foi digitado.')

if len(par) == 0:
    print('Nenhum número par foi digitado!')
else:
    print(f'Os números pares são: {par}')
    

print(f'Você digitou os valores: {numeros_tupla}')





