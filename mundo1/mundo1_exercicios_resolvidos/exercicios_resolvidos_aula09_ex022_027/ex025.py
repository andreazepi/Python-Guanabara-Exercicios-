# ## Desafio 025
# - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o nome de uma pessoa: ').strip()
frase = nome.upper()

print(f"A palavra 'SILVA' existe na frase? {'SILVA' in frase}")

# Solução alternativa usando if/else
nome = input('Digite o nome de uma pessoa: ').strip().upper()
if 'SILVA' in nome:
    print('O nome contém SILVA.')
else:
    print('O nome não contém SILVA.')