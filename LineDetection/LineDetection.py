import cv2
import numpy as np

img = cv2.imread('Edificio.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/100, 50, maxLineGap=250)
print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow("Bordes", edges)
cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()