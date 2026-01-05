# Exercicio 11
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tintas necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Qual é a largura da parede em metros: '))
altura = float(input('Qual é a altura da parede em metros: '))

area = largura * altura

print(f'Sua parede tem dimensão de {largura:.0f} x {altura:.0f}, e sua área total é de {area:.1f}m².')

tinta = area / 2 # Cada litro pinta 2m²
                #  :.0f lembrando que isso é utilizado para colocar quantas casas decimais deve ter depois do numero inteiro

print(f'Pra pintar essa parede, você precisará de {tinta:.0f}l de tinta.')

