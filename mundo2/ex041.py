# Desafio 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER') 

# Outra maneira é fazer pela extrutura match:

def categoria(idade):
    match idade:
        case idade if idade <= 9:
            return 'MIRIM'
        case idade if idade <= 14:
            return 'INFANTIL'
        case idade if idade <= 19:
            return 'JÚNIOR' 
        case idade if idade <= 25:
            return 'SÊNIOR'
        case _:
            return 'MASTER'

print(categoria(idade))

