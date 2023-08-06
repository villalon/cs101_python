# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:17:32 2019

@author: Jorge
"""

print("Look ma! I'm gonna create a funcion!")

# No funciona porque no existe aún la función
# myfunction(1)

def myfunction(x):
    x=2+x
    return x

# print(myfunction("Hola mundo"))
print(myfunction(2))

y = myfunction(1)
print(myfunction(1))
print(myfunction(y))
