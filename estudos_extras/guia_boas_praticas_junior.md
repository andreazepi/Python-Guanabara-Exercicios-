# 🚀 Guia de Sobrevivência do Dev Júnior: Além do Código

Você já está estudando Lógica (Python) e Ferramentas (Git). Mas o que separa um estudante de um profissional contratável são as **"Meta-Skills"** (habilidades sobre como trabalhar).

Aqui está o que você precisa saber para programar melhor e se destacar em entrevistas.

---

## 1. Clean Code (Código Limpo)
**O Princípio:** "Código é feito para humanos lerem, e apenas incidentalmente para máquinas executarem."
**Na Prática:**
- **Nomes de Variáveis:**
  - ❌ Ruim: `n`, `x`, `lista`, `a`
  - ✅ Bom: `numero_tentativas`, `clientes_ativos`, `idade_usuario`
- **Comentários:**
  - Evite comentar o óbvio (`c = c + 1 # Soma 1`).
  - Comente o **PORQUÊ** (`# Adicionamos 1 para compensar o índice 0 da lista`).
- **Padrão PEP 8 (Python):** O Python tem um guia de estilo oficial.
  - Use `snake_case` para variáveis (tudo minúsculo com underline).
  - Espaços ao redor de operadores (`x = 1 + 2`, não `x=1+2`).

---

## 2. A Arte de Pesquisar (Google-fu)
Você vai passar 70% do tempo pesquisando erros. Saber pesquisar é vital.
- **Inglês é Rei:** Pesquisar em inglês traz 10x mais resultados.
  - ❌ "erro python lista fora do indice"
  - ✅ "python list index out of range error"
- **Copie o Erro:** Copie a última linha do erro (Traceback) e cole no Google entre aspas.
- **Sites Confiáveis:** Stack Overflow, Documentação Oficial (python.org), GeeksforGeeks.

---

## 3. Depuração (Debugging)
Pare de tentar adivinhar onde está o erro.
- **O poder do `print()`:** Espalhe prints pelo código para ver os valores das variáveis (`print(f'DEBUG: valor de x é {x}')`).
- **O Debugger do VS Code:** Aprenda a usar as "bolinhas vermelhas" (breakpoints) na lateral do código para pausar a execução e olhar linha por linha. Isso impressiona muito em testes técnicos.

---

## 4. Inglês Instrumental
Você não precisa ser fluente para falar, mas precisa saber **ler**.
- Toda documentação boa é em inglês.
- As mensagens de erro são em inglês.
- **Dica:** Mude o idioma do seu Windows/VS Code para Inglês. Force seu cérebro a acostumar com os termos (`File`, `Save`, `Run`, `Warning`).

---

## 5. Git Sem Medo
Você já sabe `add`, `commit` e `push`. O próximo nível é:
- **Commits Atômicos:** Não faça um commit gigante "Fiz tudo". Faça pequenos: "Corrigi o bug do login", "Adicionei a validação de idade".
- **Mensagens Claras:**
  - ❌ "ajustes"
  - ✅ "fix: corrige erro na soma do carrinho"

---

## 6. Soft Skills (Comportamental)
Muitas vezes o Júnior é contratado pela vontade de aprender, não pelo que já sabe.
- **Saiba pedir ajuda:** Tente resolver sozinho por 30min. Não conseguiu? Peça ajuda explicando: "Tentei X e Y, esperava Z, mas aconteceu W".
- **Resiliência:** Programação é frustrante. O erro vai acontecer. Respire, tome um café, volte.
- **Comunicação:** Mantenha seu time (ou mentor) informado. "Estou travado nisso", "Terminei aquilo".

---

## 7. Estudo Ativo (Como treinar a Lógica de verdade)
Fazer exercícios só funciona se você **não estiver no piloto automático**.
- **A Regra dos 15 Minutos:** Tente resolver o exercício sem olhar a resposta por 15 minutos. É nesse "esforço" que o cérebro cria as conexões lógicas.
- **Explique para o Pato (Rubber Ducking):** Travou? Tente explicar o problema em voz alta para um pato de borracha (ou para a parede). Ao verbalizar, você organiza a lógica e muitas vezes acha a solução sozinho.
- **Variações:** O exercício pediu para somar 2 números? Tente mudar para somar 3. Tente mudar para multiplicar. Se você consegue mudar o código e ele funciona, você aprendeu a lógica.

---

## 🎯 Resumo
Se você dominar a **Lógica** (que já está estudando) + **Essas Práticas**, você estará na frente de 90% dos iniciantes que só sabem copiar código de tutorial.