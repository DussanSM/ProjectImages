import cv2

# Aplicar el filtro de detección de bordes (Canny)
def cannyImg(img):

    return cv2.Canny(img, 75, 230)