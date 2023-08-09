# -*- coding: utf-8 -*-
"""
First created on Tue Feb 19 18:42:13 2019

@author: Jorge
"""
# Importar librería pygame
import pygame

# Declaramos una constante para jugar con los tamaños de las imágenes.
ESCALA_MARIO = 5

# Esta función devuelve un nuevo valor de X, dado una previo, entregado como parámetro
def mueveMario(x):
        nuevoX = x + vx # Usamos la variable global vx (o pasar por parámetro)
        return nuevoX

# Usamos la función rebotaMario para cambiar la velocidad una vez que Mario
# llega a un extremo de la pantalla. Se puede usar el OR para simplificar la
# función de rebote.
def rebotaMario(x):
        if x > 1024 - 20 * ESCALA_MARIO:
                return -1 * vx
        if x < 0:
               return -1 * vx
        return vx

# Inicializar pygame
pygame.init()
# Reloj de pygame para que no vuele Mario (define máximo número de FPS)
clock = pygame.time.Clock()
# Pantalla de 400 x 300
screen = pygame.display.set_mode((1024, 768))
# Cargar música y ejecutarla
pygame.mixer.music.load('cs101_python/files/mario-bros.mp3')
pygame.mixer.music.play(-1)
# Imágenes
fondo = pygame.image.load('cs101_python/files/fondo-mario-grande.png')
mario = pygame.image.load('cs101_python/files/sprites2.gif')
# Usamos la función scale de pygame para agrandar la imagen de Mario
# la imagen originalmente es de 300x650, por eso escalar por una constante.
mario = pygame.transform.scale(mario, (300 * ESCALA_MARIO, 650*ESCALA_MARIO))
# Creamos una variable para poder "variar" la imagen que mostramos
i=0
# Creamos una variable x para la posición de Mario (queremos que varíe)
x = 250
# Con una nueva variable, velocidad, podemos hacer que se mueva en ambas direcciones
vx = 5
# Que no se termine.
while True:
        # Leemos los eventos para que la ventana no se cuelgue
        pygame.event.get()

        # Movemos a Mario, pidiendo un nuevo valor a la función mueveMario.
        x = mueveMario(x)

        # Cambiamos la velocidad de Mario, haciendo que rebote.
        vx = rebotaMario(x)

        # Siguiente imagen
        i = 7 + (i + 1) % 3

        # Dibujamos el fondo sobre la pantalla.
        screen.blit(fondo, (0, 0), (0, 0, fondo.get_width(), fondo.get_height()))

        # Dibujamos a Mario sobre la pantalla, que ya tiene el fondo.
        screen.blit(mario, (x, 520), (i * 30 * ESCALA_MARIO, 30 * ESCALA_MARIO, 24*ESCALA_MARIO, 24*ESCALA_MARIO))
        
        # Flipeamos la RAM de video que se está mostrando
        pygame.display.flip()
        
        # Pedimos a Pygame que no dibuje más de 24 FPS        
        clock.tick(24)
