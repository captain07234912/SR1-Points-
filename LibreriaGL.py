
import struct

# struct library es para estructuras binarias de datos

"""Universidad del Valle de Guatemala
    Graficas por computadora
    Clase que tiene funciones para todo el curso
    Jorge Suchite Carnet 15293
    07/07/2020
    
    sdd
"""



# Creador del BMP
# Creador del punto



# 1 byte  reservado en memoria
def char(c):

    return struct.pack('=c', c.encode('ascii'))

# 2  reservado bytes en memoria

def word(w):

    return struct.pack('=h',w)

#4  reservado bytes en memoria

def dword(d):

    return struct.pack('=l',d)


# colores que son aceptados en bytes

def color(r, g, b):
    return bytes([b, g, r])




Fondo = color(0,0,0)
Cyan =  color(0,255,255)


# posicion en x y en Y para printear cosas
x= 300
Y= 200



