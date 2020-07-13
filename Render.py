"""
Universidad del Valle de Guatemala
Graficas por computadora
Render
Jorge Suchite Carnet 15293
07/07/2020

"""
from LibreriaGL import *




class Render(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.glclear()
        self.Pcolor= Cyan
        # ancho y largo de la imagen


    def glInit(self):
        self.FrameBuffer(Fondo)


# le pongo de parametro c porque es el byte que quiero pintar y es solo uno

    """def FrameBuffer (self, c):
        self.pixeles = []
        for y in range(self.height):
            line = []
            for x in range(self.width)"""

 # necesito inciar framebuffer con el tamaio que le doy

    def glCreateWindow(self, width, height):








     " ""funcion que llena toda la imagen de un solo color con pixeles  " \
     " tomando la imagen como una matriz papu"""


    def glclear(self):
        self.pixels = [[Fondo for x in range (self.width)] for y in range(self.height) ]


    # funcion que me deja hacer el punto x largo, y alto

    def punto(self, x, y):
        self.pixels[x][y] = self.Pcolor

    # j balvin men
    #este colores me sirve para guardar el color que quiero pintar

    def colores(self, scolor):
            self.Pcolor = scolor

    # funcion que me deja escribir el BMP

    def write (self, filename):

        archivo = open(filename, 'wb')

        # header del archivo   de 14 bytes


        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))

        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        #   Header del Bitmap  de 40 bytes
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


    # fin de la funcion para escribir archivo
