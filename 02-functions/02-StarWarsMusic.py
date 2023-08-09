
# Importamos el módulo pygame
import pygame

# Inicializamos pygame
pygame.init()

# Usamos la función load para mover un mp3 desde el disco duro a la memoria del computador
pygame.mixer.music.load('cs101_python/files/starwars.mp3')

# Le decimos a pygame que toque el mp3
pygame.mixer.music.play(-1)

# Si no agregamos un while, el programa se cierra de inmediato
while True:
    # Si no agregamos el get event, el proceso quedará zombi
    # y solo podrá ser cerrado desde administración de tareas (o equivalente)
    pygame.event.get()
