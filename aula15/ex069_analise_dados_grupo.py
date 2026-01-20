# Desafio 069: Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

tot18 = homens = mulher20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)

    # PARTE 2: Coleta e Validação de Dados
    idade = int(input('Idade: '))
    sexo = ' '
    # O PORTEIRO: Enquanto o sexo NÃO ESTIVER na lista de permitidos 'MF'...
    while sexo not in 'MF': 
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    # PARTE 3: Análise (Processamento)
    if idade >= 18:                    # Aqui ele faz a soma de todas as pessoas +18
        tot18 += 1
     
    if sexo == 'M':                    # Aqui quantos Homens são
        homens += 1
        
    if sexo == 'F' and idade < 20:     # Aqui quantos Mulheres tem menos de 20 anos
        mulher20 += 1

    # PARTE 4: O Freio (Quer continuar?)
    resp = ' '
    # O PORTEIRO DE NOVO: Só deixa passar se for S ou N
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
