# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:32:58 2019

@author: Jorge
"""

import pygame

pygame.init()

pygame.mixer.music.load('cs101_python/files/starwars.mp3')
pygame.mixer.music.play(-1)

while True:
    pygame.event.get()
