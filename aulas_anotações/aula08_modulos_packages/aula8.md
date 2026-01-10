# Aula 08 — Módulos

Este arquivo contém a explicação teórica sobre módulos e packages.


## O que é um Módulo?
Um módulo é um arquivo contendo definições e instruções Python que podem ser importados para outros arquivos para reutilização de código.

## Exemplo Prático: Comidas, Bebidas e Doces
Vamos imaginar que organizamos nosso código em módulos do dia a dia, como `comida`, `bebida` e `doce`.

### Utilizando o Módulo de Doces
Vamos usar o exemplo de um módulo de pudim. Existem duas formas principais de utilizá-lo:

1. **Importação Geral**:
   Você importa o módulo inteiro. É útil quando você quer manter a referência de onde a função veio (da "loja" de doces).
   ```python
   import aula08_modulos.doce.pudim as pudim 
   
   pudim.fazer_pudim() 
   # pudim         -> Onde está (O Módulo/Local)
   # fazer_pudim() -> A ação (A Função)
   ```
   **Entendendo a linha `import ... as ...`:**
   - `import`: Comando para trazer o código.
   - `aula08_modulos.doce.pudim`: O caminho completo até o arquivo (Pasta aula08_modulos -> Pasta doce -> Arquivo pudim).
   - `as`: Significa "como" (usado para dar um apelido).
   - `pudim`: O **apelido** que escolhemos. Sem isso, teríamos que escrever o nome completo (`aula08_modulos.doce.pudim.fazer_pudim()`) toda vez. Com o apelido, fica só `pudim.fazer_pudim()` não necessariamente eu preciso toda vez ter que digitar todo o caminho pra chegar até o arquivo.

2. **Importação Específica**:
   Você importa apenas a função específica, como se pegasse apenas o pudim para si, sem precisar carregar o resto.
   ```python
   from aula08_modulos.doce.pudim import fazer_pudim
   
   fazer_pudim() 
   # fazer_pudim() -> Apenas a ação (Já dissemos de onde veio no 'from')
   ```

### Entendendo a Estrutura (Packages)
Quando fazemos `from aula08_modulos.doce.pudim`, o Python segue as pastas do seu computador. Criar pastas para organizar categorias é o que chamamos de criar **Packages**.

**Visualizando a estrutura:**
```text
aula08_modulos/ (Pasta Principal)
 └── doce/ (Pasta da Categoria)
      ├── pudim.py (Arquivo/Módulo)
      └── brigadeiro.py (Arquivo/Módulo)
      
### O que tem dentro do arquivo? (Os Ingredientes)
Dentro do arquivo (módulo), você coloca o código real. É lá que estão os "ingredientes" e o "modo de preparo".

Por exemplo, dentro de `pudim.py` teríamos:
```python
# Conteúdo do arquivo pudim.py

ingrediente_secreto = "Leite Condensado" # Variável (Ingrediente)

def fazer_pudim(): # Função (Modo de Preparo)
    print(f"Usando {ingrediente_secreto}...")
    print("Batendo tudo e assando...")
    return "Pudim está pronto!"
```

## Exemplo: Módulo `math`
O módulo `math` (nativo do Python) segue a mesma lógica dos doces acima:

1. **Importação Genérica**: `import math`
   - Traz todas as funções (`math.sqrt`, `math.ceil`, etc).
2. **Importação Específica**: `from math import sqrt`
   - Traz apenas a raiz quadrada (usa-se direto `sqrt`).

### Principais Funções:
- `ceil`: Arredonda para cima.
- `floor`: Arredonda para baixo.
- `trunc`: Elimina a parte decimal (trunca o número).
- `factorial`: Calcula o fatorial.
- `pow`: Potência.
- `sqrt`: Raiz quadrada. 

## Tipos de Importação e Bibliotecas

### 1. Módulos Padrão (Standard Library)
São aqueles que já vêm instalados junto com o Python. Você não precisa instalar nada, apenas importar.
- **Exemplos comuns:** 
  - `os`, `shutil` (Manipulação de arquivos)
  - `datetime`, `time` (Data e hora)
  - `math`, `random` (Matemática e aleatoriedade)

### 2. Pacotes (Packages)
Pacotes são coleções de módulos relacionados organizados em diretórios. Eles permitem melhor organização e reutilização.
- **Exemplo:** `NumPy` (usado para computação científica e arrays).

### 3. Pacotes Externos (Third-Party)
São bibliotecas criadas pela comunidade que não vêm com o Python. Para usá-las, você precisa instalar usando o gerenciador de pacotes **pip**.
- **Comando de instalação:** `pip install nome_do_pacote`
- **Exemplo:** `Pandas` (análise de dados), `emoji` (ícones).

> **Nota:** Sempre verifique se o pacote está instalado no seu ambiente antes de tentar importá-lo, é possivel fazer isso com o comando "Ctrl" + espaço após o "import", deste modo, você poderá ver todos os módulos padrão disponíveis na biblioteca do Python.

## Curiosidade: O que é o PyPI?
O **PyPI** (Python Package Index) é o repositório oficial de softwares para a linguagem de programação Python. Quando você usa o comando `pip install`, é de lá que os arquivos são baixados.

## Dica Extra: Explorando Módulos
Se você quiser ver todas as funções disponíveis dentro de um módulo diretamente no código, pode usar o comando `dir()`:
```python
import math
print(dir(math)) # Mostra uma lista com todos os nomes definidos no módulo math
```
# Desafios:
## Desafio 016
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
Ex: 
Digite um número: 6.127
O número 6.127 tem a parte Inteira 6.

## Desafio 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

## Desafio 018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

## Desafio 019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

## Desafio 020
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

## Desafio 021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
