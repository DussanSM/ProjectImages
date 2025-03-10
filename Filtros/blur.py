import cv2

# Aplicar el filtro de desenfoque
def blurImg(img):

    return cv2.blur(img, (50, 50))