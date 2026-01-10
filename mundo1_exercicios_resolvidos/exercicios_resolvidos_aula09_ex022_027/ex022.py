# Desafio 022
# - Crie um programa que leia o nome completo de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas e minúsculas.
#   - Quantas letras ao todo (sem considerar espaços).
#   - Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
print(f"Nome em maiúsculas: {nome.upper()}")
print(f"Nome em minúsculas: {nome.lower()}")
print(f"Quantidade de letras: {len(nome) - nome.count(' ')}")
print(f"Quantidade de letras do primeiro nome: {nome.find(' ')}") if ' ' in nome else print(f"Quantidade de letras do primeiro nome: {len(nome)}")

# Explicação da lógica acima (Operador Ternário):
# O .find(' ') procura o primeiro espaço. Se o nome for "Ana Silva", o espaço está no índice 3, indicando que "Ana" tem 3 letras.
# Se o usuário digitar só "Ana", não há espaços, e o .find() retornaria -1 (erro de lógica).
# O if resolve isso: Se houver espaço (' ' in nome), usa o .find(). Se não (else), usa o len(nome) para pegar o tamanho total.

# Alternativa para a última linha:
# primeiro_nome = nome.split()[0]
# print(f"Quantidade de letras do primeiro nome: {len(primeiro_nome)}")



# Funções úteis usadas:
# .strip() - Remove os espaços extras no início e no final da string.
# .upper() - Converte todas as letras para maiúsculas.
# .lower() - Converte todas as letras para minúsculas.
# .count() - Conta quantas vezes um caractere ou substring aparece na string.
# .find() - Retorna o índice da primeira ocorrência de uma substring na string.
# len() - Retorna o comprimento (número de caracteres) da string.
# .split() - Divide a string em uma lista de substrings com base em um delimitador (por padrão, espaços).