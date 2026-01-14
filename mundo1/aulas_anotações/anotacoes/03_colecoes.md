# 📦 Coleções de Dados
Variáveis compostas que armazenam múltiplos valores.

| Tipo | Símbolo | Mutável? | Ordenado? | Descrição |
| --- | --- | --- | --- | --- |
| **Tupla** | `()` | ❌ Não | ✅ Sim | Lista fixa, não pode ser alterada após criada. |
| **Lista** | `[]` | ✅ Sim | ✅ Sim | Pode adicionar, remover e alterar itens. |
| **Dicionário** | `{}` | ✅ Sim | ❌ Não | Guarda pares de `chave: valor`. |

### Exemplos:

```python
# Tupla
lanche = ("Hambúrguer", "Suco")
# lanche[0] = "Pizza" -> ERRO! Tuplas são imutáveis.

# Lista
compras = ["Arroz", "Feijão"]
compras.append("Carne") # Adiciona item
compras[0] = "Macarrão" # Altera item

# Dicionário
pessoa = {"nome": "Gustavo", "idade": 25}
print(pessoa["nome"])
```