# Desafio 047
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


from time import sleep   # biblioteca pra esperar

for numero_par in range(51, 1, -1):
       if numero_par % 2 == 0:
        print(numero_par, end=' ')      # end=' ' é para colocar os numero na mesma linha
print('Acabou')












