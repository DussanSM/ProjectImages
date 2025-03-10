import cv2

def gaussianBlur(img):
    return cv2.GaussianBlur(img, (51, 51), 0)