# Aula 14 — Estrutura de Repetição `while`

## 1. O que é o `while`?
O `while` (enquanto) é uma estrutura de repetição utilizada quando **não sabemos previamente o limite de repetições** ou quando a repetição depende de uma condição lógica ser verdadeira.

Diferente do `for`, que é ideal quando sabemos o número exato de iterações (ex: contar de 1 a 10), o `while` continua executando *enquanto* a condição for verdadeira.

### Analogia (Pseudocódigo vs Python)
Imagine um personagem que precisa andar até pegar uma maçã. Ele não sabe quantos passos faltam, apenas sabe que deve continuar andando *enquanto* não tiver a maçã.

**Pseudocódigo:**
```text
enquanto não pegar_maçã:
    se tiver chão:
        passo
    se tiver buraco:
        pula
    se tiver moeda:
        pega
pega_maçã
```

**Python:**
```python
while not maca:
    if chao:
        passo()
    elif buraco:
        pula()
    elif moeda:
        pega()
pega()
```

---

## 2. Comparando `for` e `while`

### Quando usar qual?
- **`for`**: Quando você sabe o limite (ex: repetir 10 vezes).
- **`while`**: Quando você não sabe o limite (ex: repetir até o usuário digitar 0).

### Exemplo Prático 1: Limite Conhecido
Ambos podem fazer a mesma coisa, mas a sintaxe muda.

**Usando `for`:**
```python
for c in range(1, 10):
    print(c)
print('FIM')
```

**Usando `while`:**
```python
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
```

---

## 3. Demonstração de Exercícios

### Exemplo 1: Limite Desconhecido (Flag)
O programa continua rodando até que uma condição de parada (flag) aconteça. Neste caso, digitar o número `0`.

```python
n = 1 # Inicializamos com um valor diferente de 0 para entrar no loop
while n != 0:
    n = int(input('Digite um valor [0 para parar]: '))
print('FIM')
```

### Exemplo 2: Contando Pares e Ímpares
O programa lê números indefinidamente até que o usuário digite `0`. Ao final, mostra quantos eram pares e quantos eram ímpares.

```python
n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    
    if n != 0: # Para não contar o 0 como par na estatística final
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Você digitou {par} números pares e {impar} números ímpares!')
```

### Exemplo 3: Validação de Dados
Forçar o usuário a digitar uma opção correta (ex: 'S' ou 'N').

```python
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] # o zero é para pegar a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
```

### Desafio 057: Validação de Dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

### Desafio 058: Jogo da Adivinhação v2.0
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

### Desafio 059: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

### Desafio 060: Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120 
faca com whie e for 

### Desafio 061: Progressão Aritmética v2.0
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

### Desafio 062: Super Progressão Aritmética v3.0
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

### Desafio 063: Sequência de Fibonacci v1.0
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Ex: 0 – 1 – 1 – 2 – 3 – 5 – 8

### Desafio 064: Tratando vários valores v1.0
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

### Desafio 065: Maior e Menor valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


