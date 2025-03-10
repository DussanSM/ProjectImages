import cv2

# Convierte la imagen a escala de grises
def grayscale(img):
    
    if img is not None:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)