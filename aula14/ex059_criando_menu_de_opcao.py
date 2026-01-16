# Desafio 059: Criando um Menu de Opções
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números 
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

while calculo != 5:
   
    print(''' Qual calculo voce quer fazer:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    print('-='*25)
    calculo = int(input('Digite a opção desejada: '))
    print('-='*25)

    if calculo == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}')
    elif calculo == 2:
        multiplicacao = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é {multiplicacao}')
    elif calculo == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        else:
            print(f'O maior valor é {valor2}')
    elif calculo == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif calculo == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-='*25)
print('FIM DO PROGRAMA')


# ==============================================================================
# OPÇÃO 2: Lógica alternativa (Inputs dentro das operações)
# ==============================================================================


opcao = 0
while opcao != 4:
    print(''' Digite uma opção: 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1 or opcao == 2 or opcao == 3:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'O resultado de {n1} x {n2} é {multiplicacao}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Fim do programa! Volte sempre...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)


# ==============================================================================
# OPÇÃO 3: Utilizando a biblioteca math
# ==============================================================================

import math

opcao = 0
while opcao != 4:
    print('''    
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1 or opcao == 2 or opcao == 3:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    if opcao == 1:
        soma = math.fsum([n1, n2])
        print(f'A soma entre {n1} + {n2} é {soma:.0f}')
    elif opcao == 2:
        produto = math.prod([n1, n2])
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opcao == 3:
        maior = max(n1, n2)
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Finalizando Opção 3...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
