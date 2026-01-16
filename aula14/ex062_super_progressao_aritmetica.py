# Desafio 062: Super Progressão Aritmética v3.0
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

# É praticamente oque eu tinha pensado na opção 1 do ex061. 
# 1º Coloquei tudo dentro do While pra fazer a repitação até a pessoa pedir pra parar
# A minha 2º opção foi fazer sem a repetição, deixando as primeiras variaveis fora do while, pra não ter repetição.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')