import numpy as np
import matplotlib.pyplot as plt

# Definimos las funciones Theta y radio. 

def r(t, c):
    return c * t**2

def theta(t, k):
    return k * t**2

# Derivadas de theta

def primeraderivada_theta(t, k):
    return k * t * 2

def segundaderivada_theta(t, k):
    return k * 2

# Derivadas del radio

def primeraderivada_radio(t, c):
    return c * t * 2

def segundaderivad_radio(t, c):
    return c * 2

# Se define el vector radio, con sus respectivas componentes. 

def radio_vector(t, k, c):
    return np.array([
        r(t, c) * np.cos(theta(t, k)),  # Componente i
        r(t, c) * np.sin(theta(t, k))   # Componente j
    ])

def velocidad_vectorial(t, k, c):
    r_val = r(t, c)
    theta_val = theta(t, k)
    return np.array([
        primeraderivada_radio(t, c) * np.cos(theta_val) - r_val * primeraderivada_theta(t, k) * np.sin(theta_val), # Se deriva mediante la regla del producto
        primeraderivada_radio(t, c) * np.sin(theta_val) + r_val * primeraderivada_theta(t, k) * np.cos(theta_val)  # Se deriva mediante la regla del producto
    ])

def aceleracion_coriolis(t, k, c):
    omega = primeraderivada_theta(t, k)  # Velocidad angular
    velocidad = velocidad_vectorial(t, k, c)
    return -2 * np.cross([0, 0, omega], [velocidad[0], velocidad[1], 0])[:2]

# Parámetros para la simulación
t1, t2 = 0, 20  # Intervalo de tiempo
c = 0.1 # Constante radio
k = 0.2 # Constante theta
t_values = np.linspace(t1, t2, 500)  # Puntos de tiempo para evaluar

# Evaluar y graficar el radio vectorial
x_vals = [radio_vector(t, k, c)[0] for t in t_values]
y_vals = [radio_vector(t, k, c)[1] for t in t_values]

# Graficar la espiral
plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label="Trayectoria (Espiral)")
plt.title("Espiral generada por $r(t)$ y $\\Theta(t)$")
plt.xlabel("$x$ (dirección i)")
plt.ylabel("$y$ (dirección j)")
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()

#Ejemplo de calcular aceleración de Coriolis para un t específico
t_example = 10
a_coriolis = aceleracion_coriolis(t_example, k, c)
print(f"Aceleración de Coriolis en t={t_example}: {a_coriolis} m/s²")


print("holi")
print("ni hao")
print("good morning class")

