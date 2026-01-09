# 📝 Manipulação de Texto (Strings)
> Baseado na Aula 09 do Curso em Vídeo

Uma **String** é uma cadeia de caracteres. No Python, toda cadeia de texto está entre aspas simples ou duplas.

Para os exemplos abaixo, considere a variável:
```python
frase = "Curso em Video Python"
```

## 1. Fatiamento (Slicing)
Consiste em pegar pedaços da string.

### 📍 Entendendo o Índice 0
O Python começa a contar do **ZERO**. O índice `0` corresponde exatamente ao **primeiro caractere** (seja letra, número, símbolo ou espaço).

Visualização:
```text
   C   u   r   s   o
[0] [1] [2] [3] [4]  [5]
```

- `frase[9]`: Pega apenas o caractere no índice 9 (`'V'`).
- `frase[9:13]`: Começa no 9 e vai até o 12 (o último é excluído). Pega `'Vide'`.
- `frase[9:21:2]`: Começa no 9, vai até o 20, pulando de 2 em 2.
- `frase[:5]`: Do início (0) até o 4. Pega `'Curso'`.
- `frase[15:]`: Do 15 até o final. Pega `'Python'`.
- `frase[9::3]`: Começa no 9 e vai até o final, pulando de 3 em 3.

## 2. Análise
Saber informações sobre a string.

- **`len(frase)`**: Retorna o comprimento (tamanho) da string. Ex: `21`.
- **`frase.count('o')`**: Conta quantas vezes a letra 'o' (minúscula) aparece.
  - `frase.count('o', 0, 13)`: Conta 'o' apenas do índice 0 ao 12.
- **`frase.find('deo')`**: Mostra em que posição começou 'deo'. Se não encontrar, retorna `-1`.
- **`'Curso' in frase`**: Retorna `True` se a palavra existir na string.

## 3. Transformação
Altera a string (lembrando que strings são imutáveis, então esses métodos retornam uma *nova* string, não alteram a original a menos que você reatribua).

- **`frase.replace('Python', 'Android')`**: Substitui partes do texto.
- **`frase.upper()`**: Transforma tudo em MAIÚSCULAS.
- **`frase.lower()`**: Transforma tudo em minúsculas.
- **`frase.capitalize()`**: Joga tudo para minúsculo e só a primeira letra da string fica maiúscula.
- **`frase.title()`**: Analisa quantas palavras tem e coloca a primeira letra de cada palavra em maiúscula.

### Removendo Espaços
Útil para tratar entrada de dados (`input`).
- **`frase.strip()`**: Remove todos os espaços inúteis no **início** e no **fim**.
- **`frase.rstrip()`**: Remove espaços apenas à direita (Right).
- **`frase.lstrip()`**: Remove espaços apenas à esquerda (Left).

## 4. Divisão e Junção

### Divisão (`split`)
```python
frase.split()
```
- Divide a string em uma **lista**, onde cada palavra vira um item.
- Por padrão, divide pelos espaços.
- Ex: `['Curso', 'em', 'Video', 'Python']`

### Junção (`join`)
```python
'-'.join(lista)
```
- Junta uma lista de strings em uma única string, usando um separador.
- Ex: `'Curso-em-Video-Python'`

## 5. Dica Importante: Imutabilidade
Uma string não muda a menos que você salve o resultado nela mesma.
```python
frase = "Curso em Video Python"
frase.replace("Python", "Android") 
print(frase) # Ainda imprime "Curso em Video Python"

frase = frase.replace("Python", "Android")
print(frase) # Agora imprime "Curso em Video Android"
```
### Desafios sobre Fatiamento e Análise:
## Desafio 022
- Crie um programa que leia o nome completo de uma pessoa e mostre:
  - O nome com todas as letras maiúsculas e minúsculas.
  - Quantas letras ao todo (sem considerar espaços).
  - Quantas letras tem o primeiro nome.

## Desafio 023
- Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
ex:
```
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
```

## Desafio 024
- Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

## Desafio 025
- Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. 

## Desafio 026
- Faça um programa que leia uma frase pelo teclado e mostre:
  - Quantas vezes aparece a letra "A".
  - Em que posição ela aparece a primeira vez.
  - Em que posição ela aparece a última vez.

## Desafio 027
- Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
