clear, clc
close all
% 对图像进行空间域锐化滤波

I = imread('moon.tif');
w = fspecial('laplacian',0);
w8 = [1 1 1;1 -8 1; 1 1 1];
I1 = imfilter(I,w,'replicate');
subplot(1,2,1),imshow(I), title('original image');

J = im2double(I);J2 = imfilter(J,w8,'replicate');
K = J - J2;
subplot(1,2,2),imshow(K),title('sharpen image')
imwrite(K,'ruihua.bmp');