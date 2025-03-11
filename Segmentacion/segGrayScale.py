import cv2
import numpy as np

def segmentGray(img):

    # Crear una máscara binaria (por ejemplo, seleccionar píxeles que sean mayores que 100)
    _, mask = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    # Aplicar la máscara a la imagen original usando bitwise_and
    return cv2.bitwise_and(img, img, mask=mask)