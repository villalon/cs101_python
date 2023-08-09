# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:39:13 2019

@author: Jorge
"""
import random
# Escriba un programa en python
# que pregunte al usuario un número
# y cree una lista con ese número de
# valores aleatorios entre 10 y 99

def creaListaAleatoria(largo):
    lista = []
    for i in range(largo):
        lista.append(random.randint(10,99))
    return lista

def imprimeListaDiagonal(lista):
    contador = 0
    for i in range(len(lista)):
        contador = contador + 1
        for j in range(contador):
            print(" ", end="")
        print(lista[i])
        
def encontrarMaximo(lista):
    maximo = lista[0]
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo

def sacarNumeroLista(numero, lista):
    for i in range(len(lista)):
        if numero == lista[i]:
            lista[i] = 0 # lista[0] = 9
    return lista

def ordenarLista(lista):
    listaOrdenada = []
    for i in range(len(lista)):
        m1 = encontrarMaximo(lista)
        listaOrdenada.append(m1)
        sacarNumeroLista(m1, lista)
    return listaOrdenada
    











cuantos = int(input("Ingresa un número positivo"))
arreglo = creaListaAleatoria(cuantos)

print(arreglo)

print("El maximo es " + str(encontrarMaximo(arreglo)))

imprimeListaDiagonal(arreglo)
arreglo = ordenarLista(arreglo)
imprimeListaDiagonal(arreglo)