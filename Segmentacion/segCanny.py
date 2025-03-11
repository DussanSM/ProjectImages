import cv2
import matplotlib.pyplot as plt

def segmentCanny(img):

    grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ret, thresholded_img = cv2.threshold(grayImg, 200, 255, cv2.THRESH_BINARY)

    # Aplicar el filtro de Canny para detección de bordes
    edges = cv2.Canny(img, 100, 200)

    plt.title('Bordes Detectados')
    plt.imshow(edges, cmap='gray')
    plt.axis('off')  # Ocultar los ejes
    plt.show()

    # Aplicar el filtro de Canny para detección de bordes
    edges_dos = cv2.Canny(thresholded_img, 100, 200)

    plt.title('Bordes Detectados')
    plt.imshow(edges_dos, cmap='gray')
    plt.axis('off')  # Ocultar los ejes
    plt.show()