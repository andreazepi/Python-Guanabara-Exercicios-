# 🐍 Aula 22: Módulos e Pacotes

A modularização surgiu para dividir programas grandes e aumentar a legibilidade e facilidade de manutenção do código.

## Conceitos
- **Módulo**: Qualquer arquivo `.py` que contenha funções e variáveis pode ser um módulo.
- **Importação**: 
  - `import uteis`: Importa tudo (acessa via `uteis.funcao()`).
  - `from uteis import funcao`: Importa apenas a função específica.

## Pacotes (Packages)
Quando os módulos começam a ficar numerosos, podemos organizá-los em pastas, criando **pacotes**.
- Estrutura: Pasta com arquivo especial `__init__.py`.
- Permite organizar por assuntos: `pacote.numeros`, `pacote.strings`, `pacote.datas`.

---

## 🎯 Exercícios Propostos (107 ao 112)

### Desafio 107: Exercitando módulos em Python
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

### Desafio 108: Formatando Moedas em Python
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

### Desafio 109: Formatando Moedas em Python
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

### Desafio 110: Reduzindo ainda mais seu programa
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

### Desafio 111: Transformando módulos em pacotes
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

### Desafio 112: Entrada de dados monetários
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
