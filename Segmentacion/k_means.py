import cv2
import numpy as np

def kmeans(img):

    # Convertir la imagen a una matriz de datos 2D (un píxel por fila)
    Z = img.reshape((-1, 3))

    # Convertir a flotante
    Z = np.float32(Z)

    # Definir criterios y aplicar kmeans
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    #Definir los criterios de terminación: maximo de 1000 iteraciones o si el cambio es menor que 0.2

    k = 2  # Número de clusters
    ret, label, center = cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convertir de nuevo los centros a 8 bits
    center = np.uint8(center)
    # Convertir los centros de los clusters a 8 bits (ya que los valores estaban en float32)

    # Etiquetas de los clusters
    res = center[label.flatten()]
    # Reemplazar los valores de cada píxel con el centro de su respectivo cluster

    # Remodelar la imagen segmentada para que tenga la misma forma que la original
    return res.reshape((img.shape))