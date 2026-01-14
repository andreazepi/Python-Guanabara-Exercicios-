Aqui está o resumo limpo e focado 100% em **Python**, sem as referências ao Portugol/Visualg.

Pode copiar e colar no seu arquivo `.md` no VS Code.

---

```markdown
# 🐍 Resumo: Algoritmos e Lógica de Programação (Python)

## 1. Entrada e Saída de Dados
Em Python, a tipagem é dinâmica (não precisa declarar o tipo antes). O fluxo básico é: ler dados, processar e mostrar resultados.

### Comandos Básicos
* `print()`: Exibe informações na tela.
* `input()`: Lê informações do teclado (sempre retorna texto/string).
* **Conversão:** Se for número, use `int()` para inteiros ou `float()` para reais.

**Exemplo: Saudação e Soma**
```python
# Entrada
nome = input("Digite seu nome: ")
n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe outro número inteiro: "))

# Processamento
soma = n1 + n2

# Saída (usando f-string para formatar)
print(f"Muito prazer, {nome}!")
print(f"A soma entre {n1} e {n2} é {soma}.")

```

---

## 2. Operadores e Módulos Matemáticos

O Python faz operações básicas nativamente, mas para operações avançadas importamos o módulo `math`.

### Operadores Nativos

* `+`, `-`, `*`, `/`: Básicos.
* `**`: Potenciação (Ex: `5 ** 2` é 25).
* `%`: Resto da divisão (Módulo).
* `//`: Divisão inteira.

### Módulo `math`

```python
import math

raiz = 81
angulo = 45

# Raiz Quadrada
print(math.sqrt(raiz)) # Saída: 9.0
# Dica: Raiz também pode ser feita sem import: print(raiz ** 0.5)

# Trigonometria (Requer conversão para radianos)
radiano = math.radians(angulo)
print(f"Seno: {math.sin(radiano):.2f}")
print(f"Cosseno: {math.cos(radiano):.2f}")

# Valor Absoluto (ignora o sinal negativo)
print(abs(-50)) # Saída: 50

```

---

## 3. Operadores Relacionais e Lógicos

O resultado dessas operações é sempre um valor Booleano: `True` (Verdadeiro) ou `False` (Falso).

### Relacionais (Comparação)

* `==`: Igual a
* `!=`: Diferente de
* `>`: Maior que
* `<`: Menor que
* `>=`: Maior ou igual
* `<=`: Menor ou igual

### Lógicos (Conectivos)

* `and`: Retorna `True` se **todas** as condições forem verdadeiras.
* `or`: Retorna `True` se **pelo menos uma** condição for verdadeira.
* `not`: Inverte o valor (`True` vira `False`).

**Exemplo: Análise de Triângulo**

```python
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

# Equilátero: Todos os lados iguais
eq = (l1 == l2) and (l2 == l3)

# Escaleno: Todos os lados diferentes
es = (l1 != l2) and (l2 != l3) and (l1 != l3)

print(f'O triângulo é Equilátero? {eq}')
print(f'O triângulo é Escaleno? {es}')

```

---

## 4. Estruturas Condicionais (`if`, `elif`, `else`)

Define o fluxo do código baseado em decisões. O Python usa a **indentação** (espaço no início da linha) para saber o que está dentro do bloco.

### Estrutura Simples e Composta

```python
n = int(input("Digite um número: "))

# Verifica se o resto da divisão por 2 é zero
if n % 2 == 0:
    print(f"O número {n} é PAR.")
else:
    print(f"O número {n} é ÍMPAR.")

```

### Estrutura Aninhada (`elif`)

Usado quando temos múltiplas condições. Exemplo: Cálculo de IMC.

```python
massa = float(input("Massa (Kg): "))
altura = float(input("Altura (m): "))
imc = massa / (altura ** 2)

print(f"IMC: {imc:.2f}")

if imc < 17:
    print("Muito abaixo do peso")
elif imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade")
elif imc < 40:
    print("Obesidade Severa")
else:
    print("Obesidade Mórbida")

```

---

## 5. Estruturas de Repetição (Loops)

### Enquanto (`while`)

Repete enquanto uma condição for verdadeira. Ideal quando não sabemos o limite exato de repetições.

```python
contador = 0
limite = int(input("Quer contar até quanto? "))

while contador <= limite:
    print(contador)
    contador += 1 # Incremento
print("Fim da contagem.")

```

### Para (`for`)

Repete um número determinado de vezes.

* `range(inicio, fim, passo)`: O `fim` no Python é excludente (se colocar 10, ele vai até 9).

```python
# Contar de 0 a 10 pulando de 2 em 2
for i in range(0, 11, 2):
    print(i)

```

**Exemplo Prático: Detector de Maior Peso**

```python
maior_peso = 0
nome_pesado = ""

for i in range(1, 6): # Repete 5 vezes (de 1 a 5)
    print("-" * 20)
    nome = input(f"Pessoa {i} - Nome: ")
    peso = float(input(f"Pessoa {i} - Peso (Kg): "))

    if peso > maior_peso:
        maior_peso = peso
        nome_pesado = nome

print("-" * 20)
print(f"A pessoa mais pesada foi {nome_pesado} com {maior_peso} Kg.")

```

---

## 6. Funções (`def`)

Usadas para organizar o código em blocos reutilizáveis.

### Função sem retorno (Procedimento)

```python
def cabecalho(texto):
    print("-" * 30)
    print(texto.center(30))
    print("-" * 30)

# Uso
cabecalho("SISTEMA ALUNO")

```

### Função com retorno

Realiza um cálculo e devolve o valor para uma variável.

```python
def somar(a, b):
    s = a + b
    return s

# Uso
n1 = 5
n2 = 8
resultado = somar(n1, n2)
print(f"A soma retornada foi {resultado}")

```

---

## 7. Variáveis Compostas (Listas)

No Python, usamos **Listas** para substituir Vetores e Matrizes. A contagem do índice começa em **0**.

### Vetores (Listas Unidimensionais)

```python
valores = [] # Lista vazia

# Preenchendo a lista
for i in range(3):
    num = int(input(f"Digite valor para posição {i}: "))
    valores.append(num) # Adiciona ao final da lista

# Acessando dados
print(f"Lista completa: {valores}")
print(f"Primeiro valor: {valores[0]}")

```

### Matrizes (Listas dentro de Listas)

```python
# Matriz 2x2
matriz = [
    [0, 0],
    [0, 0]
]

# Preenchendo
for l in range(2): # Linha
    for c in range(2): # Coluna
        matriz[l][c] = int(input(f"Valor [{l},{c}]: "))

# Exibindo como tabela
for l in range(2):
    print(matriz[l])

```
