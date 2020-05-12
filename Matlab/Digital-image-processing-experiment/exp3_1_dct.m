clear, clc 
close all
% 将真彩色图像变成灰度图像，并进行DCT变换，将DCT系数中小于10的系数舍弃使用idct2重构图像
RGB = imread('autumn.tif');
subplot(2,2,1), imshow(RGB), title('RGB');

I = rgb2gray(RGB);
subplot(2,2,2), imshow(I), title('J:RGB Gray');

J = dct2(I);
K1 = idct2(J);
subplot(2,2,3), imshow(K1,[0,255]), title('K1:Gray Dct Idct');

J(abs(J) < 10) = 0;
K2 = idct2(J);
subplot(2,2,4), imshow(K2,[0,255]), title('K2:Gray Dct Large10 Idct');