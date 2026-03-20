# 🐍 Aula 23: Tratamento de Erros e Exceções

Nesta aula aprendemos como tratar falhas que podem ocorrer durante a execução do programa, evitando que ele pare abruptamente.

## Estrutura Try ... Except

```python
try:
    # Operação (bloco onde o erro pode ocorrer)
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    # Falhou (o que fazer se der erro específico)
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except Exception as erro:
    # Erro genérico
    print(f'O erro encontrado foi {erro.__class__}')
else:
    # Deu certo (executa se não ocorrer erro)
    print(f'O resultado é {r:.1f}')
finally:
    # Certo/Falha (executa sempre, independente do que acontecer)
    print('Volte sempre! Muito obrigado.')
```

---

## 🎯 Exercícios Propostos (113 ao 115)

### Desafio 113: Funções aprofundadas em Python
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

### Desafio 114: Site está acessível?
Crie um código em Python que teste se o site pudim.com.br está acessível pelo computador usado.

### Desafio 115: Criando um menu e arquivos
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.