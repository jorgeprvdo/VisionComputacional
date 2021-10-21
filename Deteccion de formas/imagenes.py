# Nombre: Jorge Alberto Prado Rivas
# Matricula: 1677044
# Visión Computacional
# Hora: N3


import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print(kernel)

img = cv2.imread('prueba.jpg')
img = cv2.resize(img, (300, 250))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv2.Canny(img, 200, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Imagen Canny', imgCanny)
cv2.imshow('Imagen original', img)
cv2.imshow('Imagen gris', imgGray)
cv2.imshow('Imagen blur', imgBlur)
cv2.imshow('Imagen Dialte', imgDialation)
cv2.imshow('Imagen Erode', imgEroded)

cv2.waitKey(0)