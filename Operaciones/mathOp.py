import numpy as np


def calcular_varianza_manual(imagen):
    """Calcula la varianza manualmente a partir de los valores de píxeles de una imagen en escala de grises."""
    alto, ancho = imagen.shape  # Obtener dimensiones de la imagen

    suma_total = 0
    total_pixeles = alto * ancho

    for y in range(alto):
        for x in range(ancho):
            suma_total += imagen[y, x]  
    media = suma_total / total_pixeles

    # Calcular la suma de los cuadrados de las diferencias con la media
    suma_cuadrados = 0
    for y in range(alto):
        for x in range(ancho):
            suma_cuadrados += (imagen[y, x] - media) ** 2

    # Calcular la varianza
    varianza = suma_cuadrados / total_pixeles
    return varianza 


# Calcular la correlación 

def calcular_correlacion_manual(imagen):
    """Calcula la correlación entre los píxeles de una imagen en escala de grises."""
    alto, ancho = imagen.shape
    total_pixeles = alto * ancho

    # Calcular la media de la imagen
    media = np.mean(imagen)

    # Calcular la desviación estándar
    desviacion = np.sqrt(calcular_varianza_manual(imagen))

    # Calcular la correlación (matriz desplazada)
    suma_correlacion = 0
    for y in range(alto - 1):  
        for x in range(ancho - 1):  
            suma_correlacion += (imagen[y, x] - media) * (imagen[y + 1, x + 1] - media)

    correlacion = suma_correlacion / total_pixeles

    return correlacion

# media 

def calcular_media_manual(imagen):
    """Calcula la media de los valores de los píxeles de la imagen en escala de grises."""
    alto, ancho = imagen.shape  # Dimensiones de la imagen
    total_pixeles = alto * ancho

    # Sumar todos los valores de los píxeles
    suma_total = np.sum(imagen)

    # Calcular la media
    media = suma_total / total_pixeles
    return media