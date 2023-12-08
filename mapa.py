import turtle
import random
import math
import time

#Configuración
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.title("Dungeon Aleatoria")
# Tamaño de la grilla
GRID_SIZE = 20
GRID_LIMIT = 400

# Tamaño del campo de visión del protagonista
CAMPO_VISION = 40

# Tamaño de la celda de salida
SALIDA_SIZE = 20

#Personaje
protagonista = turtle.Turtle()
protagonista.speed(0)
protagonista.shape('circle')
protagonista.penup()
protagonista.direction = 'stop'
protagonista.color('white')

protagonista_x = random.randint(-GRID_LIMIT, GRID_LIMIT)
protagonista_y = random.randint(-GRID_LIMIT, GRID_LIMIT)
protagonista_x -= protagonista_x % GRID_SIZE
protagonista_y -= protagonista_y % GRID_SIZE
protagonista.goto(protagonista_x, protagonista_y)


# Celda de salida
celda_salida = turtle.Turtle()
celda_salida.speed(0)
celda_salida.shape('square')
celda_salida.color('green')
celda_salida.penup()
celda_salida_x = random.randint(-GRID_LIMIT, GRID_LIMIT)
celda_salida_y = random.randint(-GRID_LIMIT, GRID_LIMIT)
celda_salida_x -= celda_salida_x % GRID_SIZE
celda_salida_y -= celda_salida_y % GRID_SIZE
celda_salida.goto(celda_salida_x, celda_salida_y)

# Funciones de movimiento del protagonista
def mover_arriba():
    if not hay_pared(protagonista.xcor(), protagonista.ycor() + GRID_SIZE):
        protagonista.sety(protagonista.ycor() + GRID_SIZE)
        mostrar_cuadros()
        verificar_final_juego()

def mover_abajo():
    if not hay_pared(protagonista.xcor(), protagonista.ycor() - GRID_SIZE):
        protagonista.sety(protagonista.ycor() - GRID_SIZE)
        mostrar_cuadros()
        verificar_final_juego()

def mover_izquierda():
    if not hay_pared(protagonista.xcor() - GRID_SIZE, protagonista.ycor()):
        protagonista.setx(protagonista.xcor() - GRID_SIZE)
        mostrar_cuadros()
        verificar_final_juego()

def mover_derecha():
    if not hay_pared(protagonista.xcor() + GRID_SIZE, protagonista.ycor()):
        protagonista.setx(protagonista.xcor() + GRID_SIZE)
        mostrar_cuadros()
        verificar_final_juego()

# Función para verificar si hay pared en una posición
def hay_pared(x, y):
    for cuadro in cuadros:
        if colision(x, y, cuadro):
            return True
    return False

# Función para verificar colisión
def colision(x, y, objeto):
    x_dist = abs(x - objeto.xcor())
    y_dist = abs(y - objeto.ycor())
    return x_dist < GRID_SIZE / 2 and y_dist < GRID_SIZE / 2

# Función para verificar si el protagonista ha alcanzado la celda de salida
def verificar_final_juego():
    if colision(protagonista.xcor(), protagonista.ycor(), celda_salida):
        celda_salida.showturtle()
        time.sleep(1)
        turtle.bye()  # Cierra la ventana de Turtle y termina el juego

# Función para mostrar cuadros dentro del campo de visión
def mostrar_cuadros():
    for cuadro in cuadros:
        distancia = math.sqrt((protagonista.xcor() - cuadro.xcor())**2 + (protagonista.ycor() - cuadro.ycor())**2)
        if distancia < CAMPO_VISION:
            cuadro.showturtle()


# Función para ocultar todos los cuadros
def ocultar_cuadros():
    for cuadro in cuadros:
        cuadro.hideturtle()
    celda_salida.hideturtle()

# Función para generar cuadros aleatorios
def crear_cuadro():
    cuadro = turtle.Turtle()
    cuadro.speed(0)
    cuadro.shape('square')
    cuadro.color('gray')
    cuadro.penup()

    # Asegurar que las posiciones están en la grilla
    cuadro_x = random.randint(-GRID_LIMIT, GRID_LIMIT)
    cuadro_y = random.randint(-GRID_LIMIT, GRID_LIMIT)
    cuadro_x = cuadro_x - (cuadro_x % GRID_SIZE)
    cuadro_y = cuadro_y - (cuadro_y % GRID_SIZE)

    cuadro.goto(cuadro_x, cuadro_y)
    return cuadro

# Crear cuadros aleatorios
num_cuadros = 500
cuadros = [crear_cuadro() for _ in range(num_cuadros)]

while hay_pared(protagonista_x, protagonista_y):
    protagonista_x = random.randint(-GRID_LIMIT, GRID_LIMIT)
    protagonista_y = random.randint(-GRID_LIMIT, GRID_LIMIT)
    protagonista_x -= protagonista_x % GRID_SIZE
    protagonista_y -= protagonista_y % GRID_SIZE

protagonista.goto(protagonista_x, protagonista_y)

while hay_pared(celda_salida_x, celda_salida_y) or colision(celda_salida_x, celda_salida_y, protagonista):
    celda_salida_x = random.randint(-GRID_LIMIT, GRID_LIMIT)
    celda_salida_y = random.randint(-GRID_LIMIT, GRID_LIMIT)
    celda_salida_x -= celda_salida_x % GRID_SIZE
    celda_salida_y -= celda_salida_y % GRID_SIZE

celda_salida.goto(celda_salida_x, celda_salida_y)


# Inicialmente ocultar todos los cuadros
ocultar_cuadros()

# Mostrar pantalla de carga
turtle.textinput("Carga Completa", "Presiona Enter para continuar")

# Asignar funciones a teclas
turtle.listen()
turtle.onkey(mover_arriba, "Up")
turtle.onkey(mover_abajo, "Down")
turtle.onkey(mover_izquierda, "Left")
turtle.onkey(mover_derecha, "Right")


# Ciclo principal
while True:
    # Esto actualiza la ventana de Turtle
    turtle.update()
