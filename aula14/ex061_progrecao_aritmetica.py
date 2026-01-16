# Desafio 061: Progressão Aritmética v2.0
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.



# ==============================================================================
# OPÇÃO 1: Inputs dentro do loop (Permite calcular várias PAs)
# ==============================================================================
print('--- OPÇÃO 1: Inputs dentro do While (Loop Infinito) ---')
while True:
    print('Gerador de PA')
    print('-=' * 10)
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão da PA: '))
    termo = primeiro
    cont = 1
    while cont <= 10:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('FIM')
    print('-=' * 10)
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
    print('-=' * 10)
print('-=' * 10)
print('Fim do Programa')

# ==============================================================================
# OPÇÃO 2: Resolução Padrão (Inputs fora - Executa uma vez)
# ==============================================================================

print('\n--- OPÇÃO 2: Resolução Padrão ---')
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')
