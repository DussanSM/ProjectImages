import cv2
import numpy as np
import matplotlib.pyplot as plt

def segWatershed(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Hallar los contornos
    dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    ret, markers = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

    # Aplicar watershed
    markers = np.int32(markers)
    cv2.watershed(img, markers)

    # Marcamos los bordes en color rojo
    img[markers == -1] = [0, 0, 255]

    return img