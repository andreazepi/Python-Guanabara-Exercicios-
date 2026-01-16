# Desafio 048
# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0  # Acumulador
cont = 0  # Contador (opcional, mas ajuda a verificar)
for numero_impar in range(1, 501, 2):     # aqui, ele pula de dois em dois, que são os números impares
    if numero_impar % 3 == 0: 
        print(numero_impar, end=' ')
        cont += 1
        soma += numero_impar
print(f'A soma de todos os {cont} valores solicitados é {soma}')
            
        
        
        
        
        
        
        
