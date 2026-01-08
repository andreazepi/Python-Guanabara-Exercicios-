# 🎲 Estudo de Caso: Sorteio de Alunos (Desafio 019)

Este arquivo detalha diferentes formas de resolver o problema de sortear um item dentro de uma lista em Python, utilizando o módulo `random`.

## O Problema
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. O programa deve ler o nome dos alunos e escrever o nome do escolhido.

---

## 1. Método Clássico (Variáveis Separadas)
Nesta abordagem, criamos uma variável para cada aluno e depois agrupamos tudo em uma lista. É a forma mais didática para iniciantes.

```python
import random

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

aluno_escolhido = random.choice(lista_alunos)
print(f'O aluno escolhido foi: {aluno_escolhido}')
```

## 2. Método Otimizado (Lista Direta)
Aqui, inserimos o `input()` diretamente dentro da declaração da lista. Isso economiza linhas de código e evita a criação de variáveis intermediárias (`aluno1`, `aluno2`...).

```python
lista_alunos = [
    input('Digite o nome do primeiro aluno: '),
    input('Digite o nome do segundo aluno: '),
    input('Digite o nome do terceiro aluno: '),
    input('Digite o nome do quarto aluno: ')
]
print(f'O aluno escolhido foi: {random.choice(lista_alunos)}')
```

## 3. Usando `random.sample()`
O método `sample` retorna uma **lista** com a quantidade de elementos solicitados, diferentemente do `choice` que retorna o elemento direto.

```python
# random.sample(lista, k) -> Retorna uma LISTA com k elementos únicos
aluno_escolhido = random.sample(lista_alunos, 1)

# Como retorna uma lista (ex: ['Maria']), precisamos acessar o índice [0] para pegar o texto.
print(f'O aluno escolhido foi: {aluno_escolhido[0]}')
```

## 4. Entrada Única com `.split()` (Avançado)
Permite que o usuário digite todos os nomes em uma única linha, separados por vírgula.

```python
nomes = input("Digite os 4 nomes separados por vírgula: ")

# O split quebra o texto onde tem vírgula e cria a lista automaticamente.
lista_alunos = nomes.split(",") 

# .strip() remove espaços extras que podem ter ficado (ex: " Ana")
print(f'O aluno escolhido foi: {random.choice(lista_alunos).strip()}')
```