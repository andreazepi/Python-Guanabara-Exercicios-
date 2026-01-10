# ## Desafio 024
# - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input("Digite o nome de uma cidade: ").strip()
print(cidade.upper().startswith('SANTO'))

# talvez outra maneira de fazer isso e com a função if/else pra dar uma resposta mais amigável:
cidade = input("Digite o nome de uma cidade: ").strip()
cidade = cidade.upper().startswith('SANTO')
if cidade:
     print("A cidade começa com SANTO.")
else:
     print("A cidade não começa com SANTO.")









# .strip() remove espaços em branco no início e no fim da string
# .upper() transforma a string toda em maiúsculas
# .startswith() verifica se a string começa com o valor especificado
# Exemplo de uso:
# cidade = "   Santo André  "
# print(cidade.strip().upper().startswith('SANTO'))  # Isso retornaria True
# Dica: Use os métodos de string vistos na aula para facilitar a resolução do problema.