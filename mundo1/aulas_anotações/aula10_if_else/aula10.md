### Condições Aula de Python (Part 1) ###

## Estrutura If, Elif e Else

if <condição>:
    # bloco de código executado se a condição for verdadeira
elif <outra_condição>:
    # bloco de código executado se a outra condição for verdadeira
else:
    # bloco de código executado se nenhuma das condições anteriores for verdadeira

# Exemplo de uso:
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")

# Explicação:
# - A estrutura "if" verifica uma condição inicial.
# - Se a condição for verdadeira, o bloco de código indentado após o "if" é executado.
# - A estrutura "elif" permite verificar condições adicionais se a condição anterior for falsa.
# - A estrutura "else" captura todos os casos que não foram cobertos pelas condições anteriores.

# Dica:
# Você pode ter quantos "elif" quiser, mas apenas um "else" no final.

# Prática:
# Tente criar um programa que classifique a idade de uma pessoa em: criança, adolescente, adulto ou idoso.

´´´
idade = int(input('Digite a sua idade: '))
if idade >=18:
    print('Você é um adulto!')
elif idade >=13:
    print('Você é um adolescente!')
else:
    print('Você é uma criança!')
´´´

identação é o espaço em branco no início de uma linha de código, que indica o nível de hierarquia do código dentro de blocos condicionais ou de repetição.


# Exemplo:
tempo = int(input('Quantos anos tem seu carro? ')
if tempo<=3:
    print('carro novo')
else:
    print('caro velho')
print('--Fim--')

# Condição com três linhas:

tempo = int(input('Quantos anos tem seu carro? ')
print('carro novo' if tempo<=3 else'carro velho')
print('--Fim--')

# Outro exemplo:
nesse programa, ele elogia todo mundo que tem o mesmo nome do if. 

nome = str(input('Qual é o seu nome: '))

if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}!')


já nesse próximo, ele da uma mensagem diferente colocando o else.

if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é diferente!')
print(f'Bom dia, {nome}!')

# Exemplo com matemática

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)
print(f'A sua média foi {m:.2f}')
if m >= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('A sua média foi ruim! ESTUDE MAIS!')


### Exercicios

## Desafio 028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

## Desafio 029
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

## Desafio 030
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

## Desafio 031
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

## Desafio 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

## Desafio 033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

## Desafio 034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

## Desafio 035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

