# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:53:05 2019

@author: Jorge
"""
# Saludar siempre es saludable
print ("hola mundo")
# Aún así podemos quejarnos
print("adiós mundo cruel") 
# Variable numérica
x=2
print(x)
# Variable de texto (string)
y="hola mundo"
print(y)

# Demonios, esto no funciona!
#print(x+y)

# Ahora y es numérico también, funciona el +
y=2
print(x+y)

# Y con números directamente?
print(1+2)

# Mezclando variables y números
print(x+2)

# Y si sumamos texto? (NOTA: Apostar por el resultado)
print("1"+"2")

# Convertir un número en un string
print(str(1) + "2")

# ¿Qué otras operaciones hay?

# Multiplicación
print(x*y)

# División
print(x-y)

# Potencia
print(x^y)

# División
print(x/y)

# Preferencia de operadores igual que en matemáticas
print(x/y+y)

# Paréntesis
print(x/(y+y))

# No funciona :-(
# print(x/(2y))

# Esto si funciona
print(x/(2*y))