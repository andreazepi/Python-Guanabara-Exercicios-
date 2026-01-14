# 🔀 Estruturas de Controle
> Decisões e Repetições

## 1. Condições (`if`, `elif`, `else`)
Permitem que o programa tome decisões baseadas em testes lógicos.

```python
idade = int(input("Idade: "))

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem exatamente 18 anos")
else:
    print("Maior de idade")
```

## 2. Estruturas de Repetição (Loops)
Usadas para repetir blocos de código.

### `for` (Para)
Repete por um número determinado de vezes ou percorre uma coleção.
```python
for i in range(3): # Repete 0, 1, 2
    print(i)
```

### `while` (Enquanto)
Repete enquanto uma condição for verdadeira.
```python
c = 0
while c < 5:
    print(c)
    c += 1
```

### Controle de Fluxo
- **`break`**: Interrompe o loop imediatamente.
- **`continue`**: Pula para a próxima iteração.