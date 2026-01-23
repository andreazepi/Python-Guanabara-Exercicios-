# ==============================================================================
# SPRINT 1 - AMBIENTE DE DESENVOLVIMENTO
# Dev: André
# Tech Lead: Gemini
# ==============================================================================

print("\n>>> INICIANDO TICKET #001: Login com Bloqueio <<<")
SENHA_CORRETA = "1234"
tentativas = 0
max_tentativas = 3
bloqueado = False

# TODO: Implemente o loop while aqui.
# Lógica: Enquanto tentativas forem menores que o máximo...
# 1. Pedir senha.
# 2. Se acertar -> Break.
# 3. Se errar -> Aumenta tentativas e avisa.
# 4. Se estourar o limite -> bloqueado = True.



# Validação final (fora do loop)
if bloqueado:
    print("❌ CONTA BLOQUEADA POR SEGURANÇA.")
else:
    print("✅ BEM-VINDO AO SISTEMA.")


# ==============================================================================

print("\n>>> INICIANDO TICKET #002: Validador de RH <<<")

# TODO: Validação de Idade
# Dica: Use while True. Se a idade for valida (18 a 65), break. Senão, print erro.
while True:
    try:
        idade = int(input("Digite a idade (18-65): "))
        # Escreva a lógica de validação aqui...
        break # (Remova esse break provisório quando implementar a lógica)
    except ValueError:
        print("Por favor, digite um número inteiro.")

# TODO: Validação de Salário (Maior que 0)
# Faça um segundo loop aqui para o salário.

print("✅ DADOS DO FUNCIONÁRIO VALIDADOS.")


# ==============================================================================

print("\n>>> INICIANDO TICKET #003: Monitor de Logs <<<")
qtd_erros_criticos = 0 # Acumulador (Contador)

# TODO: Loop infinito para ler códigos de erro.
# 1. Pedir código (int).
# 2. Se for 0 -> Break.
# 3. Se for 500 -> qtd_erros_criticos += 1.

print(f"Relatório Final: Tivemos {qtd_erros_criticos} erros críticos (500).")