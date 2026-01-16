# Desafio 049
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço `for`.

tabuada = int(input('Digite um número para ver sua tabuada de Multiplicação: '))

for numero_tabuada in range(1, 11):
    print('-' * 12)
    print(f'{tabuada} x {numero_tabuada:2} = {tabuada*numero_tabuada}')
print('-' * 12)
    
