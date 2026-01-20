# Desafio 057: Validação de Dados
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite seu sexo[M/F]: ').strip().upper()[0]   # [0] isso é pra pegar só a primeira letra

while sexo not in '[Mm/Ff]':
    print('DADOS INVALIDOS! Por favor, digite seu sexo[M/F]: ')
    sexo = input('Digite seu sexo[M/F]: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')

