clear,clc
close all
% 图像相加是即将大小相等的两幅图像对应像素相加，下面为将 MATLAB软件自带图像进行相加处理得到。
Ibackground = imread('rice.png');
imshow(Ibackground);

J = imread('cameraman.tif');
figure, imshow(J);

K2 = imadd(Ibackground,J,'uint16');
figure,imshow(K2,[]);