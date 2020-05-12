clear,clc
close all
% 实现真彩色图像与索引图像的互相转换
rgbimage = imread('lena.jpg');
[x1,map1] = rgb2ind(rgbimage,128); % rgb true color image to index iamge
imshow(x1,map1);title('index color iamge')

rgbimage2 = ind2rgb(x1,map1); % index image to rgb true coloe image 
figure,imshow(rgbimage2); title('rgb image')