# 🏋️ Treino de Fixação: Maior e Menor (Lógica vs Ferramentas)

**O Diagnóstico:** Você precisa entender a diferença entre resolver um problema usando **Lógica de Programação** (universal) e usando **Ferramentas do Python** (produtividade).

---

## 🥊 Round 1: Modo Raiz (Lógica Pura)
**Quando usar:** Em entrevistas de emprego (testes de lógica), em linguagens de baixo nível (C, Assembly) ou quando a memória é pouca e você não pode guardar uma lista gigante.

**A Lógica do "Rei da Montanha":**
1. O primeiro número que chega é automaticamente o Maior e o Menor (pois não tem com quem comparar).
2. Os próximos números tentam "derrubar" o recordista atual.

```python
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    
    if i == 1:
        # O primeiro é o recordista inicial
        maior = peso
        menor = peso
    else:
        # Os outros tentam superar o recorde
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior: {maior} | Menor: {menor}')
```

---

## 🥊 Round 2: Modo Pythonico (Listas)
**Quando usar:** No dia a dia de trabalho. É mais legível, mais rápido de escrever e menos propenso a bugs.

**A Lógica do "Acumular e Analisar":**
1. Joga tudo dentro de uma caixa (Lista).
2. No final, pede para o Python achar o extremo.

```python
pesos = [] # A caixa vazia

for i in range(1, 6):
    p = float(input(f'Peso da {i}ª pessoa: '))
    pesos.append(p) # Guarda na caixa

# Funções Mágicas (Built-in)
print(f'Maior: {max(pesos)}')
print(f'Menor: {min(pesos)}')
```

---

## 💡 Qual escolher?
- **Para aprender Lógica:** Use o Modo Raiz. Ele treina seu cérebro para entender *como* o computador compara coisas.
- **Para trabalhar:** Use o Modo Pythonico. `max()` e `min()` são otimizados e mais rápidos.