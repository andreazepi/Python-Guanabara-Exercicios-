# 📚 Fundamentos de Python
> Baseado nas aulas do Curso em Vídeo (Prof. Guanabara)

## 1. Saída de Dados (`print`)
O comando `print()` é utilizado para exibir mensagens ou resultados na tela.

- **Mensagens de texto:** Devem estar entre aspas (simples ou duplas). Ex: `print("Olá Mundo")`
- **Números:** Não precisam de aspas. Ex: `print(360)`
- **Cálculos:** O Python resolve operações dentro do print. `print(7 + 4)` exibe `11`.
- **Concatenação:**
  - Usando vírgula (`,`): Junta valores adicionando um espaço automaticamente.
  - Usando mais (`+`): Junta strings sem espaço (se forem números, ele soma).

## 2. Variáveis e Memória
Variáveis são espaços na memória para guardar valores.
- **Sintaxe:** `nome = valor` (O sinal `=` lê-se "recebe").
- **Regras de Nomes:**
  - Devem começar com letras (minúsculas por convenção).
  - Sem espaços (use `snake_case`, ex: `nome_usuario`).
  - Não podem começar com números.

## 3. Tipos de Dados Primitivos

| Tipo | Nome Python | Descrição | Exemplo |
| --- | --- | --- | --- |
| **String** | `str` | Textos (entre aspas) | `"Python"`, `"10"` |
| **Inteiro** | `int` | Números sem casa decimal | `10`, `-5`, `0` |
| **Flutuante** | `float` | Números com ponto decimal | `3.14`, `10.0` |
| **Booleano** | `bool` | Valor Lógico | `True`, `False` |

## 4. Entrada de Dados (`input`)
Permite interação com o usuário.
**⚠️ Importante:** O `input()` sempre retorna uma **String**. Para cálculos, converta o tipo (casting).

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) # Converte para Inteiro
altura = float(input("Digite sua altura: ")) # Converte para Float
```

## 5. Operações Aritméticas

| Operação | Símbolo | Ordem |
| --- | --- | --- |
| Parênteses | `()` | 1º |
| Potência | `**` | 2º |
| Mult., Div., Resto | `*`, `/`, `//`, `%` | 3º |
| Soma e Subtração | `+`, `-` | 4º |