## Desafio 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hi = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é {hi:.2f}')

# se eu quiser usar so o modulo math, posso fazer assim:
# from math import hypot
# co = float(input('Digite o comprimento do cateto oposto:'))
# ca = float(input('Digite o comprimento do cateto adjacente:'))
# hi = hypot(co, ca) aqui já tiramos a necessidade de usar o math.hypot
# print(f'O comprimento da hipotenusa é {hi:.2f}')

# Outra forma de calcular a hipotenusa sem usar a função hypot:
# hi = math.sqrt(co**2 + ca**2)     
# print(f'O comprimento da hipotenusa é {hi:.2f}')

# Outra maneira de fazer sem utilizar o modulo math, é a conta tradicional:
# hi = (co**2 + ca**2) ** (1/2)
# print(f'O comprimento da hipotenusa é {hi:.2f}')