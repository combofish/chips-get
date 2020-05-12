clear,clc
close all
% 通过图像点运算增强图像对比度
I = imread('rice.png');
subplot(1,2,1);imshow(I); title('before processing');

I1 = double(I);
J = I1*1.4 + 40;
I2 = uint8(J);
subplot(1,2,2);imshow(I2); title('after processing');