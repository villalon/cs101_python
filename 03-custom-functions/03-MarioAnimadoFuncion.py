# -*- coding: utf-8 -*-
"""
First created on Tue Feb 19 18:42:13 2019

@author: Jorge
"""
# Importar librería pygame
import pygame

def mueveMario(px):
        x = px + 1
        if x > 400:
                x = 0
        return x

# Inicializar pygame
pygame.init()
# Reloj de pygame para que no vuele Mario (define máximo número de FPS)
clock = pygame.time.Clock()
# Pantalla de 400 x 300
screen = pygame.display.set_mode((400, 300))
# Cargar música y ejecutarla
pygame.mixer.music.load('cs101_python/files/mario-bros.mp3')
pygame.mixer.music.play(-1)
# Imágenes
fondo = pygame.image.load('cs101_python/files/fondo.png')
mario = pygame.image.load('cs101_python/files/sprites2.gif')
# Creamos una variable para poder "variar" la imagen que mostramos
i=0
# Creamos una variable x para la posición de Mario (queremos que varíe)
x = 350
# Que no se termine.
while True:
        # Leemos los eventos para que la ventana no se cuelgue
        pygame.event.get()

        # Siguiente imagen
        i = 7 + (i + 1) % 3

        # Movemos a Mario usando una función
        x = mueveMario(x)

        # Dibujamos el fondo sobre la pantalla.
        screen.blit(fondo, (0, 0), (0, 0, fondo.get_width(), fondo.get_height()))

        # Dibujamos a Mario sobre la pantalla, que ya tiene el fondo.
        screen.blit(mario, (x, 50), (i * 30, 30, 24, 24))
        
        # Flipeamos la RAM de video que se está mostrando
        pygame.display.flip()

        # Pedimos a Pygame que no dibuje más de 24 FPS        
        clock.tick(24)