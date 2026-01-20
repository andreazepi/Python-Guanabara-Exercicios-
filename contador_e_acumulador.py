# Analisador de Dados:
# Idade de varias pessoas
# para cada pessoa, pergunte se quer continuar (s/n)
# no final, mostre quantas pessoas tem +18 (contador
# qual a média de idade do grupo (soma de todas as idades dividida pelo total de pessoas.)

total_idade = 0           # Acumulador 
total_pessoas = 0         # Contador
total_18 = 0              # Contador 

while True:                                                      
    idade = int(input('Digite a idade: '))
    total_pessoas += 1  # contador
    total_idade += idade  # acumulador

    if idade >= 18:    
        total_18 += 1   # contador

    continuar = str(input('Quer continuar [S/N]? ')).upper()
    if continuar == 'N':
        break
media = total_idade / total_pessoas
print(f'Total de pessoas com mais de 18 anos: {total_18}')
print(f'Média de idade do grupo: {media}')
print(f'Total de pessoas cadastradas: {total_pessoas}')
