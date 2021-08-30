import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread('cuarto2.jpg',0)
edges = cv2.Canny(imagen,100,250)

plt.subplot(121),plt.imshow(imagen,cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Imagen de los bordes'), plt.xticks([]), plt.yticks([])

plt.show()
