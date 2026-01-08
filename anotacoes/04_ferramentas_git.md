# 🛠️ Ferramentas e Dicas

## 1. Depuração (Debugging)
Processo de encontrar e corrigir erros.
1. **Escrever** o código.
2. **Executar** (Rodar).
3. **Depurar** (Corrigir falhas).
Processo de investigar, encontrar e corrigir falhas (bugs) no código. 

### Como funciona?
Pense na depuração como assistir ao seu código rodando em **câmera lenta**:
1. **Execução Passo a Passo:** Você executa uma linha de cada vez para entender o fluxo.
2. **Monitoramento:** Você vê o valor das variáveis mudando em tempo real.
3. **Breakpoints (Pontos de Parada):** Você marca uma linha (geralmente clicando ao lado do número da linha ou F9) para o código pausar ali, permitindo que você assuma o controle.

### Tipos de Erro
- **Erro de Sintaxe (Syntax Error):** Escrita errada (ex: falta parênteses). O Python avisa antes de rodar.
- **Erro de Lógica:** O programa roda, mas faz a coisa errada. A depuração é essencial aqui.

### Atalhos no VS Code
- **F5**: Inicia a Depuração.
- **Ctrl + F5**: Executa sem depurar (apenas roda).

## 2. Git vs GitHub
Ferramentas essenciais para controle de versão e trabalho em equipe.

### O que é o Git?
É um sistema de controle de versão instalado no seu computador. Ele serve para:
- Guardar o histórico de alterações (quem mudou, o que e quando).
- Criar "checkpoints" (versões) do seu projeto.
- Permitir voltar atrás caso algo dê errado.

### O que é o GitHub?
É uma plataforma na nuvem (como um Google Drive para código) onde você hospeda seus repositórios Git. Serve para:
- Backup do seu código.
- Compartilhar projetos (Portfólio).
- Trabalhar em equipe.

### Comandos Básicos
| Comando | Descrição |
| --- | --- |
| `git init` | Inicia o Git na pasta atual (cria o repositório). |
| `git status` | Mostra o estado dos arquivos (o que mudou). |
| `git add .` | Prepara todos os arquivos modificados para serem salvos. |
| `git commit -m "msg"` | Salva a versão (cria o checkpoint) com uma mensagem. |
| `git push` | Envia as alterações locais para o GitHub (nuvem). |
| `git pull` | Baixa atualizações do GitHub para o seu PC. |

## 3. Dicas de IDLE e Sintaxe
- **Comentários**: Use `#` para anotações que o código ignora.
- **Modo Interativo**: Bom para testes rápidos.
- **Modo Script (New File)**: Para programas completos.