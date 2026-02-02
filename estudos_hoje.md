# 🧠 Resumo de Estudos: Lógica de Programação e Teste de Mesa

**Data:** 02 de Fevereiro de 2026 (Referente aos estudos do dia)
**Foco:** Tradução de Algoritmos para Python e Rastreamento de Variáveis.

---

## 1. Estrutura `Enquanto` (While) com Condição Inicial
**Conceito:** Testar se um loop roda ou não dependendo da condição inicial.

### Código Python
```python
n = 0
cont = n      # cont recebe 0
res = 0
x = 2
n = 4         # n atualiza para 4

# Teste: 0 >= 4? Falso. O loop não executa.
while cont >= n:
    res = res * x
    cont += 1

print(res) # Saída: 0
```
**Explicação:** Como a variável `cont` (0) já começa menor que `n` (4), o loop `while` nunca é executado. O resultado permanece o valor inicial de `res`.

---

## 2. Simulando `Repita...Até` (Do-While)
**Conceito:** O Python não tem `do-while` nativo. Usamos `while True` com `break`.

### Código Python
```python
Y = 'CEV'
X = False

while True:
    print(Y)    # Executa a ação
    X = not X   # Inverte o valor lógico
    
    if not X:   # Condição de parada (Até que não X)
        break
```
**Explicação:**
1. 1ª volta: X é False -> Imprime "CEV" -> X vira True -> `not X` é False (continua).
2. 2ª volta: X é True -> Imprime "CEV" -> X vira False -> `not X` é True (para).
**Resultado:** Imprime "CEV" duas vezes.

---

## 3. Rastreamento de Variáveis (Trace Table)
**Conceito:** Acompanhar mudanças de valor em variáveis através de condicionais e loops `for`.

### Código Python
```python
X = 3
Y = 4
Z = 5

if (X - 1) > 2:  # (2 > 2) é Falso
    Y = Y + 1
    Y = Y - 1

Z = X + 1        # Z vira 4

for I in range(1, 9): # Roda 8 vezes (de 1 a 8)
    Y = Y + 1

Z = Z + Y        # Z = 4 + 12
print(Z)         # Saída: 16
```
**Explicação:** O `if` inicial é ignorado. O loop soma 1 ao Y oito vezes (4 + 8 = 12). Z soma seu valor (4) com Y (12), resultando em 16.

---

## 4. Condicionais Aninhadas (If dentro de If)
**Cenário:** A=Falso, B=Verdadeiro, C=Falso.

### Código Python
```python
if A:
    print("C1")
else:
    if B:           # Entra aqui (B é True)
        if C:
            print("C2")
        else:       # Entra aqui (C é False)
            print("C3")
            print("C4")
    print("C5")     # Executa ao sair do if B

print("C6")         # Executa sempre
```
**Resultado:** Executa C3, C4, C5 e C6.

---

## 5. Funções e Acumuladores
**Conceito:** Chamar uma função dentro de um loop e somar o retorno.

### Código Python
```python
def operacao(n):
    if n % 2 == 0:
        return n ** 2  # Par: Quadrado
    else:
        return n / 2   # Ímpar: Metade

S = 0
for c in range(1, 4): # c = 1, 2, 3
    S = S + operacao(c)

print(S) # Saída: 6.0
```
**Explicação:**
- c=1 (Ímpar): 0.5
- c=2 (Par): 4
- c=3 (Ímpar): 1.5
- Soma: 0.5 + 4 + 1.5 = 6.0

---

## 6. Expressões Lógicas e Tabela Verdade
**Conceito:** Precedência de `not`, `and`, `or`.

### Expressões
1. `.não. (x>3) e (x<1)...` -> **Falso** (Pois x=1 não é < 1).
2. `.não. (d<0) e (c>5) ou...` -> **Verdadeiro** (Primeira parte é V e V, logo V. O `ou` garante o V final).
3. `(x>=3) e ...` -> **Falso** (x=1, logo falha no início).
4. `.não. (d>3) ou ...` -> **Falso** (Todas as negações invertem os verdadeiros para falso).

---

## 7. Loop While com Acumulador (Soma)
**Conceito:** Somar uma sequência de números até um limite.

### Código Python
```python
INDICE = 6
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
    print(f'K: {K}')

print(f'SOMA: {SOMA}')
```
**Explicação:**
O código soma os números de 1 a 6.
1 + 2 + 3 + 4 + 5 + 6 = **21**.

---

## 📌 Conclusão do Dia
Esses exercícios reforçaram a importância de fazer o **Teste de Mesa** (simular o computador no papel) antes de codificar.

- **Atenção:** Em Python, `range(a, b)` vai até `b-1`.
- **Atenção:** Python usa indentação para definir blocos, não `fim_se` ou `fim_para`.
- **Atenção:** Operadores lógicos são `not`, `and`, `or`.
```

<!--
[PROMPT_SUGGESTION]Pode criar um script Python que execute todos esses exemplos de uma vez para eu ver os resultados?[/PROMPT_SUGGESTION]
[PROMPT_SUGGESTION]Gostaria de um exercício novo desafiador envolvendo listas e loops para praticar o que aprendi hoje.[/PROMPT_SUGGESTION]
->