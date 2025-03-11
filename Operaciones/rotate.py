import cv2
from tkinter import simpledialog

# Permite rotar la imagen
def rotateImg(img):

    # Obtener las dimensiones de la imagen
    (h, w) = img.shape[:2]

    # Establecer el centro de la imagen para rotarla
    center = (w // 2, h // 2)

    # Obtener angulo de rotación
    r = simpledialog.askinteger("Rotar", "Ingrese el angulo de rotacion:")

    if r:
        # Crear la matriz de rotación
        M = cv2.getRotationMatrix2D(center, r, 1.0)

    # Rotar la imagen
    rotated_img = cv2.warpAffine(img, M, (w, h))
    return rotated_img