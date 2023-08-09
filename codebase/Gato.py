# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:56:03 2019

@author: Jorge
"""
import random
import sys

gato = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]

# print(gato)
def imprime(felix):
    for i in range(3):
        for j in range(3):
            print(felix[i][j], end=" ")
        print()

def preguntaFilaColumna():
    i = int(input("En qué fila quiere jugar (0 al 2):"))
    j = int(input("En qué columna quiere jugar (0 al 2):"))
    return [i, j]

def revisaGanar(gato, quereviso):
    for i in range(3):
        c = 0
        dondeestaelcero = -1
        for j in range(3):
            if quereviso == 'filas':
                c = c + gato[i][j]
                if gato[i][j] == 0:
                     dondeestaelcero = i
            else:
                c = c + gato[j][i]
                if gato[j][i] == 0:
                    dondeestaelcero = j
        if c == 6:
            if quereviso == 'filas':
                gato[j][dondeestaelcero] = 3
            else:
                gato[dondeestaelcero][i] = 3
            print("Gané madafaka")
            imprime(gato)
            sys.exit()
        elif c == 2:
            if quereviso == 'filas':
                gato[j][dondeestaelcero] = 3
                print("Bloqueando " + str(j) + " " + str(dondeestaelcero))
            else:
                gato[dondeestaelcero][i] = 3                
                print("Bloqueando " + str(dondeestaelcero) + " " + str(i))
            return True
        print(quereviso + " " + str(i) + " " + str(c))
    return False

imprime(gato)

espaciosLlenos = 0
quienjuega = "Persona"
while(espaciosLlenos <= 8):
    if quienjuega == "Persona":
        jugadaUsuario = preguntaFilaColumna()
        i = jugadaUsuario[0]
        j = jugadaUsuario[1]
        while(gato[i][j] != 0):
            print("No seai barsa")
            jugadaUsuario = preguntaFilaColumna()
            i = jugadaUsuario[0]
            j = jugadaUsuario[1]
        
        gato[i][j] = 1
        quienjuega = "Robot"
    else:
        jugo = revisaGanar(gato, 'filas')
        if jugo == False:
            jugo = revisaGanar(gato, 'kolumnas')
        
        if jugo == False:
            p = random.randint(0,2)
            q = random.randint(0,2)
            while(gato[p][q] != 0):
                p = random.randint(0,2)
                q = random.randint(0,2)
            print("Random " + str(p) + " " + str(q))
            gato[p][q] = 3
            
        quienjuega = "Persona"

    print("==========")

    imprime(gato)
    
    espaciosLlenos = espaciosLlenos + 1