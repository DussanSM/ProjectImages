
import cv2

import numpy as np
from Operaciones import gray

def dilateImg(img):

    grayImg = gray.grayscale(img)
    
    # Umbralizar la imagen para obtener una imagen binaria
    _, binary_image = cv2.threshold(grayImg, 128, 255, cv2.THRESH_BINARY)

    # Crear un kernel para la dilatación
    kernel = np.ones((5, 5), np.uint8)

    # Aplicar el filtro de dilatación
    return cv2.dilate(binary_image, kernel, iterations=1)