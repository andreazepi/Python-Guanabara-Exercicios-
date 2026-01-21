# 📋 Backlog da Sprint 1 - Dev Junior

Bom dia, André! ☕👨‍💼

Aqui é o seu Tech Lead falando. Bem-vindo à equipe!

Para essa sua primeira semana (Sprint 1), separei 3 tickets (tarefas) que simulam problemas reais que temos no nosso sistema. O objetivo aqui não é só "fazer funcionar", mas escrever um código que seja seguro e não trave o servidor.

Vou te passar dois arquivos:

tarefas_sprint_1.md: O "E-mail" com os requisitos detalhados de cada tarefa.
sprint_1_dev_jr.py: O arquivo de código onde deixei a estrutura pronta para você trabalhar.
Seu foco agora é dominar o while para Validação, Tentativas (Retry) e Loops Infinitos Controlados.

Mãos à obra! 🚀

No Ticket #001, você tem um limite claro (3 tentativas). O while tentativas < 3 é perfeito aqui.
No Ticket #002, você quer prender o usuário até ele acertar. O while True com break quando a condição for satisfeita é muito limpo.
No Ticket #003, é um loop clássico de "Flag" (o zero para sair).

## Ticket #001: Sistema de Login com Bloqueio
**Prioridade:** Alta
**Cenário:** Precisamos proteger o sistema contra força bruta.
**Regra:**
- O usuário tem **3 chances** para digitar a senha correta (a senha correta é `1234`).
- Se ele errar, avise quantas chances restam.
- Se ele errar as 3 vezes, mostre "Conta Bloqueada" e encerre.
- Se acertar, mostre "Login efetuado" e encerre.
**Dica Técnica:** Use um `while` com contador de tentativas.

---

## Ticket #002: Validador de Cadastro (Idade e Salário)
**Prioridade:** Média
**Cenário:** O RH reclamou que estão cadastrando funcionários com dados absurdos.
**Regra:**
- Peça a **Idade**: Tem que ser entre 18 e 65 anos. Enquanto não for, peça de novo.
- Peça o **Salário**: Tem que ser maior que 0. Enquanto não for, peça de novo.
- Só mostre "Cadastro Validado" quando ambos estiverem certos.
**Dica Técnica:** Use `while True` ou `while condicao` para validar cada campo separadamente.

---

## Ticket #003: Monitoramento de Erros (Log)
**Prioridade:** Baixa
**Cenário:** Precisamos contar quantos erros críticos acontecem no sistema durante o dia.
**Regra:**
- O sistema deve pedir para o usuário digitar o código do erro (ex: 404, 500, 200).
- O loop só para quando o usuário digitar `0` (zero).
- No final, mostre quantos erros **500** (Erro Crítico) foram digitados.