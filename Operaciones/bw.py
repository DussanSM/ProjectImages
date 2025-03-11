import cv2

# Convierte la imagen a blanco y negro (binarización)
def blackNwhite(img):
    
    if img is not None:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        _, bw_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)
        return bw_img