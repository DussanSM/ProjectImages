import cv2

import numpy as np

def sharp(img):

    # Crear un kernel para nítidez
    sharpen_kernel = np.array(
                            [[-1, -1, -1],
                            [-1,  9, -1],
                            [-1, -1, -1]])

    # Aplicar el filtro de nítidez el segundo parametro de profundidad de la imagen de salida ddepth
    return cv2.filter2D(img, 0, sharpen_kernel)