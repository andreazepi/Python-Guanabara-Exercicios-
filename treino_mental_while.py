# 🧠 TREINO MENTAL: O PORTEIRO (Validação com While)
# Objetivo: Decorar a estrutura de obrigar o usuário a digitar a opção certa.

# Cenário: Você precisa obrigar o usuário a digitar 'S' (Sim) ou 'N' (Não).

resposta = ' '  # 1. Começa com um valor vazio ou inválido para forçar a entrada no loop

# 2. A CONDIÇÃO (O Porteiro)
# Leia-se: "Enquanto a resposta NÃO ESTIVER dentro de 'SN'..."
while resposta not in 'SN':
    
    # 3. A COLETA (A Tentativa)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # 4. O FEEDBACK (Opcional, mas bom para entender)
    if resposta not in 'SN':
        print('Dados inválidos. Por favor, digite S ou N.')

# Se o código chegou aqui, significa que o loop quebrou.
# Ou seja, a pessoa digitou S ou N.
print(f'Você escolheu a opção: {resposta}')

# DICA DE OURO:
# Tente reescrever esse código mudando para validar 'M' (Masculino) e 'F' (Feminino).
