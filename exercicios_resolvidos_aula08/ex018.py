# Desafio 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo em graus:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno do ângulo {angulo} é {seno:.2f}')
print(f'O cosseno do ângulo {angulo} é {cosseno:.2f}')
print(f'A tangente do ângulo {angulo} é {tangente:.2f}')