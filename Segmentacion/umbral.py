import cv2
import matplotlib.pyplot as plt

def thresholding(img):

    grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    ret, thresholded_img = cv2.threshold(grayImg, 200, 255, cv2.THRESH_BINARY)

    adaptive_threshold = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    plt.title('Segmentación por Umbralización Adaptativa Uno')
    plt.imshow(adaptive_threshold, cmap='gray')
    plt.axis('off')  # Ocultar los ejes
    plt.show()

    adaptive_threshold_2 = cv2.adaptiveThreshold(thresholded_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    plt.title('Segmentación por Umbralización Adaptativa Dos')
    plt.imshow(adaptive_threshold_2, cmap='gray')
    plt.axis('off')  # Ocultar los ejes
    plt.show()