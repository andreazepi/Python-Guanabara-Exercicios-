# ## Desafio 027
# - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input("Digite seu nome completo: ").strip()
nomes = nome.split()
print(f'Seu primeiro nome é: {nomes[0]}')
print(f'Seu último nome é: {nomes[-1]}') #neste caso utilizamos o índice -1 para pegar o último elemento da lista.


# .split() -> divide a string em uma lista de palavras
# .strip() -> remove espaços em branco no início e no final da string