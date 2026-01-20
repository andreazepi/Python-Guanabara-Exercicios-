# Desafio 068: Jogo Par ou Ímpar
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    
    # Validação
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    
    print('-' * 30)

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break # Interrompe o loop
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break # Interrompe o loop
            
    print('Vamos jogar novamente...')
    print('=-' * 15)

print(f'GAME OVER! Você venceu {vitorias} vezes.')
                
