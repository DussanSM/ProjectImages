import cv2
import numpy as np
import matplotlib.pyplot as plt

def segWatershed(img):
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral binario
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Encontrar los contornos
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Crear una imagen vacía para los marcadores con 1 canal
    markers = np.zeros_like(gray, dtype=np.int32) # Changed to gray and dtype to int32

    # Definir los seed points (por ejemplo, marcar manualmente las regiones de interés)
    for i in range(len(contours)):
        cv2.drawContours(markers, contours, i, (i + 1), -1)

    # Marcar el fondo como -1
    markers[thresh == 0] = -1

    # Aplicar Watershed
    cv2.watershed(img, markers)

    # Las fronteras de los objetos serán marcadas con -1
    img[markers == -1] = [0, 0, 255]  # Rojo para las fronteras

    return img