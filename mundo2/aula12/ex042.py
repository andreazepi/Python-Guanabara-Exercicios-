# Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)       # lembrando, essa é a formula pra calculo de imc

print(f'Seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')  
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

# Vamos praticar com def:

def classificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    match imc:
        case imc if imc < 18.5:
            return 'Abaixo do peso'
        case imc if imc < 25:
            return 'Peso ideal'
        case imc if imc < 30:
            return 'Sobrepeso'
        case imc if imc < 40:
            return 'Obesidade'
        case _:
            return 'Obesidade mórbida'

print(imc(peso, altura))
