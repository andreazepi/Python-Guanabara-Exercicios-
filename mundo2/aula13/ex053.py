# Desafio 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os acentos e espaços.
# Oque é um palindromo? pesquisar.

# Palíndromo é um...

frase = input('Digite uma frase: ').strip().upper() # lembrando: .strip(ajeita a frase).upper(tudo M)
for frase in frase.split():                         # .split é...
    junto = ''.join(frase)                         # .join é...
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')