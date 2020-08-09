import struct
from LibreriaGL import *

"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020
SR1 : Points
"""



class Render(object):
    def __init__(self, width, height):
        self.colorPintar = YELLOW
        self.clearFondo = Fondo
        self.glCreateWindow(width, height)
        # ancho y largo de la imagen

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0, 0, width, height)

    def glViewport(self, x, y, width, height):
        self.CoorxViewport = x
        self.CooryViewport = y
        self.ViewportHEight = height
        self.ViewportWidth = width

    """funcion que llena toda la imagen de un solo color con pixeles   
         tomando la imagen como una matriz papu"""
    def glClear(self):
        self.pixels = [[self.clearFondo for x in range(self.width)] for y in range(self.height)]

    # funcion que me deeja ahcer el punto x largo y  alto
    def punto(self,x,y):
        self.pixels[y][x] = self.colorPintar

    # vertex relativo al viewport punto en pantalla
    def glVertex(self, x, y):
        pixelX = ( x + 1) * (self.ViewportWidth / 2) + self.CoorxViewport
        pixelY = ( y + 1) * (self.ViewportHEight / 2) + self.CooryViewport
        self.pixels[round(pixelY)][round(pixelX)] = self.colorPintar

    def glVertexespacio(self, x, y):
        self.pixels[y][x] = self.colorPintar

    # j balvin men
    # este colores me sirve para guardar el color
    def glColor(self, r, g, b):
        self.colorPintar = color(r, g, b)
    # poner el color de fondo si quiere cuas

    def glClearColor(self, r, g, b):
        self.clearFondo = color(r, g, b)
    # funcion que me deja escribir el BMP

    def glFinish(self, filename):
        archivo = open(filename, 'wb')

        # header del archivo de  14 bytes
        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))
        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # header del Mitmap de 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))


        for x in range(self.height):
            for y in range(self.width):
                archivo.write(self.pixels[x][y])

        archivo.close()




                











