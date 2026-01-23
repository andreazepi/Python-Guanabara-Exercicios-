import os
import shutil

# Nome da pasta onde vamos guardar os guias
pasta_destino = 'estudos_extras'

# Lista dos arquivos que estão soltos e queremos organizar
arquivos_para_mover = [
    'exercicio_fixacao_maior_menor.md',
    'exercicio_fixacao_listas_datas.md',
    'treino_logica_for.md',
    'exercicio_fixacao_primos.md',
    'exercicio_fixacao_loops_aninhados.md',
    'tarefas_sprint_1.md',
    'exercicios_contador_acumulador.md',
    'resumo_estruturas_fundamentais.md',
    'matematica_para_devs.md',
    'guia_boas_praticas_junior.md'
]

# 1. Cria a pasta se ela não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)
    print(f'📂 Pasta criada: {pasta_destino}')

# 2. Move os arquivos
for arquivo in arquivos_para_mover:
    if os.path.exists(arquivo):
        shutil.move(arquivo, os.path.join(pasta_destino, arquivo))
        print(f'✅ Movido: {arquivo}')
    else:
        print(f'⚠️  Não encontrado (ou já movido): {arquivo}')

print('\n✨ Organização concluída! Pode deletar este script agora.')
