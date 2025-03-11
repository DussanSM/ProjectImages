# Cargar imagen en color
import cv2
import numpy as np

def detectColor(img):

    # Convertir a espacio de color HSV
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definir rango de color en el espacio HSV
    lower_bound = np.array([30, 50, 50])  # Rango inferior (ej. verde)
    upper_bound = np.array([80, 255, 255])  # Rango superior

    # Crear máscara para segmentar el color verde
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Aplicar máscara sobre la imagen original
    segmented_img = cv2.bitwise_and(img, img, mask=mask)

    return segmented_img