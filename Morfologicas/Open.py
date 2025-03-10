import cv2
import numpy as np

def opening(img):
    # Crear un kernel de 5x5
    kernel = np.ones((5, 5), np.uint8)

    # Apertura para eliminar ruido
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)