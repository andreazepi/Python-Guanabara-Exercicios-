### Condições Aninhadas
if carro.esquerda():
    bloco1
elif carro.direita():
    bloco2
elif carro.ré():
    bloco3
else:
    bloco4

## essa é uma condição simples:

nome = str(input('Qual é seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
print(f'Tenha um bom dia {nome}')

## essa é uma condição composta:

nome = str(input('Qual é seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
else: 
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')

## vamos dar uma aprimorada: (Pode usar várias elif que quiser, e o else é opcional)
# E essa é uma extrutura de formação aninhada, porque esta bem formatada
nome = str(input('Qual é seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Marcia' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else: 
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')

### Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

### Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

### Desafio 038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

### Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

### Desafio 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

### Desafio 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

### Desafio 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

### Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

### Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

### Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você. 