# Desafio 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

numero = int(input('Digite um número: '))
if numero % 2 == 1:   # outra opção é colocar: % 2 != 0
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')


# lembrando:
# o da divisão de qualquer número par é 0, e o resto da divisão de qualque número impar é 1, e é calculado como (numero % 2).