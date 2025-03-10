import cv2
from tkinter import filedialog

import matplotlib.pyplot as plt

def aritmeticOP(img):
    
    ruta = filedialog.askopenfilename(filetypes=[("Imagenes", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    
    if ruta:
        img2 = cv2.imread(ruta)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Redimensionar la segunda imagen al tamaño de la primera
        if img.shape[:2] != img2.shape[:2]:
            img2 = cv2.resize(img2, (img.shape[1], img.shape[0]))

        # Realizar operaciones aritméticas
        sum_img = cv2.add(img, img2)
        diff_img = cv2.subtract(img, img2)
        mult_img = cv2.multiply(img, img2)
        div_img = cv2.divide(img, img2 + 1)  # Se suma 1 para evitar divisiones por cero

        # Mostrar las imágenes resultantes
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))

        axs[0, 0].imshow(sum_img)
        axs[0, 0].axis("off")
        axs[0, 0].set_title("Suma")

        axs[0, 1].imshow(diff_img)
        axs[0, 1].axis("off")
        axs[0, 1].set_title("Resta")

        axs[1, 0].imshow(mult_img)
        axs[1, 0].axis("off")
        axs[1, 0].set_title("Multiplicación")

        axs[1, 1].imshow(div_img)
        axs[1, 1].axis("off")
        axs[1, 1].set_title("División")

        plt.show()