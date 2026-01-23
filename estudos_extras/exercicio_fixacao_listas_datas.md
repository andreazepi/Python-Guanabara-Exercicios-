# 🗂️ Treino de Fixação: Listas, Datas e Classificação

**O Diagnóstico:** Você já sabe fazer loops, mas precisa fixar como **guardar** os resultados filtrados para usar depois (Listas) e como lidar com o **tempo** (Datas).

---

## 📝 A Estrutura Chave (O "Esqueleto")
Este exercício combina 3 ferramentas essenciais do dia a dia.

### 1. O Setup (Antes do Loop)
- **Importar Data:** `from datetime import date`
- **Pegar Ano Atual:** `ano = date.today().year`
- **Criar Listas Vazias:** `lista = []` (Sempre **fora** do loop, senão ela zera a cada volta!).

### 2. A Ação (Dentro do Loop)
- **Calcular:** `idade = ano_atual - nascimento`
- **Verificar:** `if idade >= 21:`
- **Guardar (O Pulo do Gato):** `lista.append(valor)`
  - *Nota:* O `.append()` não retorna nada, ele apenas executa a ação de guardar. Não faça `lista = lista.append()`.

---

## 💻 Código de Referência (Sua Solução Limpa)

```python
from datetime import date 

ano_atual = date.today().year
maiores = [] # Lista A
menores = [] # Lista B

for c in range(1, 8):
    nasc = int(input(f'Ano da {c}ª pessoa: '))
    idade = ano_atual - nasc
    
    if idade >= 21:
        maiores.append(nasc) # Guarda na Lista A
    else:
        menores.append(nasc) # Guarda na Lista B

print(f'Temos {len(maiores)} maiores: {maiores}')
print(f'Temos {len(menores)} menores: {menores}')
```

---

## 💡 Dicas de Ouro para Revisão
1. **`len(lista)`:** Se precisar saber *quantas* pessoas tem na lista, use `len()`. Não precisa criar uma variável `cont = 0` separada.
2. **Listas são Mutáveis:** Quando você dá `append`, você está alterando a lista original na memória.
```