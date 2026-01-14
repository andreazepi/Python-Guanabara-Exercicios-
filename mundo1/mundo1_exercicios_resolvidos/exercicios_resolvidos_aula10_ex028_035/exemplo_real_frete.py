# Exemplo Real: Sistema de E-commerce escolhendo a melhor transportadora
# O sistema recebe cotações de 3 empresas e precisa decidir qual mostrar para o cliente como "Melhor Preço".

print("--- SISTEMA DE COTAÇÃO DE FRETE ---")

# Entradas (simulando o cálculo que o sistema faria internamente)
preco_correios = float(input("Cotação Correios: R$ "))
preco_jadlog = float(input("Cotação Jadlog: R$ "))
preco_azul = float(input("Cotação Azul Cargo: R$ "))

# Lógica Otimizada com Dicionários (Mundo 3)
cotacoes = {
    "Correios": preco_correios,
    "Jadlog": preco_jadlog,
    "Azul Cargo": preco_azul
}

# Ordenando os itens do dicionário pelo preço
# sorted() cria uma lista ordenada. O comando 'key=lambda item: item[1]' diz para ordenar pelo PREÇO (item[1])
ranking = sorted(cotacoes.items(), key=lambda item: item[1])

print("-" * 30)
print("--- Ranking de Fretes (Do mais barato para o mais caro) ---")
for transportadora, preco in ranking:
    print(f"{transportadora}: R$ {preco:.2f}")

print("-" * 30)
# Como a lista 'ranking' já está ordenada, o índice [0] é o menor e o [-1] é o maior (último)
print(f"Menor valor: {ranking[0][0]} (R$ {ranking[0][1]:.2f})")
print(f"Maior valor: {ranking[-1][0]} (R$ {ranking[-1][1]:.2f})")