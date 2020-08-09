from Render import Render, color


########################### Lista de colores para probar
Fondo = color(0,0,0)
Blanco = color(1,1,1)
CYAN = color(0,1,1)
Red = color(1,0,0)
BLUE = (0,0,1)
YELLOW = (1,1,0)

###########################################################
# tamaño de la imagen
prueba = Render(600, 600)
# introduzca el tamaño del viewport
prueba.glViewport(100, 100, 400, 400)

# ingrese el color del fondo
prueba.glClearColor(0,0,0)

# ingrese el color para pintar
prueba.glColor(1, 0, 0)
prueba.glClear()
# si quiere pintar un punto es aqui
prueba.punto(150,275)
prueba.glColor(1,0,0)
prueba.punto(100,200)

# quiere pintar una linea, perfecto! aca es el espacio




prueba.glFinish('PuntoPrueba.bmp')



