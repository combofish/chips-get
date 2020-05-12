clear,clc
close all
% 实现图像位置的旋转变换
I = imread('onion.png');
subplot(1,3,1), imshow(I), title('origin image');

T_rot30 = imrotate(I,30,'nearest');
subplot(1,3,2), imshow(T_rot30); title('rotate 20 degree');

I_rotf45 = imrotate(I,-45,'bilinear','crop');
subplot(1,3,3), imshow(I_rotf45); title('rotate -45 degree');