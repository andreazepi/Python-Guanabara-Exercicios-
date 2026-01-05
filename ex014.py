# Desafio 14 - Conversor de Temperatura
# Escreva um programa que converta uma temperatura digitada em ºC e concerta para ºF

c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32 # Formula da equação de conversão de Celsios para Farenaght
print(f'A temperatura de {c}ºC corresponde a {f}ºF!')

