"""
Universidad del Valle de Guatemala
Graficas por computadora
Principal
Jorge Suchite
Carnet 15293
07/07/2020
SR1 Points
"""
from LibreriaGL import *

from Render import Render



prueba = Render(200, 200)


prueba.punto(100,100)

print(prueba.pixels)


prueba.write('Puntoprueba.bmp')

