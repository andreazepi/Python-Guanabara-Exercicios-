## Desafio 021
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('exercicios_resolvidos_aula08/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# Certifique-se de ter o arquivo 'ex021.mp3' no mesmo diretório deste script para que ele funcione corretamente.
# Você pode instalar o pygame usando o comando: pip install pygame
# Outros exemplos e explicações detalhadas estão disponíveis no arquivo: anotacoes/ex021_reproduzir_audio.md
