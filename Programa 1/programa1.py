import cv2
import numpy as np

imagen = cv2.imread("Rueda.jpg")
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#Aplicar el suavizado o desenfoque
gaussiana = cv2.GaussianBlur(gris, (5,5), 0)
cv2.imshow("suavizado", gaussiana)

#detector de bordes
bordes = cv2.Canny(gaussiana, 50,150, apertureSize=3)
# cv2.imshow("Detector de bordes", bordes)

#Lineas
lines = cv2.HoughLinesP(bordes,1,np.pi/160,115,minLineLength=50,maxLineGap=5)
# Contornos
(contornos, j) = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

circles = cv2.HoughCircles(gaussiana, cv2.HOUGH_GRADIENT, 1, 200, param1=30, param2=45, minRadius=0, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:

    cv2.circle(imagen, (i[0], i[1]), i[2], (0,0,255), 2)
    cv2.circle(imagen, (i[0], i[1]), 2,(0,255,0),3)

cv2.imshow("Circulos", imagen)
print("Cantidad de ejes en la rueda: " +str(len(lines)))

cv2.waitKey(0)
cv2.destroyAllWindows()


