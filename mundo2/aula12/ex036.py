# Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


# A prestação mensal não pode exceder 30% do salário, senão o empréstimo será negado.
# Lógica simplificada:
# Passo 1 (Definir as variáveis): V = Valor da casa, T = Tempo total em meses (Anos * 12), S = Salário mensal.
# Passo 2 (Calcular a Prestação): P = V / T
# Passo 3 (Verificação): Se P <= (S * 0.30), o empréstimo é aprovado. Caso contrário, é negado.

valor_casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual a sua renda mensal? R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))

prestacao = valor_casa / (anos * 12) # prestação mensal é o valor total que tera que pagar dividido pelo número de meses.
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${valor_casa:.3f} em {anos} anos a prestação será de R${prestacao:.0f}')

if prestacao <= minimo:
   print('Empréstimo pode ser CONCEDIDO!')
else:
   print('Empréstimo NEGADO! Não pode exceder 30% do seu salário.')


# Calculo pessoal: 

valor_automovel = float(input('Qual é o valor do automovel? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = float(input('Em quantos anos voce pretende pagar? '))

prestação_mensal = valor_automovel / (anos * 12)

print(f'Para pagar um automovel de R${valor_automovel:.2f} em {anos:.0f} anos a prestação será de R$ {prestação_mensal:.2f}')

