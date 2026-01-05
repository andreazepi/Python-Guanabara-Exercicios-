#Opção 1
# Observação: Opção 1 não realiza soma numérica; apenas concatena as entradas (strings) porque não usa int() para converter.
n1 = input("Digite um valor: ")
n2 = input("Digite outro valor: ")
s = n1 + n2
print("A soma entre", n1, "e", n2, "é igual a", s)

#Opção 2
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))