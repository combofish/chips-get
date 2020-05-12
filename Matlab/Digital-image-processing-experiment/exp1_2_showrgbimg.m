clear,clc
close all
% 在一个图形窗口中显示RGB图像
I = imread('lena.jpg');
subplot(2,2,1),imshow(I);title('true color image');

R=I;R(:,:,[2,3])=0;
G=I;G(:,:,[1,3])=0;
B=I;B(:,:,[1,2])=0;
subplot(2,2,2),imshow(R),title('R color compents');
subplot(2,2,3),imshow(G),title('G color compents');
subplot(2,2,4),imshow(B),title('B color compents');