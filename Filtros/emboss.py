import cv2

import numpy as np

# Aplicar el filtro de relieve
def embossImg(img):

    # Crear un kernel para el filtro de relieve
    emboss_kernel = np.array([
                            [-2, -1, 0],
                            [-1,  1, 1],
                            [ 0,  1, 2]])
    
    return cv2.filter2D(img, -1, emboss_kernel)