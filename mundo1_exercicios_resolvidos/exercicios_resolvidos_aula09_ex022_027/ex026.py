# ## Desafio 026
# - Faça um programa que leia uma frase pelo teclado e mostre:
#   - Quantas vezes aparece a letra "A".
#   - Em que posição ela aparece a primeira vez.
#   - Em que posição ela aparece a última vez.


frase = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra "A" aparece na posição {frase.find("A")}')
print(f'A última letra "A" aparece na posição {frase.rfind("A")}')
