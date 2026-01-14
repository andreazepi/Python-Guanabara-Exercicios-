# Desafio 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centrimentros e milimetros.

medida = float(input('Digite uma distância em metros: '))

cm = medida * 100
mm = medida * 1000

# extra das aulas, fazer também com quilômetros, hectômetro, decâmetro, metro, decímetro, centimetro, milímetro

km = medida / 1000 
hm = medida / 100 
dam = medida / 10
dm = medida * 10



print(f'A medida de {medida}m corresponde a {cm:.01f}cm e {mm:.01f}mm.')