import cv2

import tkinter as tk
from tkinter import  simpledialog
import matplotlib.pyplot as plt

def interpolation(img):
    
    if img is None:
        return

    w = simpledialog.askinteger("Redimensionar", "Ingrese el nuevo ancho:")
    h = simpledialog.askinteger("Redimensionar", "Ingrese el nuevo alto:")

    # Redimensionar la imagen con diferentes interpolaciones
    resized_bilinear = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
    resized_nearest = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)

    # Mostrar las imágenes resultantes
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(resized_bilinear, cmap='gray')
    axes[0].set_title("Interpolación Bilineal")
    axes[0].axis('off')

    axes[1].imshow(resized_nearest, cmap='gray')
    axes[1].set_title("Interpolación Vecino Más Cercano")
    axes[1].axis('off')

    plt.show()