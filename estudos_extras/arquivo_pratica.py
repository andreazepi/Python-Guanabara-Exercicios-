# Variáveis acumuladoras (DEVEM ser criadas FORA do loop)
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    # 1. Lógica da Média (Soma tudo agora, divide no final)
    soma_idade += idade
    
    # 2. Lógica do Homem Mais Velho
    if p == 1 and sexo == 'M': # Se for a 1ª pessoa E for homem
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem: # Se for homem E for mais velho que o atual recordista
        maior_idade_homem = idade
        nome_velho = nome

    # 3. Lógica das Mulheres < 20
    if sexo == 'F' and idade < 20:
        tot_mulher20 += 1

media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {tot_mulher20} mulheres com menos de 20 anos.')