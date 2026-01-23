# 🎯 Treino de Fixação: Números Primos

**Por que praticar isso?**
Este exercício é fundamental porque ensina o conceito de **"Força Bruta"** (testar todas as possibilidades) e o uso de **Contadores** dentro de condições.

---

Com certeza! Números Primos são um dos conceitos mais importantes para treinar lógica de repetição (for) e condicionais (if).

Criei o arquivo exercicio_fixacao_primos.md para você praticar, seguindo o mesmo modelo do anterior.

🧠 A Lógica dos Números Primos
O Conceito Matemático: Um número é PRIMO se ele for divisível apenas por 1 e por ele mesmo.

Exemplo: O número 5 é primo?
5 ÷ 1 = 5 (Resto 0) ✅
5 ÷ 2 = 2.5 (Resto 1) ❌
5 ÷ 3 = 1.6 (Resto 2) ❌
5 ÷ 4 = 1.2 (Resto 1) ❌
5 ÷ 5 = 1 (Resto 0) ✅
Total de divisores: 2. Logo, é Primo.
Como traduzir isso para Python? Precisamos testar a divisão do número por todos os antecessores dele (de 1 até ele mesmo).

Criamos um contador (tot = 0).
Fazemos um laço for de 1 até o número.
Se o resto da divisão for 0 (if num % c == 0), aumentamos o contador.
No final, se o contador for igual a 2 (if tot == 2), ele é primo



## 📝 O Desafio
**Enunciado:** Crie um programa que leia um número inteiro e diga se ele é ou não um número primo.

### 🥋 Nível 1: O Contador de Divisores (Estilo Guanabara)
*Objetivo:* Entender a lógica básica.
- Use um `for` que vá de 1 até o número digitado.
- Dentro do loop, verifique se a divisão é exata (`if num % c == 0`).
- Se for, aumente um contador (`tot += 1`).
- No final, se `tot == 2`, é primo.

### 🥋 Nível 2: Otimização Visual (Cores)
*Objetivo:* Aprender a dar feedback visual.
- Use códigos de cores ANSI (ex: `\033[33m`).
- Se o número for divisível, mostre ele em Amarelo.
- Se não for, mostre em Vermelho.

### 🥋 Nível 3: Otimização de Performance (Break)
*Objetivo:* Pensar como um computador (economizar processamento).
- Um número par maior que 2 nunca é primo. Você pode eliminar isso logo de cara?
- Se você encontrar *qualquer* divisor entre 2 e o número anterior, você já sabe que **não** é primo. Precisa continuar testando até o final?
- Tente usar o comando `break` para parar o loop assim que descobrir que não é primo.

---

## 💡 Dicas de Ouro
1. **O Loop:** Lembre-se que o `range(1, n)` vai até `n-1`. Para ir até o número, use `range(1, n + 1)`.
2. **O Resto:** O operador `%` (módulo) é seu melhor amigo aqui. `5 % 2` sobra 1 (não divisível). `4 % 2` sobra 0 (divisível).

---

## 🧪 Espaço para Prática

```python
# Tente implementar aqui:
num = int(input('Número: '))
tot = 0
# ... continue
```

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

numero = int(input('Digite um numero inteiro: '))
tot = 0 # Variável para contar quantos divisores achamos

# Vamos de 1 até o número (numero + 1 para incluir o próprio número)
for c in range(1, numero + 1): 
    if numero % c == 0:
        tot += 1 # Achou um divisor! Conta mais um.

if tot == 2:
    print(f'O número {numero} é PRIMO!')
else:
    print(f'O número {numero} NÃO É PRIMO (tem {tot} divisores).')