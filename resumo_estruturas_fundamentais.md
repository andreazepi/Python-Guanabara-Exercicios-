# 🐍 Guia de Estruturas Python: Do Básico ao Profissional

Este guia serve como referência rápida para sintaxe e, principalmente, para entender **quando** aplicar cada estrutura em cenários reais de desenvolvimento.

---

## 1. Condicionais (`if`, `elif`, `else`)

### 💀 Esqueleto
```python
if condicao:
    # Bloco executado se a condição for Verdadeira
elif outra_condicao:
    # Bloco executado se a primeira for Falsa e esta for Verdadeira
else:
    # Bloco executado se nenhuma das anteriores for Verdadeira
```

### 💡 Quando usar?
- **Lógica:** Tomada de decisão. O código precisa seguir caminhos diferentes.
- **Exemplo Acadêmico:** Verificar se um aluno passou de ano (nota >= 7).

### 💼 Cenário Real (Dev Junior / Estágio)
- **Validação de Permissões:** Verificar se o usuário logado é "Admin" para liberar um botão de "Deletar".
- **Feature Flags:** Ativar uma funcionalidade nova apenas para um grupo de usuários beta.
- **Tratamento de Erros:** Se a resposta do banco de dados vier vazia (`if not dados:`), mostrar mensagem de "Nenhum registro encontrado".

## 1.1. Estrutura de Escolha (`match` / `case`)
*(Disponível a partir do Python 3.10)*

### 💀 Esqueleto
```python
match variavel:
    case 1:
        # Faz algo se for 1
    case 2:
        # Faz algo se for 2
    case _:
        # O "Curinga" (equivalente ao else)
```

### 💡 Quando usar?
- Quando você tem **uma** variável e quer testá-la contra **vários** valores específicos (ex: Menu de opções 1, 2, 3).
- Substitui cadeias longas e feias de `if opcao == 1 ... elif opcao == 2 ...`.

---

## 2. Laços de Repetição: `for`

### 💀 Esqueleto
```python
# Opção A: Iterar sobre um intervalo numérico
for i in range(inicio, fim, passo):
    # Faz algo com i

# Opção B: Iterar sobre uma coleção (Lista, String, Tupla)
for item in lista_de_itens:
    # Faz algo com o item
```

### 🧩 Como Pensar por Partes?
1. **Parte 1 (O Mapa):** O que eu vou percorrer? Uma lista? Um intervalo de números (`range`)?
2. **Parte 2 (O Extrator):** Dê um nome para a variável que vai segurar o valor *daquela volta* (`for item...`).
3. **Parte 3 (A Ação):** O que eu faço com esse `item` agora que o tenho na mão?

### 💡 Quando usar?
O `for` é o "canivete suíço" das repetições. Ele brilha em 4 situações principais:
1. **Iteração (Percorrer):** Ler cada item de uma lista, tupla ou string.
2. **Contagem (Acumuladores):** Contar quantas vezes algo acontece ou somar valores (ex: total do carrinho).
3. **Filtragem (Seleção):** Usar com `if` para pegar só o que serve (ex: só números pares).
4. **Transformação (Mapeamento):** Gerar uma nova lista com valores alterados (ex: converter nomes para maiúsculo).

#### Exemplos Práticos:
```python
# 1. Iteração (Percorrer)
frutas = ['Maçã', 'Banana', 'Uva']
for fruta in frutas:
    print(fruta)

# 2. Contagem (Acumuladores)
numeros = [10, 20, 35, 40]
pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
print(f'Temos {pares} pares.')

# 3. Filtragem (Seleção)
precos = [100, 500, 25, 1000]
caros = []
for p in precos:
    if p > 200:
        caros.append(p)
print(caros) # [500, 1000]

# 4. Transformação (Mapeamento)
nomes = ['andre', 'maria']
maiusculos = []
for nome in nomes:
    maiusculos.append(nome.upper())
print(maiusculos) # ['ANDRE', 'MARIA']
```

### 💼 Cenário Real (Dev Junior / Estágio)
- **Processamento em Lote:** Enviar um e-mail de "Feliz Natal" para uma lista de 5.000 clientes (`for cliente in lista_clientes:`).
- **Renderização de Telas:** Exibir uma tabela de produtos no Front-end ou gerar um relatório PDF com várias linhas.
- **Data Science:** Percorrer colunas de uma planilha Excel ou CSV para limpar dados.

---

## 3. Laços de Repetição: `while`

### 💀 Esqueleto
```python
while condicao_for_verdadeira:
    # Executa o bloco
    # IMPORTANTE: Deve haver algo aqui que mude a condição ou um break
```

### 🧩 Como Pensar por Partes?
1. **Parte 1 (Preparação):** Crie variáveis fora do loop (contadores, somadores, flags). *Ex: `soma = 0`*
2. **Parte 2 (A Porta):** Defina a condição de entrada. *Ex: `while True:` ou `while c < 10:`*
3. **Parte 3 (A Coleta/Ação):** Dentro do loop, peça dados (`input`) ou faça a conta.
4. **Parte 4 (O Freio):** Garanta que o loop vai parar! *Ex: `if n == 999: break` ou `c += 1`*

### 💡 Quando usar?

### 💼 Cenário Real (Dev Junior / Estágio)
- **Menus de Console:** Manter o programa rodando até o usuário escolher "Sair".
- **Aguardar Resposta (Polling):** Tentar conectar ao banco de dados; se falhar, esperar 5 segundos e tentar de novo (`while not conectado:`).
- **Workers/Serviços:** Um script que fica rodando infinitamente (`while True:`) processando pedidos de uma fila (ex: fila de impressão ou fila de envio de e-mails).

---

## 3.1. Os Três Padrões de Ouro do While

### A. Validação / Menus (`while True`)
**Cenário:** Você precisa ler o dado *antes* de saber se ele serve.
**Lógica:** "Atirar primeiro, perguntar depois". O loop é infinito e o `break` é o porteiro interno.
```python
while True:
    sexo = input('Sexo [M/F]: ').upper()
    if sexo in 'MF':
        break # O Porteiro libera a saída
    print('Inválido!')
```

### B. Matemático (`while c < 10`)
**Cenário:** Você controla o início e o fim com números (contadores).
**Lógica:** O "Segurança" barra a entrada se o limite estourou.
```python
c = 0
while c < 10:
    print(c)
    c += 1 # Não esqueça de incrementar!
```

### C. Flag Clássica (`while n != 0`)
**Cenário:** Existe um "número mágico" para sair e você quer testar no topo.
**Lógica:** Exige ler uma vez fora e outra vez dentro (repetição do input).
```python
n = int(input('Número (0 para): ')) # 1. Lê fora
while n != 0:
    print(f'Digitou {n}')
    n = int(input('Número (0 para): ')) # 2. Lê dentro (para a próxima volta)
```

---

## 3.2. Laços Aninhados (While dentro de While)

### 💀 Esqueleto
```python
while condicao_lenta:      # Loop Externo (Pai)
    variavel_rapida = 0    # RESET (Importante!)
    while condicao_rapida: # Loop Interno (Filho)
        # Executa várias vezes
        variavel_rapida += 1
    variavel_lenta += 1    # Avança o Pai
```

### 🧩 Como Pensar por Partes? (Metáfora do Relógio)
1. **Parte 1 (O Ponteiro de Horas - Externo):** Define o ciclo maior. Ele anda devagar.
2. **Parte 2 (O Reset - O Segredo):** Antes de entrar no loop interno, você **precisa** resetar a variável de controle dele. Se o relógio marca 13h, o ponteiro de minutos tem que voltar pro 0 para contar até 60 de novo.
3. **Parte 3 (O Ponteiro de Minutos - Interno):** Roda o ciclo completo dele (ex: 0 a 59) para cada **um** passo do externo.

### 💼 Cenário Real (Dev Junior / Estágio)
- **Matrizes/Grids:** Percorrer linhas e colunas de uma planilha ou imagem (pixels).
- **Relatórios Agrupados:** Para cada *Departamento* (Externo), listar todos os *Funcionários* (Interno).

---

## 3.3. Contadores, Acumuladores e Listas (O Kit de Sobrevivência)

Dentro dos loops, você quase sempre vai precisar guardar dados. Aqui está a diferença entre os três tipos principais de "memória":

### A. Contador (`cont += 1`)
**Objetivo:** Contar a **quantidade** de ocorrências.
*Lógica:* "Mais um pra conta".

### B. Acumulador (`soma += valor`)
**Objetivo:** Somar os **valores** (dinheiro, peso, notas).
*Lógica:* "Joga na pilha do total".

### C. Lista Histórica (`lista.append(valor)`)
**Objetivo:** Guardar **quais** foram os valores para mostrar no final.
*Passo 1:* Crie uma lista vazia fora do loop (`lista = []`).
*Passo 2:* Dentro do loop, use `.append()` para guardar o dado (`lista.append(dado)`).

### 💀 Exemplo Prático (Moedas)
```python
# 1. Inicialização (Fora do Loop)
qtd_moedas = 0      # Contador
valor_total = 0     # Acumulador
todas_moedas = []   # Lista para guardar o histórico

while valor_total < 10:
    # 2. Entrada
    moeda = float(input('Valor da moeda: '))
    
    # 3. Processamento
    qtd_moedas += 1              # Conta +1 (Quantidade)
    valor_total += moeda         # Soma o valor (Acumulador)
    todas_moedas.append(moeda)   # Guarda na lista (Histórico)

# 4. Saída
print(f'Quantidade: {qtd_moedas}')
print(f'Total: {valor_total}')
print(f'Extrato: {todas_moedas}') # Mostra [0.5, 1.0, 0.25...]
```

---

## 4. Controle de Fluxo (`break` e `continue`)

### 💀 Esqueleto
```python
while True:
    if condicao_de_parada:
        break  # Mata o loop imediatamente
    
    if condicao_de_pulo:
        continue  # Pula essa volta e vai para a próxima
```

### 💼 Cenário Real (Dev Junior / Estágio)
- **Break:** Busca em lista. Se você procura o usuário "André" em uma lista de 1 milhão de nomes e o encontra na posição 10, você dá um `break`. Não faz sentido continuar procurando nos outros 999.990. Economiza processamento.
- **Continue:** Processamento de dados. Imagine processar uma lista de pagamentos. Se o pagamento estiver "Cancelado", você dá um `continue` para ignorar ele e ir para o próximo, sem rodar o resto da lógica pesada.

---

## 5. Funções (`def`)

### 💀 Esqueleto
```python
def nome_da_funcao(parametro1, parametro2):
    # Processamento
    resultado = parametro1 + parametro2
    return resultado

# Como chamar:
valor = nome_da_funcao(10, 20)
```

### 💡 Quando usar?
- **Lógica:** Organização, Reutilização e Legibilidade. Princípio **DRY** (Don't Repeat Yourself - Não se repita).
- **Exemplo Acadêmico:** Função para calcular área, função para mostrar uma linha na tela.

### 💼 Cenário Real (Dev Junior / Estágio)
- **Regras de Negócio:** Uma função `calcular_imposto(valor)` que é usada tanto na tela de vendas quanto na tela de relatórios. Se a lei mudar, você altera só em um lugar.
- **Conexões:** Uma função `conectar_banco()` que encapsula a complexidade de senhas e IPs.
- **APIs:** No Backend (Flask/Django/FastAPI), cada "rota" (URL) do site geralmente é ligada a uma função. Ex: `def listar_usuarios():`.

---

## 6. Manipulação de Strings (f-strings)

### 💀 Esqueleto
```python
nome = "André"
salario = 2500.50

# Formatação moderna
print(f"O funcionário {nome} ganha R${salario:.2f}")
```

### 💼 Cenário Real (Dev Junior / Estágio)
- **Logs:** Gerar mensagens de erro claras para o sistema. Ex: `print(f"[ERRO] Falha ao conectar no IP {ip_servidor} às {hora_atual}")`.
- **SQL Dinâmico (Cuidado):** Montar queries simples (embora ORMs sejam preferidos para evitar injeção de SQL).
- **Geração de Mensagens:** Criar textos personalizados para notificações de usuário.

---

## 7. Tuplas e Listas (Estruturas de Dados Básicas)

### 💀 Esqueleto
```python
lista = [1, 2, 3]  # Mutável (Pode mudar)
tupla = (1, 2, 3)  # Imutável (Não pode mudar)

lista.append(4)    # Adiciona
lista.pop()        # Remove o último
```

### 💼 Cenário Real (Dev Junior / Estágio)
- **Listas:** Quase tudo! Lista de produtos do carrinho de compras, lista de comentários de um post, lista de tarefas.
- **Tuplas:** Configurações fixas do sistema (ex: dias da semana, coordenadas GPS de uma loja, configurações de banco de dados que não devem ser alteradas durante a execução).

---

## 🧠 Resumo: Como escolher?

| Pergunta | Use... |
| :--- | :--- |
| "Preciso tomar uma decisão?" | **if / elif / else** |
| "Sei quantas vezes vou repetir?" | **for** |
| "Tenho uma lista de coisas para processar?" | **for** |
| "Não sei quando vai parar (depende de algo)?" | **while** |
| "Vou usar esse código em mais de um lugar?" | **def** (Função) |
| "O código está ficando muito grande e confuso?" | **def** (Quebre em funções menores) |
| "Preciso formatar texto com variáveis?" | **f-string** |

---
*Este documento é vivo. Adicione novas estruturas (Dicionários, Classes, Try/Except) conforme avançar nos estudos.*

## 🚀 Como ficar "Craque"? (Estratégia de Treino)

Para sair do "entendi a teoria" para "consigo fazer de olhos fechados":

1. **Não copie, recrie:** Viu a aula? Feche o vídeo e tente fazer o código do zero. Se travar, olhe, feche e tente de novo.
2. **Variações (O "E se?"):** Pegue um exercício pronto e mude a regra.
   - *Ex:* Fez uma tabuada com `for`? Tente fazer com `while`. Tente fazer uma função `tabuada(n)`.
3. **Debug Mental:** Antes de rodar, tente ler seu código linha por linha e prever o que vai acontecer.
4. **Projetos Pessoais:** Crie ferramentas para você.
   - *Ex:* Um script que calcula quantas horas você estudou música na semana.
5. **Explique para o Pato (Rubber Ducking):** Tente explicar em voz alta o que cada linha faz. Se gaguejar, é ali que você precisa estudar mais.