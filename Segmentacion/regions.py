import cv2
import numpy as np

    # Función de crecimiento de regiones
def region_growing(seed_points, img, threshold):
    # Obtener la forma de la imagen
    rows, cols = img.shape
    mask = np.zeros_like(img)  # Crear la máscara

    for seed in seed_points:
        # Establecer el píxel semilla en la máscara
        mask[seed] = 255
        region_mean = img[seed]  # Promedio de la región inicial

        # Expansión de la región
        for i in range(rows):
            for j in range(cols):
                if mask[i, j] == 0:  # Si el píxel no está marcado
                    if abs(int(img[i, j]) - int(region_mean)) < threshold:
                        mask[i, j] = 255  # Marcar el píxel como parte de la región

    return mask