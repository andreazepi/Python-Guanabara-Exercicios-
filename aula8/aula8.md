# Aula 8 — Módulos

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
   import aula8.doce.pudim as pudim # toda vez que 
   
   pudim.fazer_pudim() 
   # pudim         -> Onde está (O Módulo/Local)
   # fazer_pudim() -> A ação (A Função)
   ```
   **Entendendo a linha `import ... as ...`:**
   - `import`: Comando para trazer o código.
   - `aula8.doce.pudim`: O caminho completo até o arquivo (Pasta aula8 -> Pasta doce -> Arquivo pudim).
   - `as`: Significa "como" (usado para dar um apelido).
   - `pudim`: O **apelido** que escolhemos. Sem isso, teríamos que escrever o nome completo (`aula8.doce.pudim.fazer_pudim()`) toda vez. Com o apelido, fica só `pudim.fazer_pudim()` não necessariamente eu preciso toda vez ter que digitar todo o caminho pra chegar até o arquivo.

2. **Importação Específica**:
   Você importa apenas a função específica, como se pegasse apenas o pudim para si, sem precisar carregar o resto.
   ```python
   from aula8.doce.pudim import fazer_pudim
   
   fazer_pudim() 
   # fazer_pudim() -> Apenas a ação (Já dissemos de onde veio no 'from')
   ```

### Onde fica o arquivo? (Packages)
Quando você vê o comando `from aula8.doce.pudim`, o Python está seguindo o caminho das pastas no seu computador para encontrar o arquivo:

1. **aula8**: É a pasta principal.
2. **doce**: É uma subpasta (pacote) dentro de aula8.
3. **pudim**: É o arquivo `pudim.py` (o módulo) dentro da pasta doce.

### Devo criar uma pasta para tudo?
Sim, essa é uma ótima prática de organização!

- **Categoria Geral (ex: `doce`)** -> Vira uma **Pasta** (chamamos de *Package*).
- **Itens Específicos (ex: `pudim`, `brigadeiro`)** -> Viram **Arquivos** `.py` dentro dessa pasta (chamamos de *Módulos*).

**Visualizando a estrutura:**
```text
aula8/ (Pasta Principal)
 └── doce/ (Pasta da Categoria)
      ├── pudim.py (Arquivo/Módulo)
      └── brigadeiro.py (Arquivo/Módulo)
      
      ### O que tem dentro do arquivo? (Os Ingredientes) +Dentro do arquivo (módulo), você coloca o código real. É lá que estão os "ingredientes" e o "modo de preparo". + +Por exemplo, dentro de pudim.py teríamos: +```python +# Conteúdo do arquivo pudim.py + +ingrediente_secreto = "Leite Condensado" # Variável (Ingrediente) + +def fazer_pudim(): # Função (Modo de Preparo)

print(f"Usando {ingrediente_secreto}...")
print("Batendo tudo e assando...")
return "Pudim está pronto!" +
```

## Exemplo: Módulo `math`
O módulo `math` fornece funções matemáticas avançadas. Existem duas formas principais de importá-lo:

1. **Importação Genérica**: `import math`
   - Importa todas as funcionalidades.
   - Uso: `import math`

2. **Importação Específica**: `from math import sqrt`
   - Importa apenas a função específica desejada, como neste caso abaixo a raiz quadrada.
   - Uso: `sqrt(25)`

### Principais Funções:
- `ceil`: Arredonda para cima.
- `floor`: Arredonda para baixo.
- `trunc`: Elimina a parte decimal (trunca o número).
- `factorial`: Calcula o fatorial.
- `pow`: Potência.
- `sqrt`: Raiz quadrada. 


