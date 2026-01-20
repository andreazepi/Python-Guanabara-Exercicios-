# Aula 15 — Interrompendo Repetições `while`

## 1. Laços de Repetição (Parte 3)
Nesta aula, aprendemos como interromper um laço de repetição `while` utilizando o comando `break`.

O `break` é utilizado para sair de um loop de forma forçada, interrompendo a execução do bloco de repetição e passando para o próximo comando fora do laço. É muito comum utilizá-lo em loops infinitos (`while True`).

### Pseudocódigo (Analogia)
Imagine que o personagem deve andar infinitamente, mas se encontrar um troféu, ele deve parar.

```python
while True:
    if chao:
        passo()
    if buraco:
        pula()
    if moeda:
        pega()
    if trofeu:
        pula()
        break  # Aqui ele sai do loop e vai para o comando 'pega' fora do laço
pega()
```

## 2. Prática

### Exemplo 1: Loop Finito (Padrão)
Enquanto a condição for verdadeira (menor ou igual a 10), ele roda o bloco.
```python
cont = 1
while cont <= 10:
    print(f'{cont} -> ', end='')
    cont += 1
print('Acabou')
```

### Exemplo 2: Loop Infinito (`while True`)
Se usarmos `True` na condição, o laço rodará para sempre, a menos que usemos um `break` para interrompê-lo.
```python
cont = 1
while True:
    print(f'{cont} -> ', end='')
    cont += 1
    if cont > 10:
        break # Interrompe o loop quando cont for maior que 10
print('Acabou')
```

## 3. Desafios

### Desafio 066: Vários números com flag
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

### Desafio 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

### Desafio 068: Jogo Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

### Desafio 069: Análise de dados do grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

### Desafio 070: Estatísticas em produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

### Desafio 071: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

    
