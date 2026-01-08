
#Desafio 005 Antecessor e Sucessor
#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
#Aula 7 do guanabara que fala sore isso



n = int(input('Digite um número: '))
#a = n - 1
#s = n + 1

#print(f'Analisando o valor {n}, \n o seu antecessor é o {a}, \n e o seu sucessor é o {s}')
print(f'Analisando o valor {n}, o seu antecessor é o {n - 1}, e o seu sucessor é o {n + 1}')

'''
outra maneira é só colocar a primeira variavel, e depois,
cololocar a subtração e soma com 1 dentro do print, no caso,
ficaria asim:
print(f'Analisando o valor {n}, o seu antecessor é o {n - 1}, e o seu sucessor é o {n + 1}')
'''


