# Desafio 072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostrá-la por extenso.

# Digite um numero entre 0 e 20:
# Voce digitou o numero vinte
# Número invalido

'''
Docstring para Python_Mundo_3.tuplas.pratica
- criar uma variavel contendo o nome dos numeros de zero a vinte
- Add um input para coletar o numero que o individuo quer entre 0 e 20
- Add uma condição de numero invalido
- Add uma condição de que a pessoa digitou o número certo, e mostrar no cursor o número por extenso
'''

numero_escrito = 'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte'
# tem que ter 21 elementos para que o print de certo

while True:
    numero_digitado = int(input('Digite um número de 0 a 20: ')) 

    if 0 <= numero_digitado <= 20:
        break
    print('Número inválido! Tente novamente...', end=' ')  
print(f'Você digitou o número {numero_escrito[numero_digitado]}')