import cv2
import numpy as np
from Operaciones import bw

def opening(img):
    # Crear un kernel de 5x5
    kernel = np.ones((5, 5), np.uint8)

    bwImg = bw.blackNwhite(img)

    # Apertura para eliminar ruido
    return cv2.morphologyEx(bwImg, cv2.MORPH_OPEN, kernel)