clc,clear;
close all;
RGB=imread('saturn.png');
I0=rgb2gray(RGB);     %转化为原始灰度图像
I=imresize(I0,1/2);
figure(1);
subplot(2,2,1),imshow(I),title('original gray image');
J1=fft2(I);        %二维fft变换
subplot(2,2,2),imshow(log(1+abs(J1)),[]),title('spectrum image');

J2=fftshift(J1);
subplot(2,2,3),imshow(log(1+abs(J2)),[]),title('spectrum displacement');

K=ifft2(J2);          %显示频率变换后的频谱图
subplot(2,2,4),imshow(K,[]),title('the transformed spectrum');
