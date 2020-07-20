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
from LibreriaGL import *


"""
Se corrigio que tiraba la imagen y la coordenada volteada

"""

from Render import Render


# ancho y altura
prueba = Render(200, 300)


prueba.punto(100,150)

print(prueba.pixels)


prueba.write('Puntoprueba.bmp')

