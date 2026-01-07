# Desafio 007
# Aula 7
# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {media:.1f}.')

'''
:.1f
lembrando, este comando é utilizado para nao aparecer muitos números flutuantes no valor da variavel no resultado final,
ou seja, 1f é apenas para aparecer uma casa decimal após o ponto.

E lembre-se da ordem de precedencia!!!
'''
