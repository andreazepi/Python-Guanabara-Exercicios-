### Tuplas
## Variáveis compostas

lanche (variavel), quando é declarada vira um espaço na memoria

        recebe alguma coisa 
lanche = 

variavel simples, é colocar tipo colocar uma coisa só no resultado da varivael
lanche = sandwiche    -- essas é a simples

Há 3 possibilidades sobre como fazer essa varivel compostas:
- Tuplas
- Listas
- Dicionários

Uma variavel que guarda vários valores é uma tupla, tipo
lanche = Sandwuich, Suco, Pudim, Pizza

e como podemos acessar os elementos dessa tupla?
é a indicação por indices:
0 1 2 3 - essa sequencia de numeros simboliza a variavel que esta dentro da tupla

print(lanche) - ele vai printar todos os lanches
print(lanche[2]) - ai ele vai printar o pudim
print(lanche[0:2]) - vai ate o 1, lembre-se, o ultimo numero é ignorado
print(lanche[1:]) - vai do suco ate p final
print(lanhe[-1]) - pega o último elemento

len(lanche) vai contar quantos elementos tem, no caso do lanche, tem 4 itens


como não tem a variavel c, ele vai pegar o primeiro item da tupla, e no loop, ele vai passando pelos itens até chegar no final e sair do loop.
for c in lanche:
    print(c)

"As tuplas são imutaveis" - não da para fazer mudança dentro da tupla, não tem como trocar o pudim por um sorvete dentro do programa enquanto ele estiver execultando.

 lanche = 'Hamburgues', 'Suco', 'Pizza', 'Pudim'

 as tuplas não precisa mais de parenteses

 lanche = 'Hamburgues', 'Suco', 'Pizza', 'Pudim'

for comida in lanche:
    print(f'Eu vou comer {comida}')


for cont in range(0, len(lanche)):
    print(f'Eu vou vomer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi muito!')

Ás tres maneiras diferentes de fazer a mesma coisa.


print(sorted(lanche))  aqui ele ordena a tupla em ordem alfabetica.

a = 2, 5, 4
b = 5, 7, 1, 2
c = b + a
print(c) aqui ele vai juntar as duas tuplas A e B

print(c.count(5))  ou seja, quantas vezes o numero 5 ta aparecendo no C
print(c.index(8)) vai falar em que posição está o numero pedido

outra ideia:

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

del(pessoa) apaga a tupla toda, mas nao pode alterar e 
del(pessoa[0]) nem tirar um intem da tupla por ser imutavel


### DESAFIOS 

## Desafio 072
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostrá-la por extenso.

Digite um numero entre 0 e 20:
Voce digitou o numero vinte
Número invalido

## Desafio 073
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados. 
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense

Lista de times do brasileiro: (______)
d (A Chapecoense está na 8º posição) exemplo

## Desafio 074
Crie um programa que vai gerar cinco número aleatórios e colocaremuma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla;.
min()
max()


Os valores sorteados foram: 
O maior valor sorteado foi 
E o menor valor foi

## Desafio 075
Desenvolda um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No Final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. 

Digite um numero
outro
maos um
o ultimo

Você digitou os valores()
O valor 3 apareceu na ___ posição
Os valores pares digitados froma ___


## Desafio 076

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# listagem = 'Pão', 1, 'Leite', 2


# e no final a lista de preços

# (-*20)
# Listagem de preços
# (-*20)

# Pão......R$ 1.75
# Leite....R$ 2




(-*20)

## Desafio 077
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar para cada palavra quais sãoi as suas vogais.

Na palavra ______ temos a e e
.....






