Exercícios: Contadores e Acumuladores

1. Calcular a Média das Notas:

Descrição: Dada uma lista de notas de alunos, calcular a média das notas.

Uso no Mundo Real: Calcular métricas de desempenho, análise de dados.

Implementação:

Usar um loop for para iterar pela lista de notas.
Usar um acumulador para somar as notas.
Usar um contador para controlar o número de notas.
Calcular a média dividindo a soma total pela contagem.

``` python
notas = [7.5, 8.0, 6.5, 9.0, 5.5, 10.0]
soma_notas = 0
for nota in notas:
    soma_notas += nota
media = soma_notas / len(notas)
print(f"A média das notas é: {media}")

2. Contar o Número de Linhas em um Arquivo:

Descrição: Dado um arquivo de texto, contar o número de linhas nele.

Uso no Mundo Real: Análise de arquivos de log, processamento de dados.

Implementação:

Abrir o arquivo.
Usar um loop for para iterar por cada linha no arquivo.
Usar um contador para incrementar para cada linha.

``` python
nome_arquivo = 'arquivo_teste.txt'
cont = 0
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        cont += 1
print(f'O arquivo {nome_arquivo} tem {cont} linhas.')

3. Calcular o Preço Total de Itens em um Carrinho de Compras:

Descrição: Dada uma lista de itens com preços, calcular o preço total de todos os itens no carrinho de compras.


Uso no Mundo Real: Aplicações de comércio eletrônico.

Implementação:

Usar um loop for para iterar pela lista de itens.
Usar um acumulador para somar os preços dos itens.

``` python
carrinho_precos = [45.90, 12.50, 8.00, 120.00, 9.99]
soma = 0

for preco in carrinho_precos:
    soma += preco

print(f'Total (For): R$ {soma:.2f}')


4. Contar as Ocorrências de uma Palavra Específica em um Texto:

Descrição: Dado um texto e uma palavra, contar quantas vezes essa palavra aparece no texto.

Uso no Mundo Real: Análise de texto, funcionalidade de busca.

Implementação:

Usar um loop for para iterar pelas palavras no texto (você pode precisar dividir o texto em palavras).
Usar um contador para incrementar cada vez que a palavra específica é encontrada.
``` python
nome_arquivo = 'texto_ex4.txt'
palavra_busca = 'Python'
contador = 0

with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        palavra_buscada = linha.split()   # .split() separar as palavras em uma lista.
        for palavra in palavra_buscada:
            if palavra == palavra_busca:
                contador += 1

print(f'A palavra "{palavra_busca}" aparece {contador} vezes no arquivo.')

5. Calcular a Soma de Números em um Intervalo (usando while):

Descrição: Calcular a soma dos números de um ponto inicial a um ponto final.

Uso no Mundo Real: Gerar somas em um determinado intervalo, calcular séries.

Implementação:

Usar um loop while que continua enquanto o número atual for menor ou igual ao número final.
Usar um acumulador para somar os números.
Incrementar o número atual em cada iteração.

inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))

soma = 0
atual = inicio

# Escreva seu while abaixo:
while atual <= fim:
    soma += atual
    atual += 1

print(f'A soma dos números entre {inicio} e {fim} é: {soma}')

6. Validar a Entrada do Usuário Até Correção (usando while):

Descrição: Continuar pedindo ao usuário para inserir dados até que ele forneça uma resposta válida (por exemplo, um número dentro de um intervalo específico).

Uso no Mundo Real: Validação de formulários, design de interface do usuário.

Implementação:

Usar um loop while que continua enquanto a entrada for inválida.
Dentro do loop, solicitar a entrada do usuário.
Verificar se a entrada é válida; caso contrário, exibir uma mensagem de erro.
Se a entrada for válida, sair do loop.

nota = -1

while nota < 0 or nota > 10:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Entrada invalida!')
print('entrada valida')

7. Simular um Caixa Eletrônico Básico:

Descrição: Permitir que um usuário deposite dinheiro, saque dinheiro e verifique seu saldo.

Uso no Mundo Real: Aplicações financeiras.

Implementação:

Usar um loop while para mostrar continuamente as opções do menu.
Usar um acumulador para rastrear o saldo.
Usar contadores e condicionais para gerenciar as transações.

saldo = 0
extrato = []  # Lista para guardar o histórico de movimentações

while True:
    print('-' * 20)
    print('CAIXA ELETRÔNICO')
    print('-' * 20)
    print('[1] Ver Saldo')
    print('[2] Depositar')
    print('[3] Sacar')
    print('[5] Extrato')  # Nova opção
    print('[4] Sair')
    
    opcao = int(input('Sua opção: '))

    match opcao:
        case 1:
            print(f'Seu saldo é de R${saldo:.2f}')
        case 2:
            deposito = float(input('Quanto deseja depositar? '))
            saldo += deposito   # acumulador
            extrato.append(f'Depósito: +R$ {deposito:.2f}')  # Adiciona ao histórico
            print(f'Você depositou R${deposito:.2f}')
        case 3:
            saque = float(input('Quanto deseja sacar? '))
            if saque > saldo:
                print('Saldo insuficiente.')
            else:
                saldo -= saque    # aqui já temos uma difença no acumulador
                extrato.append(f'Saque:    -R$ {saque:.2f}')  # Adiciona ao histórico
                print(f'Você sacou R${saque:.2f}')
        case 4:
            print('Saindo...')
            break
        case 5:
            print('--- EXTRATO ---')
            # Verifica se a lista está vazia
            if not extrato:
                print('Nenhuma movimentação registrada.')
            else:
                # Percorre a lista imprimindo cada linha
                for movimentacao in extrato:
                    print(movimentacao)
            print(f'Saldo Atual: R$ {saldo:.2f}')
        case _:
            print('Opção inválida. Por favor, tente novamente.')
print('Mercado Fechado.')


8. Calcular Juros Compostos:

Descrição: Calcular o valor final de um investimento, dados um principal, taxa de juros e período de tempo.

Uso no Mundo Real: Cálculos financeiros, planejamento de investimentos.

Implementação:

Usar um loop for para iterar por cada período de capitalização.
Usar um acumulador para atualizar o valor total após cada período.

capital = 1000.00
taxa = 0.05  # 5% ao ano
tempo = 10   # 10 anos
montante = capital

# Escreva seu código abaixo:

# Para cada ano no intervalo de 1 até 10:
for ano in range(1, tempo + 1):
    # O novo montante é o que eu já tinha MAIS os juros desse ano
    montante += montante * taxa
    print(f'Ano {ano}: R$ {montante:.2f}')

print(f'\nResultado Final: R$ {montante:.2f}')

9. Analisar o Tráfego do Site:

Descrição: Dada uma lista de visitas diárias ao site, calcular o total de visitas e a média de visitas diárias.

Uso no Mundo Real: Web analytics, marketing.

Implementação:

Usar um loop for para iterar pela lista de visitas.
Usar um acumulador para somar o total de visitas.
Usar um contador para controlar o número de dias.
Calcular a média dividindo o total de visitas pelo número de dias.

visitas_diarias = [120, 350, 200, 150, 500, 800, 450]
total = 0
dias = len(visitas_diarias)

for visitas in visitas_diarias:
    total += visitas

media = total / dias

print(f'Total de visitas: {total}')
print(f'Média de visitas diárias: {media}')