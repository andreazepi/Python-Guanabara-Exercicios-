#n1 = input('Digite um valor: ')
#print(type(n1))

#Isso é para descobrir o tipo primitivo de uma variável.
#No caso, o valor digitado é sempre considerado uma string (str).       

#Ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

tipo = input('Digite algo: ')
res = [
    ("Tipo primitivo", type(tipo).__name__),
    ("Só tem espaços?", tipo.isspace()),
    ("É um número?", tipo.isnumeric()),
    ("É alfabético?", tipo.isalpha()),
    ("É alfanumérico?", tipo.isalnum()),
    ("Está em maiúsculas?", tipo.isupper()),
    ("Está em minúsculas?", tipo.islower()),
    ("Está capitalizada?", tipo.istitle())
]

# Imprime a lista de tuplas
print(res)

# Impressão formatada (mais legível)
print("\nSaída formatada:")
for label, value in res:
    print(f"{label}: {value}")

#O comando isnumeric() serve para identificar se o valor digitado é um número.
#O comando isalpha() serve para identificar se o valor digitado é uma letra.
#O comando isalnum() serve para identificar se o valor digitado é uma letra ou número.
#O comando isupper() serve para identificar se o valor digitado está em maiúsculas
#O comando islower() serve para identificar se o valor digitado está em minúsculas
#O comando istitle() serve para identificar se o valor digitado está capitalizado. Ex
#exemplo: "Curso em Vídeo" (Cada palavra começa com letra maiúscula)
#O comando isspace() serve para identificar se o valor digitado só tem espaços.

