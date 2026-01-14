'''
Exemplos para a Aula 8: Módulos e Packages
Este arquivo contém funções de exemplo pratico da aula 8:
'''

import math 
numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print(f'A raiz de {numero} é igual a {raiz}')
# em vez de utilizar a função math.sqrt() podemos utilizar o comando :.2f dentro do f-string para limitar o número de casas decimais
print(f'A raiz de {numero} é igual a {raiz:.2f}')

print(f'A raiz de {numero} arredondada para cima é igual a {math.ceil(raiz)}')
print(f'A raiz de {numero} arredondada para baixo é igual a {math.floor(raiz)}')
print(f'A raiz de {numero} sem casas decimais é igual a {math.trunc(raiz)}')

# Essa é a primeira forma de utilizar o módulo math, importando o módulo completo.
# Outra forma é importar apenas as funções que iremos utilizar, como no exemplo abaixo:
# se você apertar "Ctrl" + espaço após o "import" verá todas as funções disponíveis no módulo math
from math import sqrt  # Apartir do momento que eu faço isso, eu posso utilizar a função sqrt()         diretamente, sem o prefixo "math."
print(f'A raiz de {numero} (usando import específico) é igual a {sqrt(numero):.2f}')

# Exemplo de Alias para função (Apelido)
# Útil quando a função tem nome longo ou pode conflitar com outra
from math import factorial as fat
print(f'O fatorial de 5 é {fat(5)}')

# Exemplo de Módulo Padrão (já vem com o Python)
import random
numero = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
print(f'O número aleatório gerado foi: {numero}')

# Escolhendo um item aleatório de uma lista
lista_alunos = ['Maria', 'João', 'Pedro', 'Ana']
print(f'O aluno escolhido foi: {random.choice(lista_alunos)}')

# Exemplo de Pacote (NumPy)
try:
    import numpy as np  # Importa o pacote NumPy com o alias "np" 
    array = np.array([1, 2, 3, 4, 5])  # Cria um array NumPy
    print(f'O array criado foi: {array}')
except ImportError:
    print('\n[AVISO] NumPy não instalado. Instale com: pip install numpy')

# Exemplo de Pacote Externo (Pandas) - Requer: pip install pandas
try:
    import pandas as pd  # Importa o pacote Pandas com o alias "pd" 

    data = {
        'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
        'Idade': [25, 30, 35, 28],
        'Data_Admissao': ['15/01/2023', '10/02/2023', '20/03/2023', '15/01/2023'],
        'Departamento': ['TI', 'RH', 'TI', 'Financeiro']
    }
    df = pd.DataFrame(data)  # Cria um DataFrame Pandas a partir do dicionário
    print('O DataFrame criado foi:')
    print(df)

    # O poder do Pandas: Calcular estatísticas instantaneamente
    print(f'A média das idades é: {df["Idade"].mean()}')

    # Filtrando dados (Ex: Apenas do departamento de TI)
    print('\nFuncionários de TI:')
    print(df[df['Departamento'] == 'TI'])
except ImportError:
    print('\n[AVISO] Pandas não instalado. Instale com: pip install pandas')

# Exemplo com a biblioteca emoji
# Instalação no terminal: pip install emoji
try:
    import emoji
    print(emoji.emojize("Olá, Mundo :sunglasses:", language='alias'))
except ImportError:
    print('\n[AVISO] Emoji não instalado. Instale com: pip install emoji')