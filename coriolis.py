import numpy as np
print("holi")
print("ni hao")
print("good morning class")

def aceleracion_coriolis(omega, v):
    """
    Calcula la aceleración de Coriolis.

    Parámetros:
    omega (array): Vector de velocidad angular del sistema en radianes por segundo (rad/s).
    v (array): Vector de velocidad del objeto en metros por segundo (m/s).

    Retorna:
    array: Vector de aceleración de Coriolis en m/s².
    """
    # Convertir omega y v a arrays de numpy si no lo son
    omega = np.array(omega)
    v = np.array(v)
    
    # Calcular la aceleración de Coriolis
    a_coriolis = -2 * np.cross(omega, v)
    return a_coriolis

# Ejemplo de uso
omega = [0, 0, 7.2921e-5]  # Velocidad angular de la Tierra (aproximadamente) en rad/s
v = [10, 0, 0]  # Velocidad del objeto en m/s en el sistema de referencia en rotación

a_coriolis = aceleracion_coriolis(omega, v)
print("Aceleración de Coriolis:", a_coriolis, "m/s²")
