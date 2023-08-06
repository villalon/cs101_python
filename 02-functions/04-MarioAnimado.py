# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:42:13 2019

@author: Jorge
"""
# Importar librerías
import pygame

# Inicializar pygame
pygame.init()
# Pantalla de 400 x 300
screen = pygame.display.set_mode((400, 300))
# Cargar música y ejecutarla
pygame.mixer.music.load('cs101_python/files/mario-bros.mp3')
pygame.mixer.music.play(-1)
# Imágenes
fondo = pygame.image.load('cs101_python/files/fondo.png')
mario = pygame.image.load('cs101_python/files/mario-sprite.png')
# Que no se termine
while True:
        pygame.event.get()

        screen.blit(fondo, (0, 0), (0, 0, fondo.get_width(), fondo.get_height()))

        screen.blit(mario, (50, 50))
        
        pygame.display.flip()