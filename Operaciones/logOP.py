import cv2

from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy as np

# Permite realizar Operaciones Logicas entre Imagenes
def logicOP(img):

    ruta = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    
    if ruta:
        img2 = cv2.imread(ruta)

        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # Redimensionar img2 si tiene diferente tamaño
        if img1.shape != img2.shape:
            img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

        # Convertir a binario (THRESH_BINARY) y asegurarse de que las dimensiones sean iguales
        _, img_binaria_1 = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY)
        _, img_binaria_2 = cv2.threshold(img2, 128, 255, cv2.THRESH_BINARY)

        img_binaria_1 = img_binaria_1.astype(np.uint8)
        img_binaria_2 = img_binaria_2.astype(np.uint8)

        # Operaciones lógicas
        and_img = cv2.bitwise_and(img_binaria_1, img_binaria_2)
        or_img = cv2.bitwise_or(img_binaria_1, img_binaria_2)
        not_img1 = cv2.bitwise_not(img_binaria_1)
        not_img2 = cv2.bitwise_not(img_binaria_2)

        # Mostrar imágenes en una cuadrícula
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))

        axs[0, 0].imshow(and_img, cmap="gray")
        axs[0, 0].axis("off")
        axs[0, 0].set_title("AND")

        axs[0, 1].imshow(or_img, cmap="gray")
        axs[0, 1].axis("off")
        axs[0, 1].set_title("OR")

        axs[1, 0].imshow(not_img1, cmap="gray")
        axs[1, 0].axis("off")
        axs[1, 0].set_title("NOT Imagen 1")

        axs[1, 1].imshow(not_img2, cmap="gray")
        axs[1, 1].axis("off")
        axs[1, 1].set_title("NOT Imagen 2")

        plt.show()