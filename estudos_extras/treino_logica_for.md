# 🧠 Plano de Destravamento: Dominando o "Meio" do Loop

**O Problema:** Você sabe começar (Input) e terminar (Print), mas trava no processamento.
**A Solução:** Exercícios focados exclusivamente em **Acumuladores** e **Condicionais** dentro do `for`.

---

## 🛠️ A Técnica do "Sanduíche"
Sempre que travar, desenhe o problema assim:

1.  **Pão de Cima (Antes do Loop):** O que eu preciso responder no final?
    *   "Quantos?" -> Crie `cont = 0`
    *   "Soma?" -> Crie `soma = 0`
    *   "Maior?" -> Crie `maior = 0`
2.  **Recheio (Dentro do Loop):** A cada volta, o que eu faço com o dado novo?
    *   "É o que eu quero?" -> Use `if`.
    *   "Se sim, guarda/soma" -> `cont += 1` ou `soma += valor`.
3.  **Pão de Baixo (Depois do Loop):** Mostre as variáveis que você criou no passo 1.

---

## 🏋️ Lista de Exercícios Progressivos (Faça um por dia)

### Nível 1: O Acumulador Simples
**Objetivo:** Ler 6 números inteiros e mostrar a soma apenas dos que forem **pares**.
*Dica:* Use `if num % 2 == 0:` para filtrar e `soma += num` para acumular.

### Nível 2: O Contador Seletivo (Vogais)
**Objetivo:** Ler uma frase (string) e dizer quantas vogais (a, e, i, o, u) ela tem.
*Dica:* Strings também funcionam no for! `for letra in frase:`. Use `if letra in 'aeiou':`.

### Nível 3: O Espelho Numérico
**Objetivo:** Ler 5 números. No final, mostrar quantos foram maiores que 10 e quantos foram menores que 5.
*Dica:* Você vai precisar de duas variáveis contadoras (`maior10 = 0`, `menor5 = 0`).

### Nível 4: A Busca Específica
**Objetivo:** Ler o peso de 5 pessoas. No final, mostrar a média de peso, mas **apenas das pessoas com mais de 80kg**.
*Dica:* Você precisa somar o peso (`soma_gordos`) e contar quantas pessoas (`cont_gordos`) entraram no `if`. A média será `soma / cont`.

### Nível 5: O Desafio do "Break"
**Objetivo:** Ler nomes de pessoas infinitamente. Se a pessoa digitar "sair", o programa para. (Isso já é um pré-treino para o `while`).
*Dica:* Use `if nome == 'sair': break`.

---

## 💡 Dica de Ouro para quando travar
Não tente escrever o código direto. Escreva em português (pseudocódigo) no papel:

> "Para cada pessoa de 1 a 5:"
> "   Peço a idade."
> "   SE a idade for maior que 18:"
> "       Adiciono +1 no meu contador."
> "Mostro o contador."

Se você consegue escrever isso, você consegue escrever o código. A sintaxe é só tradução.