import cv2
import numpy as np

img = cv2.imread('Velociraptor.jpg')
cv2.imshow("imagen", img)

#Tamaño de la imagem
height, width = img.shape[:2]

print("Ancho y alto: ", height, width)

cv2.waitKey(0)
cv2.destroyAllWindows()