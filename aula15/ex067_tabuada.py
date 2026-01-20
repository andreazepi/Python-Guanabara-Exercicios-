# Desafio 067: Tabuada v3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')