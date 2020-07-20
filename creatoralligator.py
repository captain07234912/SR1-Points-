"""
Universidad del Valle de Guatemala
Graficas por computadora
Principal
Jorge Suchite
Carnet 15293
07/07/2020
SR1 Points

sdad
"""



"""
Se corrigio que tiraba la imagen y la coordenada volteada

"""

from Render import Render
from LibreriaGL import *


# ancho y altura

prueba = Render(Y, x)

# printear cualquier cosa dentro del tamanio de la imagen

prueba.punto(100,150)

print(prueba.pixels)


prueba.write('Puntoprueba.bmp')

