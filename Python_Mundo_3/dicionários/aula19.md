# 🐍 Aula 19: Dicionários - O Guia Definitivo

Dicionários são uma das estruturas mais poderosas e flexíveis do Python. Se as listas são como uma "fila" numerada, os dicionários são como uma "agenda" ou um "catálogo", onde você acessa a informação por um nome específico, não por um número de posição.

---

## 1. O que é um Dicionário?

É uma coleção de itens que **não é ordenada por posição**, but sim por um sistema de **`chave: valor`**.

- **Chave (Key):** Um identificador único (como uma palavra em um dicionário real ou um CPF em um cadastro). Geralmente é uma string ou um número.
- **Valor (Value):** A informação associada àquela chave (como a definição da palavra ou os dados da pessoa). Pode ser qualquer tipo de dado: string, número, lista, ou até outro dicionário.

**Sintaxe:** Utilizam chaves `{}`.

```python
# Exemplo: Dicionário representando uma pessoa
pessoa = {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}
```

---

## 2. Operações Fundamentais (CRUD)

CRUD significa **Create, Read, Update, Delete** (Criar, Ler, Atualizar, Deletar).

### Criar (Create)
Você pode criar um dicionário vazio ou já com dados.
```python
# Dicionário vazio
dados = dict() 
# ou
dados = {}

# Dicionário com dados
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
```

### Ler (Read / Acessar)
Você acessa um valor usando sua chave entre colchetes `[]`.
```python
print(filme['titulo'])  # Saída: Star Wars
print(filme['ano'])     # Saída: 1977
```

### Atualizar / Adicionar (Update)
Se a chave não existe, um novo par `chave: valor` é adicionado. Se a chave já existe, seu valor é substituído.
```python
# Adicionando um novo elemento
filme['genero'] = 'Ficção Científica'

# Atualizando um elemento existente
filme['ano'] = 1978 
```

### Deletar (Delete)
Use o comando `del` para remover um par `chave: valor`.
```python
del filme['diretor']
```

---

## 3. Iterando sobre Dicionários (A Parte Mais Importante!)

Existem três formas principais de percorrer um dicionário com um loop `for`.

### A. Pegando apenas as Chaves (`.keys()`)
Útil quando você só precisa dos identificadores.
```python
for chave in filme.keys():
    print(chave)
# Saída:
# titulo
# ano
# genero
```

### B. Pegando apenas os Valores (`.values()`)
Útil quando você só precisa dos dados, sem se importar com a chave.
```python
for valor in filme.values():
    print(valor)
# Saída:
# Star Wars
# 1978
# Ficção Científica
```

### C. Pegando Chave e Valor Juntos (`.items()`) - O Padrão de Ouro!
Este é o método mais comum e poderoso. Ele retorna, a cada volta do loop, uma **tupla com dois itens: (chave, valor)**.

```python
# filme.items() gera algo como: [('titulo', 'Star Wars'), ('ano', 1978), ...]

# O for desempacota essa tupla em duas variáveis!
for k, v in filme.items():
    # k -> recebe o primeiro item da tupla (a chave)
    # v -> recebe o segundo item da tupla (o valor)
    print(f'O {k} é {v}')

# Saída:
# O titulo é Star Wars
# O ano é 1978
# O genero é Ficção Científica
```
> **Lembre-se:** `k` e `v` são apenas **nomes de convenção** (key/value). Você poderia usar `for chave, valor in filme.items():` e o resultado seria idêntico. O que importa é a **ordem**: a primeira variável sempre pega a chave, a segunda sempre pega o valor.

---

## 4. Dicionários e Listas: A Combinação Perfeita

É extremamente comum ter uma **lista onde cada item é um dicionário**. Isso permite criar estruturas de dados complexas, como um cadastro de vários filmes ou pessoas.

```python
# Lista de dicionários
locadora = [
    {'titulo': 'Star Wars', 'ano': 1977},
    {'titulo': 'Matrix', 'ano': 1999},
    {'titulo': 'Interestelar', 'ano': 2014}
]

# Acessando dados
print(locadora[0]['titulo'])  # Saída: Star Wars
print(locadora[2]['ano'])     # Saída: 2014

# Iterando sobre a lista de dicionários
for filme_atual in locadora:
    print(f"--- Filme: {filme_atual['titulo']} ---")
    for chave, valor in filme_atual.items():
        print(f" - {chave}: {valor}")
```

---

## 5. Copiando Dicionários

Cuidado! Usar `=` não cria uma cópia, cria uma **ligação**.

```python
d1 = {'a': 1}
d2 = d1  # Ligação! Não é uma cópia.
d2['a'] = 99

print(d1) # Saída: {'a': 99} -> d1 foi alterado também!

# Para copiar de verdade, use o método .copy()
d3 = {'b': 2}
d4 = d3.copy()
d4['b'] = 100

print(d3) # Saída: {'b': 2} -> d3 permanece intacto!
```

---

## 🎯 Exercícios Propostos (090 ao 095)

### Desafio 090: Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

### Desafio 091: Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

### Desafio 092: Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

### Desafio 093: Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

### Desafio 094: Unindo dicionários e listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A média de idade.
C) Uma lista com as mulheres.
D) Uma lista de pessoas com idade acima da média.

### Desafio 095: Aprimorando os Dicionários
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.