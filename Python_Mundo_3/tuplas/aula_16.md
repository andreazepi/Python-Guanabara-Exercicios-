### 🐍 Aula 16: Tuplas em Python - O Guia Completo

> **🎼 Analogia Musical:** Imagine que uma **Tupla** é como uma *partitura impressa*. Você pode ler a música, tocar pedaços diferentes dela, saber quantas notas ela tem e descobrir onde está uma nota específica. Porém, **você não pode apagar ou alterar uma nota diretamente no papel impresso**. Para mudar a música, você precisaria escrever uma partitura nova!

---

## 1. A Regra de Ouro: Tuplas são IMUTÁVEIS 🔒

A característica mais importante das Tuplas é a **Imutabilidade**. Isso significa que, após ser criada, ela NÃO PODE ser modificada.

```python
lanche = ('Sanduíche', 'Suco', 'Pudim', 'Pizza')

# Tentando mudar o Sanduíche por Hamburger:
lanche[0] = 'Hamburger'  
# ❌ ERRO! TypeError: 'tuple' object does not support item assignment

# Tentando deletar apenas um item:
del(lanche[0])  
# ❌ ERRO! TypeError: 'tuple' object doesn't support item deletion
```
*Nota:* Você pode apagar a tupla inteira da memória usando `del(lanche)`, mas nunca um único item de dentro dela.

---

## 2. Variáveis Simples vs Compostas

- **Variável Simples**: Armazena um único valor. (Ex: Uma nota musical solta).
  ```python
  lanche = 'Sanduíche'
  ```
- **Variável Composta**: Armazena vários valores em um único espaço. (Ex: Um acorde ou um compasso inteiro).
  ```python
  lanche = ('Sanduíche', 'Suco', 'Pudim', 'Pizza')
  ```

Em Python, temos 3 principais variáveis compostas:
1. **Tuplas** `()` -> Imutáveis (O que vamos focar agora).
2. **Listas** `[]` -> Mutáveis (Veremos depois).
3. **Dicionários** `{}` -> Chave-Valor.

---

## 3. Criando Tuplas

Tuplas aceitam misturar tipos de dados (Textos, Números, Decimais) no mesmo lugar.

```python
# Forma 1: Com Parênteses (Mais comum e recomendada)
lanche = ('Sanduíche', 'Suco', 'Pudim', 'Pizza')

# Forma 2: Sem Parênteses (O Python entende automaticamente)
lanche = 'Sanduíche', 'Suco', 'Pudim', 'Pizza'

# Forma 3: Dados misturados
pessoa = ('Andre', 30, 'M', 75.5) # String, Int, String, Float
```

---

## 4. Acessando Elementos (Indexação) 🔍

Cada item recebe um número de posição (índice). **Em Python, a contagem sempre começa no ZERO.**

```text
Valores:  'Sanduíche', 'Suco', 'Pudim', 'Pizza'
Índices:       0          1       2        3
```

```python
print(lanche[0])   # Saída: Sanduíche
print(lanche[2])   # Saída: Pudim
print(lanche[-1])  # Saída: Pizza (O índice -1 sempre pega o último item!)
```

---

## 5. Pegando "Pedaços" (Fatiamento / Slicing) 🍕

Você pode extrair partes da tupla usando a sintaxe `[início:fim]`. 
⚠️ **Atenção:** O número do "fim" é ignorado pelo Python (ele para um elemento antes).

```python
lanche = ('Sanduíche', 'Suco', 'Pudim', 'Pizza')

print(lanche[0:2])   # Saída: ('Sanduíche', 'Suco') -> Pega o 0 e o 1. Ignora o 2.
print(lanche[1:])    # Saída: ('Suco', 'Pudim', 'Pizza') -> Do 1 até o final.
print(lanche[:3])    # Saída: ('Sanduíche', 'Suco', 'Pudim') -> Do começo até o 2.
```

---

## 6. Percorrendo a Tupla (Laço For) 🔄

Você vai usar muito o `for` para varrer os itens de uma tupla. Escolha a forma que melhor se adapta ao que você precisa:

**Forma 1: Quando você SÓ precisa do nome do item**
```python
for comida in lanche:
    print(f'Eu vou comer {comida}')
```

**Forma 2: Quando você precisa da POSIÇÃO numérica e do item**
```python
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
```

**Forma 3: A mais elegante (Usando `enumerate`) ⭐**
```python
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
```

---

## 7. Operações Úteis com Tuplas 🛠️

```python
# 📏 Descobrir o tamanho da tupla (len)
print(len(lanche))  # Saída: 4

# 🔀 Unir (Concatenar) tuplas usando o '+'
a = (2, 5, 4)
b = (5, 7, 1, 2)
c = a + b
print(c)  # Saída: (2, 5, 4, 5, 7, 1, 2)

# 🔤 Mostrar em ordem alfabética / crescente (sorted)
print(sorted(lanche))  # Obs: Isso transforma a saída numa Lista []

# 🔢 Contar quantas vezes um item aparece (count)
numeros = (2, 5, 4, 5, 7, 1, 2, 5)
print(numeros.count(5))  # Saída: 3 (O número 5 aparece três vezes)

# 📍 Descobrir a posição de um item (index)
print(numeros.index(7))  # Saída: 4 (O número 7 está na posição quatro)
```

---

## 8. Tabela Resumo Rápida

| Ação | Tuplas Suportam? |
|---|---|
| Criação | `()` ou sem parênteses |
| **Imutável** | ✅ SIM (Não muda após criada) |
| Acessar por posição (Índice) | ✅ SIM |
| Pegar pedaços (Fatiamento) | ✅ SIM |
| Aceitar tipos misturados (Int, String) | ✅ SIM |
| Adicionar / Remover item | ❌ NÃO |
| Modificar um item existente | ❌ NÃO |

---

# 🎯 DESAFIOS PRÁTICOS (072 ao 077)
*Lembre-se da técnica do seu guia: Tente quebrar a cabeça por 15 min antes de ver a resposta!*

### 🏁 Desafio 072: Número por Extenso
**O que fazer:** Crie uma tupla com os números escritos por extenso (`'zero'`, `'um'`, `'dois'`, até `'vinte'`). Peça para o usuário digitar um número entre 0 e 20. Pegue o número digitado e use-o como **índice** para buscar a palavra certa na tupla.
*Dica:* Use um laço `while True` para obrigar o usuário a digitar um número válido.

### ⚽ Desafio 073: Tabela do Brasileirão
**O que fazer:** Crie uma tupla com os 20 primeiros times do Brasileirão em ordem.
- A) Mostre os 5 primeiros (Slicing `[:5]`).
- B) Mostre os 4 últimos (Slicing `[-4:]`).
- C) Mostre os times em ordem alfabética (Use `sorted()`).
- D) Descubra a posição de um time específico (Use `.index('Nome_do_Time') + 1`).

### 🎲 Desafio 074: Sorteio de Números
**O que fazer:** Use `random.randint` para gerar 5 números aleatórios. Coloque-os dentro de uma tupla.
*Dica de Ouro:* No final, basta usar as funções nativas `max(sua_tupla)` e `min(sua_tupla)` para encontrar o maior e menor número num piscar de olhos!

### 🔢 Desafio 075: Análise de Dados
**O que fazer:** Peça 4 números pelo teclado e coloque dentro de uma tupla (Sim, você pode colocar `int(input())` direto dentro dos parênteses da tupla, separados por vírgula).
- A) Quantas vezes apareceu o 9? (Use `.count()`).
- B) Posição do primeiro número 3 (Use `.index()`. *Cuidado: use um `if 3 in tupla` antes para não dar erro se o 3 não existir!*).
- C) Mostre os pares (Faça um `for` e use `if num % 2 == 0`).

### 🛒 Desafio 076: Lista de Preços (Tabular)
**O que fazer:** Crie uma única tupla intercalando Nome e Preço. Ex: `('Pão', 1.50, 'Leite', 3.20)`.
*Dica:* Faça um laço `for` avançando de 2 em 2 posições ou use `len(tupla)`. Se a posição for par (`pos % 2 == 0`), é o nome do produto (alinhe à esquerda). Se for ímpar, é o preço (alinhe à direita com `R$`).

### 🔠 Desafio 077: Caçador de Vogais
**O que fazer:** Crie uma tupla com várias palavras soltas. Crie um laço `for` para passar por cada palavra. Dentro dele, crie *outro* laço `for` para passar por cada letra da palavra, verificando `if letra in 'aeiou':` e imprima a vogal.
