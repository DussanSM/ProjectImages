import cv2
from tkinter import simpledialog

# Permite cambiar el tamaño de la imagen
def resizeImg(img):
    
    if img is not None:
        # Pedir al usuario el nuevo ancho y alto
        w = simpledialog.askinteger("Redimensionar", "Ingrese el nuevo ancho:")
        h = simpledialog.askinteger("Redimensionar", "Ingrese el nuevo alto:")
        
        if w and h:
            resized_img = cv2.resize(img, (w, h))
            return resized_img