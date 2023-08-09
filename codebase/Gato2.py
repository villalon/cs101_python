# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:13:31 2019

@author: Jorge
"""

# Cree una matriz de 5 x 5 y rellénela con números
# aleatorios entre 1 y 100
# Luego escriba el código para contar cuántos
# números primos hay en la matriz

import random

def creaLista():
    l = []
    for i in range(random.randint(1,10)):
        l.append(random.randint(1,100))
    return l

def buscarMaximo(li):
    maximo = li[0]
    for i in range(len(li)):
        if li[i] > maximo:
            maximo = li[i]
    return maximo

lista = creaLista()

print(lista)
# Encontrar el máximo
maximo = buscarMaximo(lista)

print("El maximo es " + str(maximo))

listaAzul = creaLista()

print(listaAzul)

maximo = buscarMaximo(listaAzul)

print("El maximo es " + str(maximo))

matriz = []

for i in range(5):
    fila = []
    for j in range(5):
        fila.append(random.randint(1,100))
    matriz.append(fila)
        
print(matriz)

maxmatriz = -1
for i in range(5):
    maximo = buscarMaximo(matriz[i])
    if maxmatriz < maximo:
        maxmatriz = maximo

print("El maximo de la matriz es:" + str(maxmatriz))