# 🎵 Reproduzindo Áudio em Python (Desafio 021)

Este arquivo detalha como reproduzir arquivos de áudio (MP3) utilizando Python, com foco na biblioteca `pygame`.

## O Problema
O desafio consiste em criar um programa que abra e reproduza o áudio de um arquivo MP3.

---

## 1. A Biblioteca `pygame`
O Python não traz nativamente um reprodutor de MP3 robusto em sua biblioteca padrão. Por isso, utilizamos o **Pygame**, uma biblioteca muito popular para criação de jogos e multimídia.

### Instalação
Antes de usar, você precisa instalar a biblioteca pelo terminal:
```bash
pip install pygame
```

## 2. O Código Passo a Passo

```python
import pygame

# 1. Inicializar o Pygame
# É necessário iniciar os módulos do pygame antes de usar qualquer função.
pygame.init() 

# 2. Carregar o arquivo de música
# O arquivo deve estar na mesma pasta do script ou você deve passar o caminho relativo correto.
pygame.mixer.music.load('ex021.mp3')

# 3. Dar o Play
pygame.mixer.music.play()

# 4. Manter o programa rodando
# O Python executa as linhas e fecha o programa imediatamente. 
# Se não pedirmos para ele esperar, a música para assim que o script termina.
input("Escutando... Aperte Enter para parar.") 
```

## 3. Detalhes Importantes

### Por que o programa fecha sozinho?
O comando `play()` é **assíncrono**. Isso significa que ele manda a música tocar e o Python imediatamente libera o processador para a próxima linha de código. Se a próxima linha for o fim do arquivo, o programa encerra e o áudio é cortado instantaneamente.

**Soluções comuns:**
1. **`input()`**: O método mais simples. O programa pausa esperando o usuário digitar algo.
2. **`pygame.event.wait()`**: Espera um evento do Pygame. É o método clássico ensinado, mas às vezes pode exigir uma janela gráfica aberta para funcionar perfeitamente.

### Erro de Arquivo (`FileNotFoundError`)
Se o arquivo MP3 não estiver exatamente onde o script procura, o Python dará erro.
- Certifique-se de que o nome do arquivo no código (`ex021.mp3`) é idêntico ao arquivo real na pasta.