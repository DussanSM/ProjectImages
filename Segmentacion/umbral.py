import cv2

def thresholding(img):
    # se puso 200 ya que mas bajo algunos elementos se pierden
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
