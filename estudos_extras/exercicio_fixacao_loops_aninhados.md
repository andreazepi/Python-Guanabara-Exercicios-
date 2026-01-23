# 🔄 Treino de Lógica: Loops Aninhados (O "Inception" do Código)

**O Diagnóstico:** Você entende a sintaxe, mas sente dificuldade em *visualizar* a execução de um loop dentro do outro.
**A Cura:** Exercícios que forçam o cérebro a separar o "Ciclo Grande" (Pai) do "Ciclo Pequeno" (Filho).

---

## 📝 Desafio 1: O Relógio (Visualização)
**Objetivo:** Entender que o loop de dentro roda *várias* vezes para cada *uma* vez do loop de fora.

**Enunciado:** Simule um relógio digital simples.
- O loop de fora conta as **Horas** (de 0 a 3).
- O loop de dentro conta os **Minutos** (de 0 a 5).
- Mostre na tela: `0h:0min`, `0h:1min`... até `3h:5min`.

---

## 📝 Desafio 2: A Tabuada Completa (Matemática Simples)
**Objetivo:** Usar o número do loop de fora (`i`) dentro da conta do loop de dentro (`j`).

**Enunciado:** Mostre as tabuadas do 1 ao 5, uma seguida da outra.
- Loop Externo: `for num in range(1, 6):` (Define qual tabuada é).
- Loop Interno: `for mult in range(1, 11):` (Define o multiplicador).
- Print: `num x mult = resultado`.
- Dica: Use um separador (`print('-'*10)`) entre cada tabuada (no loop externo).

---

## 📝 Desafio 3: O Desenhista (Padrões Visuais)
**Objetivo:** Manipular a quantidade de repetições do loop interno baseada no loop externo.

**Enunciado:** Faça um programa que desenhe um triângulo na tela.
```text
*
**
***
****
*****
```
- Loop Externo: Controla a linha (1 a 5).
- Loop Interno: Imprime o asterisco `*`.
- **O Pulo do Gato:** O loop interno deve ir de 0 até o número da linha atual. Se estou na linha 3, imprimo 3 asteriscos.

---

## 📝 Desafio 4: Números Perfeitos (Lógica Avançada)
**Objetivo:** Similar aos Primos, mas com acumulador.

**Definição:** Um número é perfeito se a soma dos seus divisores (excluindo ele mesmo) for igual a ele.
- Exemplo: **6**. Divisores: 1, 2, 3. Soma: 1 + 2 + 3 = 6. ✅
- Exemplo: **9**. Divisores: 1, 3. Soma: 1 + 3 = 4. ❌

**Enunciado:** Encontre os 4 primeiros números perfeitos (Dica: eles estão entre 1 e 10.000).
- Loop Externo: Testa os números (ex: 1 a 1000).
- Loop Interno: Soma os divisores desse número.
- Condição: Se `soma == numero`, mostre na tela.