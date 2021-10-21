# Nombre: Jorge Alberto Prado Rivas
# Matricula: 1677044
# Visión Computacional
# Hora: N3

imagen=imread('prueba.jpg');
imshow(imagen)
cuadrante_superior_izquierdo=imagen(1:250,1:250,:);
cuadrante_inferior_derecho=imagen(251:500,251:500,:);
imagen(1:250,1:250,:)=cuadrante_inferior_derecho;
imagen(251:500,251:500,:)=cuadrante_superior_izquierdo;
imwrite(imagen, 'PruebaFinal.jpg');
imshow(imagen)
# Octave 6.3.0, Mon Oct 11 18:43:44 2021 GMT <unknown@DESKTOP-V30N649>
a=imread('prueba.jpg');
b=rgb2gray(a);
imshow(b)
borde=edge(b,'Sobel');
pkg load image
borde=edge(b,'Sobel');
imwrite(borde,'resuelto.jpg');
imshow(borde)
original=imread('prueba.jpg');
invertida=incomplement(original);
invertida=imcomplement(original);
imshow(invertida)
c=imread('prueba.jpg');
rotada=imrotate(a,180);
imshow(rotada)
redim=imresize(a,1.5);
imshow(redim)
redim=imresize(a,2.5);
imshow(redim)