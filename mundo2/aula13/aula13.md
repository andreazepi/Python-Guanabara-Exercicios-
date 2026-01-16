# Aula 13 — Estrutura de Repetição `for`

Nesta aula, aprendemos sobre estruturas de repetição (laços ou loops), especificamente o laço com variável de controle: o **`for`**.

## 1. O que é uma Estrutura de Repetição?
É um recurso que permite executar um bloco de comandos várias vezes, sem precisar reescrever o código. É ideal quando sabemos previamente quantas vezes o comando deve ser repetido ou quando queremos iterar sobre um intervalo.

### Analogia do "Passo" e "Pula"
Imagine um personagem que precisa andar e pular repetidamente. Em vez de escrever os comandos várias vezes, usamos um laço.

**Em Português (Pseudocódigo):**
```text
laço c no intervalo(0, 3)
    passo
    pula
pega
```

**Em Python:**
```python
for c in range(0, 3):
    passo()
    pula()
pega()
```

## 2. A Função `range()`
A função `range()` define o intervalo da contagem (iteração).

- **`range(1, 6)`**: Conta de 1 até 5 (o último número é ignorado).
- **`range(0, 5)`**: Conta de 0 até 4 (total de 5 iterações).
- **`range(0, 10, 2)`**: Conta de 0 até 9, pulando de 2 em 2.
- **`range(10, 0, -1)`**: Conta de trás para frente.

## 3. Exemplos Práticos

### Exemplo 1: Repetição Simples
```python
# Imprime "Oi" 5 vezes
for c in range(0, 5):
    print('Oi')
print('Fim')
```

### Exemplo 2: Usando a Variável de Controle
A variável `c` (ou qualquer outro nome) assume o valor de cada iteração.
```python
# Conta de 1 até 5
for c in range(1, 6):
    print(c)
print('Fim')
```

### Exemplo 3: Lógica Condicional dentro do Laço
Podemos usar `if` dentro do `for` para executar ações apenas em certas iterações.

**Pseudocódigo:**
```text
laço c no intervalo(0, 3)
    se moeda
        pega
    passo
    pula
passo
pega
```

**Python:**
```python
for c in range(0, 3):
    if moeda:
        pega()
    passo()
    pula()
passo()
pega()
```

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')


for c in range(0, 3):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')
print('Fim')

### Exercícios

### Desafio 046
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

### Desafio 047
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

### Desafio 048
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

### Desafio 049
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço `for`.

### Desafio 050
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

### Desafio 051
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

### Desafio 052
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

### Desafio 053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os acentos e espaços.
Oque é um palindromo? pesquisar.

### Desafio 054
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

### Desafio 055
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

### Desafio 056
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: 
a média de idade do grupo, 
qual é o nome do homem mais velho 
e quantas mulheres têm menos de 20 anos.



