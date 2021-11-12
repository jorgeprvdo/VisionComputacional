import cv2
from cv2 import data
import numpy as np
from PIL import Image

src = cv2.imread('Cebra.jpg')
src = cv2.fastNlMeansDenoisingColored(src, None, 10,10,7,21)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(7,7),3)

t, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
contours, _ = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(src, contours, -1, (0,255,255), 2, cv2.LINE_AA)

for c in contours:
    area = cv2.contourArea(c)
    if area > 1000 and area < 10000:
        cv2.drawContours(src, [c], 0, (0,255,255), 2, cv2.LINE_AA)

im = Image.open('Cebra.jpg')
data = np.array(im)

r1, g1, b1 = 0, 0, 0
r2, g2, b2 = 223, 66, 244

red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
mask = (red <= r1+50) & (green <= g1+50) & (blue <= b1+50)
data[:,:,:3][mask] = [r2, g2, b2]
im = Image.fromarray(data)
im.save('CebraMorada.jpg')

edges = cv2.Canny(src,100,200,apertureSize = 3)
# minLineLength = 50
# maxLineGap = 5
lines = cv2.HoughLinesP(edges,1,np.pi/100,95,minLineLength=48,maxLineGap=5)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(src,(x1,y1),(x2,y2),(255,255,255),1)

print("Lineas de la cebra:" +str(len(lines)))
cv2.imshow('Contorno', src)
cv2.imshow('Rayas', data)
cv2.waitKey(0)