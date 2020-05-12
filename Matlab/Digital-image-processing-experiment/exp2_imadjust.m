clear,clc
close all
% 对图像进行灰度变换，实现反转图像效果

I = imread('cameraman.tif');
subplot(1,2,1), imshow(I), title('origin image');

I1 = imadjust(I,[0 1],[1 0],1);
subplot(1,2,2), imshow(I1), title('adjusted image');