# Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Python já tem função pra calculo de conversão, neste caso, será: \n bin(), oct() e hex().

numero = int(input('Digite um número para qual voce quer fazer uma conversão: '))

print('-'*40)
print("Para calcular uma conversão...")
print('Digite 1: Para calculo de binario')
print('Digite 2: Para calcuo de octal')
print('Digite 3: Para calculo de hexadecimal')
print('-'*40)

# ou opção guanabara: 
# print('''Escolha uma das bases para conversão:
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL''')


base_conversao = int(input('Sua opção: '))

# Foi utilizado o fatiamento [2:] para remover os prefixos (0b, 0o, 0x) que o Python insere automaticamente nas conversões.
if base_conversao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif base_conversao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif base_conversao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.') # isso é pra caso o usuário digite um numero diferente de 1, 2 ou 3.

    
# Indicação do Bernardo, usar Switch case, pra Python é a estrutura Match Case.

def switch_match_case(base_conversao, numero):
    match base_conversao:
        case 1:
            return f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}'
        case 2:
            return f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}'
        case 3:
            return f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}'
        case _:
            return 'Opção inválida. Tente novamente.'

print(switch_match_case(base_conversao, numero))










