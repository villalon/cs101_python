# -*- coding: utf-8 -*-
"""
First created on Tue Feb 19 18:42:13 2019

@author: Jorge
"""
# Importar librerías
import pygame

# Inicializar pygame
pygame.init()
# Reloj de pygame para que no vuele Mario
clock = pygame.time.Clock()
# Pantalla de 400 x 300
screen = pygame.display.set_mode((400, 300))
# Cargar música y ejecutarla
pygame.mixer.music.load('cs101_python/files/mario-bros.mp3')
pygame.mixer.music.play(-1)
# Imágenes
fondo = pygame.image.load('cs101_python/files/fondo.png')
mario = pygame.image.load('cs101_python/files/mario-sprite.png')
#mario = pygame.image.load('cs101_python/files/mario-sprite-4.png')
# Creamos una variable para poder "variar" la imagen que mostramos
i=0
# Que no se termine
while True:
        # Revisamos los eventos, para poder detener el programa
        pygame.event.get()

        # Siguiente imagen
        i = 2 + (i + 1) % 4

        screen.blit(fondo, (0, 0), (0, 0, fondo.get_width(), fondo.get_height()))

        screen.blit(mario, (50, 50), (i * 30, 0, 24, 24))
        
        pygame.display.flip()
        
        clock.tick(24)

        # print(i)