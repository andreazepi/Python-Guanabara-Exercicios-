# Desafio 073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados. 
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense

# Lista de times do brasileiro: (______)
# d (A Chapecoense está na 8º posição) exemplo

'''
Docstring para Python_Mundo_3.tuplas.ex073

Fora do loop:
- Criar uma várivel com o nome dos times por extenso
Dentro do loop: 
                Qual loop usar? For ou While?
- Um print com essas informações:
    A) Apenas os 5 primeiros colocados. 
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time da Chapecoense
- Criar uma variavel de input, para coletar a opção que a pessoa colocou,
- Criar uma variavel de opção invalida, caso não digite nenhuma das opções que definimos.
- Criar variaveis de if para interligar as opções de A a D de acordo com oq é pedido.
- 
'''

tabela_campeonato_brasileiro = ('Palmeiras', 'São Paulo', 'Corinthias', 'Bahia', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol', 'Flamengo', 'Coritiba', 'Santos', 'Botafogo', 'EC Vitória', 'Remo', 'Atlético-MG', 'Internacional', 'Cruzeiro', 'Vasco da Gama')

print('-' * 30)
print('Lista Campeonato Brasileiro')
print('-' * 30)
print('\n'.join(tabela_campeonato_brasileiro)) 
print('-' * 30)
print(' ')
print('Escolha uma Opção:') 
print(' ')
print('''
        A) Mostre apenas os 5 primeiros colocados. 
        B) Os últimos 4 colocados da tabela.
        C) Uma lista com os times em ordem alfabética.
        D) Em que posição na tabela está o time da Chapecoense')
          ''')

while True:
    escolha = input('Escolha uma opção de A a D ou S para sair: ').upper()
    print(' ')

    if escolha == 'S':
        print('Saindo do Programa...')
        break
    
    elif escolha == 'A':
        resultado = tabela_campeonato_brasileiro[0:5]
        print('\n'.join(resultado))     #'\n'.join utiliza pra printar em uma lista, uma abaixo da outra
        print('-' * 30)
        print(' ')

    elif escolha == 'B':
        resultado = tabela_campeonato_brasileiro[-4:]
        print('\n'.join(resultado))
        print('-' * 30)
        print(' ')

    elif escolha == 'C':
        resultado = sorted(tabela_campeonato_brasileiro)
        print('\n'.join(resultado))
        print('-' * 30)
        print(' ')

    elif escolha == 'D':
       
        print(f'O time da Chapecoense esta na {tabela_campeonato_brasileiro.index('Chapecoense')}º posição')

    else:
        print('Opção invalida! Tente novamente.')
        print('-' * 30)
        print(' ')

print('Programa Encerrado!')


    

