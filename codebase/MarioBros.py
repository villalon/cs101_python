# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:42:13 2019

@author: Jorge
"""
# Importar librerías
import pygame
import sys
import random

# Reloj de pygame para que no vuele Mario
clock = pygame.time.Clock()

# Inicializar pygame
pygame.init()
# Pantalla de 400 x 300
screen = pygame.display.set_mode((400, 300))
# Cargar música y ejecutarla
pygame.mixer.music.load('cs101_python/files/mario-bros.mp3')
pygame.mixer.music.play(-1)
# Cargar el salto
sonidosalto = pygame.mixer.Sound('cs101_python/files/salto.wav')
sonidogameover = pygame.mixer.Sound('cs101_python/files/gameover.wav')
# Imágenes
fondo = pygame.image.load('cs101_python/files/fondo.png')
imageder = pygame.image.load('cs101_python/files/mario.png')
imageizq = pygame.image.load('cs101_python/files/mario-izq.png')
image = imageder
# Posición inicial
x = 200
y = 1
# Velocidad inicial
vy = 0
vx = 0
# Tortuga de Chernobyl ######################
imagentortuga = pygame.image.load('cs101_python/files/TortugaChernobyl.png')
xt = []
yt = []
vtx = []
vty = []
#########################################3
for i in range(3):
    xt.append(0)
    yt.append(random.randint(0,300))
    vtx.append(1)
    vty.append(0)
#######################################
paso = 1
puntaje = 0
jugando = True
basicfont = pygame.font.SysFont(None, 48)
# Que no se termine
while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False

        teclado = pygame.key.get_pressed()
        
        if teclado[pygame.K_ESCAPE]:
            jugando = False

        if teclado[pygame.K_UP]:# and y == 240:
            vy = vy - 1
            sonidosalto.play()
            
        if teclado[pygame.K_LEFT]:
            vx = -3
            image = imageizq
            
        if teclado[pygame.K_RIGHT]:
            vx = 3
            image = imageder
            
        if y > 240:
            y = 240
            vy = 0
            
        if x < 0:
            x = 0
            vx = 0

        if x > 400 - image.get_width():
            x = 400 - image.get_width()
            vx = 0
        
        for t in range(len(xt)):
            if xt[t] > 400 - imagentortuga.get_width():
                xt[t] = 0
                yt[t] = random.randint(0,300)
                puntaje = puntaje + 100
        
        for i in range(len(xt)):
            dx = abs(x - xt[i])
            dy = abs(y - yt[i])
            if(dx < 13 and dy < 13):
                sonidogameover.play()
                jugando = False

        # Movimiento rectilíneo de Mario
        y = y + vy
        x = x + vx
        
        # Movimiento rectilíneo de Tortugas
        for i in range(len(xt)):
            yt[i] = yt[i] + vty[i]
            xt[i] = xt[i] + vtx[i]
        
        if y < 240 and not teclado[pygame.K_UP]:
            vy = vy + 1
        
        paso = paso + 1
        
        if paso >= 60:
            paso = 1
        
        imgx = 32 * (round(x / 3) % 4)
        screen.blit(fondo, (0, 0), (0, 0, fondo.get_width(), fondo.get_height()))
        # imagenamostrar = pygame.Surface.subsurface(image,pygame.Rect(imgx, 0, imgx + 18, 18))
        text = basicfont.render(str(puntaje), True, (255, 0, 0), (255, 255, 255))
        screen.blit(text, (300, 0))

        screen.blit(image, (x, y))
        for i in range(len(xt)):
            screen.blit(imagentortuga, (xt[i], yt[i]))
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
sys.exit()