# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:17:32 2019

@author: Jorge
"""

print("Look ma! I'm gonna create a funcion!")

# No funciona porque no existe aún la función
# myfunction(1)

# def permite crear una nueva función dentro de este programa
def myfunction(x):
    # Tenemos que indentar para saber qué código pertenece a la función y cuál no
    x=2+x
    # El valor de retorno reemplaza la invocación de la función
    return x

# No funciona porque los tipos fallan
# print(myfunction("Hola mundo"))
print(myfunction(2))

# Guardar el resultado en una variable
y = myfunction(1)

# Imprimimos la variable, y llamadas a la función. NOTA: Momento ideal para apostar por el output.
print(y)
print(myfunction(1))
print(myfunction(y))
