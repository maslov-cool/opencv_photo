import cv2
import numpy as np

image = cv2.imread('path.png')

image = cv2.resize(image, (image.shape[1] * 2, image.shape[0] * 2))
#image = cv2.GaussianBlur(image, (9, 9), 0) --> размытие фото
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) --> чёрно-белое фото
image = cv2.Canny(image, 200, 200)

kernel = np.ones((5, 5), np.uint8)
image = cv2.dilate(image, kernel, iterations=1)

image = cv2.erode(image, kernel, iterations=1)

#cv2.imshow('Space', image[0:640, 0:576]) --> обрезка фото
cv2.imshow('Space', image)

#print(image.shape) --> показывает размеры фото и количество слоёв

cv2.waitKey(0)
