from vpython import *

# Definición de los objetos 3D
disk = cylinder(pos=vector(0,0,-.1), axis=vector(0,0,0.1), radius=1)
b1 = cylinder(pos=vector(-1,0,0), axis=vector(2,0,0), radius=0.02, color=color.red)
b2 = cylinder(pos=vector(0,-1,0), axis=vector(0,2,0), radius=0.02, color=color.green)

# Creación de un objeto compuesto (compound) a partir de los cilindros
mgo = compound([disk, b1, b2], pos=vector(0,0,-.1))
print(mgo.axis)

# Definición de la bola y sus propiedades iniciales
ball = sphere(pos=vector(-1,0,0), radius=.1, color=color.yellow, make_trail=True)
w = vector(0,0,1)  # Velocidad angular
g = vector(0,0,-9.8)  # Gravedad
ball.m = 0.1  # Masa de la bola
ball.v = vector(3,0,3)  # Velocidad inicial de la bola

# Parámetros de tiempo y escala
t = 0
dt = 0.01
ascale = 0.1
bscale = 1

# Fuerzas de Coriolis y centrípeta iniciales
acor = -2 * cross(w, ball.v)
acen = cross(cross(w, ball.pos), w)

# Flechas para visualizar las fuerzas de Coriolis y centrípeta
arrow1 = arrow(pos=ball.pos, axis=ascale * acor, color=color.cyan)
arrow2 = arrow(pos=ball.pos, axis=bscale * acen, color=color.magenta)

# Objeto oculto auxiliar
hid = sphere(pos=vector(0,-2.5,0), radius=0.001)

# Bucle para actualizar la posición de la bola y las fuerzas en cada paso de tiempo
while ball.pos.z >= 0:
    rate(100)  # Controla la velocidad de la simulación
    
    # Recalcular las fuerzas de Coriolis y centrípeta
    acor = -2 * cross(w, ball.v)
    acen = cross(cross(w, ball.pos), w)
    
    # Aceleración resultante
    ball.a = g + acor + acen
    
    # Actualización de la velocidad y posición de la bola
    ball.v = ball.v + ball.a * dt
    ball.pos = ball.pos + ball.v * dt
    
    # Actualización de las flechas de visualización
    arrow1.pos = ball.pos
    arrow2.pos = ball.pos
    arrow1.axis = ascale * acor
    arrow2.axis = bscale * acen
    
    # Incremento del tiempo
    t = t + dt
