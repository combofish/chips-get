clear,clc
close all
% 原始图像增加椒盐噪声和髙斯噪声，再分别用中值滤波和均值滤波处理图像

I = imread('eight.tif');
J1 = imnoise(I,'salt & pepper',0.02);
subplot(2,3,1), imshow(J1);title('salt & papper (J1)');

K1 = imfilter(J1,fspecial('average',3));
subplot(2,3,2), imshow(J1);title('average (J1)');

Z1 = medfilt2(J1,[3,3]);
subplot(2,3,3), imshow(Z1);title('medfilt2 (J1)');

J2 = imnoise(I,'gaussian',0.02);
subplot(2,3,4), imshow(J2);title('gussian (J2)');

Z2 = medfilt2(J2,[3,3]);
subplot(2,3,5), imshow(Z2);title('medfilt2 (J2)');

K2 = imfilter(J2,fspecial('average',3));
subplot(2,3,6), imshow(K2);title('average (J2)');
