# -*- coding: utf-8 -*-
"""
Creada el 09-08-2023

@author: Jorge
"""

# DEFinición de una nueva función
def convertir(x): # DEF nombre_función(conjunto_de_parámetros):
    y = x * 3 # y aparece en un color diferente, pues está dentro del scope. NOTA: Esta línea se agrega después
    w = x * 2 + z # z apunta a la variable externa, y no necesita estar definida antes.
    return w # Valor de retorno, reemplaza la invocación de la función

# Función a crear en segunda instancia, para mostrar el problema de varibles locales
def convertir2():
    # z = z + 5  # Esta línea arroja error porque usa z y la define al mismo tiempo.
    z = x + 2 # Al agregar esta línea, ya no se usa z del programa principal. Definimos una nueva variable local.
    return z + 5

# las 3 variables existen en el scope del programa completo
x = 3
y = 3
z = 4
print(x)
print(y)
print(z)

# al invocar la función convertir, se usa z desde el scope del programa
# principal e y se pasa como valor, no como referencia. No cambia el valor de y.
print(convertir(y))
print(y)

# Acá cambiamos el valor de z, y al invocar la función, usará este nuevo valor.
z = 6
x=convertir(z)
print(x)
print(convertir(x))

# Usamos convertir2
print(convertir2())

# Para cambiar el valor de una variable, no la podemos definir en una función
# de manera local. z no cambia.
print(convertir2())
print(z)

# Para cambiar el valor de una variable, basado en su valor previo, debemos
# usar el valor de retorno de la función.
z = convertir2()
print(convertir2())
print(z)