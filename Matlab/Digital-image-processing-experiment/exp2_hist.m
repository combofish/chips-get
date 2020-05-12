clear, clc
close all
% 对原始图像进行直方图均衡化
I = imread('circuit.tif');
subplot(2,2,1); imshow(I); title('origin image');

subplot(2,2,2); imhist(I); title('origin histgram');
 
J = histeq(I,256);
subplot(2,2,3); imshow(J); title('equalization image');

subplot(2,2,4); imhist(J); title('histogram equalization');