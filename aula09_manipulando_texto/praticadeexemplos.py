frase = "Curso em Video Python"

print("--- 1. FATIAMENTO (Cortando a string) ---")
# Pega do índice 9 até o 13 (14 é excluído) -> 'Video'
print(f"frase[9:14]: {frase[9:14]}") 
# Pega do início até o 5 -> 'Curso'
print(f"frase[:5]: {frase[:5]}")    
# Pega do 15 até o final -> 'Python'
print(f"frase[15:]: {frase[15:]}")   
# Pega do 9 ao 21 pulando de 2 em 2 -> 'VdoPto'
print(f"frase[9:21:2]: {frase[9:21:2]}") 

print("\n--- 2. ANÁLISE (Examinando a string) ---")
print(f"Tamanho da frase: {len(frase)}")
print(f"Quantas vezes aparece a letra 'o': {frase.count('o')}")
print(f"Em que posição começa 'deo': {frase.find('deo')}")
print(f"A palavra 'Android' existe na frase? {'Android' in frase}")

print("\n--- 3. TRANSFORMAÇÃO (Mudando a string) ---")
print(f"Substituindo: {frase.replace('Python', 'Android')}")
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")
print(f"Capitalizada: {frase.capitalize()}")
print(f"Título: {frase.title()}")

print("\n--- REMOVENDO ESPAÇOS ---")
frase_suja = "   Aprenda Python  "
print(f"Original: '{frase_suja}'")
print(f"Sem espaços (strip): '{frase_suja.strip()}'")

print("\n--- 4. DIVISÃO E JUNÇÃO ---")
lista = frase.split()
print(f"Dividido (lista): {lista}")
print(f"Pegando só a primeira palavra da lista: {lista[0]}")
print(f"Juntando com traços: {'-'.join(lista)}")

# --- DESAFIO PARA VOCÊ ---
# Tente criar um código abaixo que peça o nome de uma cidade (input)
# e diga se ela começa com a palavra "SANTO" (independente de maiúsculas/minúsculas).

# Gabarito (Tire os comentários para testar):
# cidade = input("Em que cidade você nasceu? ").strip()
# print(cidade[:5].upper() == "SANTO")