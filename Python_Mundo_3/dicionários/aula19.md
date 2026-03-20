# 🐍 Aula 19: Dicionários

Os dicionários são estruturas de dados semelhantes às listas e tuplas, mas permitem índices literais (personalizados), chamados de **chaves** (keys).

## Características Principais
- **Sintaxe**: Utilizam chaves `{}`. Ex: `dados = {'nome': 'Pedro', 'idade': 25}`.
- **Estrutura**: Composto por `chave: valor`.
- **Acesso**: `print(dados['nome'])` retorna 'Pedro'.
- **Métodos Importantes**:
  - `.values()`: Retorna os valores (Ex: Pedro, 25).
  - `.keys()`: Retorna as chaves (Ex: nome, idade).
  - `.items()`: Retorna ambos (chave e valor).
  - `.copy()`: Método para copiar dicionários (evita ligação direta).

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