ANSI (é o codigo para cores)
escape sequence
 stype:text:back
\033[0:33:44m]


Styple
0 None (Sem estilo nenhum)
1 Bold (Negrito)
4 Underline (Siblinhado)
7 Negative (Negativo, ele inverte as cores do texto e do fundo)

Text (sempre começa com 33)
30 (Branco)
31 (Vermelho)
32 (Verde)
33 (Amarelo)
34 (Azul escuro)
35 (Roxo)
36 (Azul claro)
37 (Cinza)

Back (São as mesmas cores de text, porém começa com 40)

Letra branca com fundo vermelha: \033[0:30:41m]
Amarelo com fundo azul claro: \033[4:33:44m]
Roxo com fundo amarelo: \033[1:35:43m]
Branco com fundo verde: \033[30:42m]
Branco com fundo preto: \033[m]
Preto com fundo branco: \033[7:30m]

print('\033[1;31;43mOlá, Mundo\033[m') # Exemplo inicial colorido

# Exemplos baseados no arquivo cores_em_python.md
# Sintaxe ANSI: \033[style;text;backm
# Obs: Substituímos ':' por ';' para compatibilidade com Python.

# 1. Letra branca com fundo vermelho
# Style: 0 (None), Text: 30 (Branco), Back: 41 (Vermelho)
print('\033[0;30;41mTeste 1: Letra branca com fundo vermelho\033[m')

# 2. Amarelo com fundo azul (Código 44 é Azul Escuro na tabela padrão, embora o MD diga claro)
# Style: 4 (Sublinhado), Text: 33 (Amarelo), Back: 44 (Azul)
print('\033[4;33;44mTeste 2: Amarelo sublinhado com fundo azul\033[m')

# 3. Roxo com fundo amarelo
# Style: 1 (Negrito), Text: 35 (Roxo), Back: 43 (Amarelo)
print('\033[1;35;43mTeste 3: Roxo negrito com fundo amarelo\033[m')

# 4. Branco com fundo verde
# Text: 30 (Branco), Back: 42 (Verde)
print('\033[30;42mTeste 4: Branco com fundo verde\033[m')

# 5. Preto com fundo branco
# Style: 7 (Inverte as cores: Texto 30 Branco vira Fundo Branco, Fundo padrão vira Texto Preto)
print('\033[7;30mTeste 5: Preto com fundo branco (Invertido)\033[m')

