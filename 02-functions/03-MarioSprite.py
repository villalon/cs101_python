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
# Imágenes
mario = pygame.image.load('cs101_python/files/mario.png')
# Que no se termine
while True:
        pygame.event.get()
        screen.blit(mario, (0, 0))
        pygame.display.flip()