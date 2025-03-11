import cv2

def segContour(img):

    grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Aplicar umbralización
    ret, thresholded_img = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)

    # Encontrar los contornos
    contours, hierarchy = cv2.findContours(thresholded_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos sobre la imagen original
    contoursImg = cv2.cvtColor(thresholded_img, cv2.COLOR_GRAY2BGR)  # Convertir a color
    cv2.drawContours(contoursImg, contours, -1, (0, 255, 0), 3)
    return contoursImg