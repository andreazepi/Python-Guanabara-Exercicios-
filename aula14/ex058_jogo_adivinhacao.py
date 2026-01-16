# Desafio 058: Jogo da Adivinhação v2.0
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


print("-="*25)  
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
print("-="*25)


from random import randint
n = randint(0, 10)
palpites_total = 0

while True:
    numero = int(input('Digite um número: '))
    palpites_total += 1  # Conta a tentativa atual
    if numero == n:
        print(f'Acertou com {palpites_total} tentativas. Parabéns!')
        break
    else:
        if numero < n:
            print('Mais... Tente mais alto.')
        else:
            print('Menos... Tente mais baixo.')
