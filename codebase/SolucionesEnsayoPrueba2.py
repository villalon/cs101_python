import pandas as pd
import numpy as np
import random as rnd
import matplotlib.pyplot as mpl

from PIL import Image

# Pregunta 1
"""
def rgb2gray(rgb):
  return np.dot(rgb[...,:3], [0.2989, 0.5870,0.1140])

def analisis(coords, im):
    cont =0
    # para cada coordenada
    for i in range(0,coords.shape[0]):
        [x,y] = coords[i,:]
        x = coords[i][0]
        y = coords[i][1]
        pixel_value= im[x,y]

        if pixel_value>100:
            cont = cont+1
    
    return cont
    
# --- Programa Principal ---

#lectura de datos en Pandas
df = pd.read_csv('coordenadas_p2.csv')

# datos en formato numpy
coords = np.array(df[['x','y']])

# apertura de la imagen
img = mpl.imread('noise.png')
if np.all(img <= 1):
  img = (img*255).astype('uint8')

#convertimos a grises
img_data = rgb2gray(img)

output = analisis(coords, img_data)

print('Porcentaje de puntos de interés', output/coords.shape[0]*100)

input("Presione Enter para continuar")
"""
# Pregunta 2
"""
imagen=mpl.imread("happy_face.png")
imagen=(imagen*255).astype("uint8")
for i in range(1, imagen.shape[0]-1,3):
  for j in range(1,imagen.shape[1]-1,3):
    for k in range(0,3):
      imagen[i-1,j-1,k]=imagen[i,j,k]
      imagen[i-1,j+1,k]=imagen[i,j,k]
      imagen[i+1,j-1,k]=imagen[i,j,k]
      imagen[i+1,j+1,k]=imagen[i,j,k]
      imagen[i-1,j,k]=255
      imagen[i,j-1,k]=255
      imagen[i+1,j,k]=255
      imagen[i,j+1,k]=255
mpl.imsave("happy_face_pixel.png",imagen)

input("Presione Enter para continuar")
"""
# Pregunta 3

df = pd.read_csv('wwc.csv')

# Obtener el nombre de la arquera con mayor número de atajadas del torneo 
max_atajadas = df['Atajadas'].dropna().max()
arquera = df[df['Atajadas'] == max_atajadas]
print(arquera['Nombre'])

equipos = df.groupby(['Pais'])
# Obtener el país del equipo que ha convertido menos tantos en el torneo
goles = equipos['GolesConvertidos'].sum()
print(goles)
min_goles = goles.min()
print(goles[goles == min_goles].index)

# Obtener el número de pases por equipo
print(equipos['Pases'].sum())
# print(equipos['Pases'].agg(['sum']))

#Obtener el promedio de minutos jugados por equipo, sin tomar en cuenta a las jugadoras que no han jugado
equipos = df[df['Minutos']>0].groupby(['Pais'])
print(equipos['Minutos'].agg(['mean']))


input("Presione Enter para continuar")

# Pregunta 4

def genera_tablero():
  matriz = np.full([10,10,3], 255)
  posiciones = np.random.randint(0, 10, [5,2])
  for i in range(5):
    fila = posiciones[i,0]
    columna = posiciones[i,1]
    matriz[fila, columna, :] = 0
    fila = fila + rnd.sample([-1, 1], 1)
    if fila < 0:
      fila = fila + 2
    if fila > 9:
      fila = fila - 2
    columna = columna + rnd.sample([-1, 1], 1)
    if columna < 0:
      columna = columna + 2
    if columna > 9:
      columna = columna - 2
    matriz[fila, columna, :] = 0
  return(matriz)

def jugada(matriz, tablero):
  fila = int(input("Ingrese fila"))
  columna = int(input("Ingrese columna"))
  return chequea(matriz, tablero, fila, columna)

def chequea(matriz, tablero, fila, columna):
  R, G, B = 0, 1, 2
  if np.all(tablero[fila,columna,:] == 255):
    matriz[fila, columna, B] = 255
  elif np.all(tablero[fila,columna,:] == 0):
    if (fila >0 and columna > 0 and matriz[fila-1, columna-1, G] == 255) or (fila >0 and columna < 9 and matriz[fila-1, columna+1, G] == 255) or (fila < 9 and columna > 0 and matriz[fila+1, columna-1, G] == 255) or (fila < 9 and columna < 9 and matriz[fila+1, columna+1, G] == 255):
      matriz[fila, columna, R] = 255
      return 1
    else:
      matriz[fila, columna, R] = 255
      matriz[fila, columna, G] = 255
  mpl.imsave('jugadas.png', matriz)
  return 0

tablero = genera_tablero()

matriz = np.full([10,10,3], 0)
total = 0
flag = 0
while (total < 5):
  # la solución es:
  # total += jugada(matriz, tablero)
  # pero para recorrer todo hago:
  for i in range(0,9):
    for j in range(0,9):
      j = chequea(matriz, tablero, i, j)
      total += j
      if j == 1:
        print(f"Has hundido {total} barcos")
      if total == 5:
        flag = 1
        break
    if flag == 1:
      break

input("Presione Enter para continuar")
"""
# Pregunta 5
"""
def lastCommonYear(dfA,deporteA,deporteB):
    tempA=dfA[dfA['Sport']==deporteA]
    tempA=tempA['Year'].unique()
    tempB=dfA[dfA['Sport']==deporteB]
    tempB=tempB['Year'].unique()
    years = []
    for i in tempA:
        if i in tempB:
          years.append(i)
    if len(years) > 0:
      years=np.array(years)
      return np.max(years)
    return None

def difSignificativas(dfA,deporteA,deporteB):
    year=lastCommonYear(dfA,deporteA,deporteB)
    if year is None:
        return 0
    tempA=dfA[dfA['Sport']==deporteA]
    indexA=tempA['Year']==year
    tempB=dfA[dfA['Sport']==deporteB]
    indexB=tempB['Year']==year

    meanA=tempA['Height'][indexA].mean()
    varA=tempA['Height'][indexA].var()
    meanB=tempB['Height'][indexB].mean()
    varB=tempB['Height'][indexB].var()
    estT=(meanA-meanB)/np.sqrt(varA/sum(indexA)+varB/sum(indexB))
    return estT
        
df = pd.read_csv('athlete_events.csv')
i="Archery"
j="Golf"
est=difSignificativas(df,i,j)
if (-1.96<est and est<1.96 and est!=0):
  print("NO hay diferencias significativas entre ",i, " y ", j," con estadistico ",est)
else:
  if est!=0:
     print("Hay diferencias significativas entre ",i, " y ", j," con estadistico ",est)
  else:
    print("No hay jugadores con agnos en comun")
"""
