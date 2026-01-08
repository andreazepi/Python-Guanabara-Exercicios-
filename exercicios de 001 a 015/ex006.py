# Desafio 006 - Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
# Aula 7 

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2) #ou usar 0.5 em vez do (1/2) para raiz quadrada
# também pode-se usar o math.sqrt(n), a pessoa saberá que essa é a formula pra raiz quadrada. 

# print(f'Analisando o valor {n}, o dobro é {d}, o triplo é {t} e a raiz quadra de {n} é {r}.')
# ou poderia usar o \n para quebrar as linhas e deixar tudo uma abaixo da outra a resposta.
        
print(f'Analisando o valor {n}:')
print(f'O dobro é {d}.')
print(f'O triplo é {t}.')
print(f'E a raiz quadra é {r}.')
