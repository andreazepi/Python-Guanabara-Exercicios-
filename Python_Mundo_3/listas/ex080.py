# Desafio 080: Lista ordenada sem repetições
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(1, 6):
    valores = int(input(f'Digite o {i}º Valor: '))
    
    if valores in lista:
            print(f'O número {valores} já existe e não será adicionado na lista.')

    elif i == 1 or valores > lista[-1]:
        lista.append(valores)
        print('Adicinado ao final da lista...')
        
    
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                lista.insert(pos, valores)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')