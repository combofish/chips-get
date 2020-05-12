clear,clc 
close all
% 对二值图像、索引色图像实现读取、显示和保存
i1 = imread('circbw.tif');
imshow(i1),title('black-and-white image');
imwrite(i1,'newcircbw.bmp');

figure,imshow('newcircbw.bmp');
title('newcircbw.bmp')

load clown
imwrite(X,map,'clown.bmp');
[i2,map] = imread('clown.bmp');
figure,imshow(i2,map);
title('index color image');

imwrite(i2,map,'newclown.bmp');
figure,imshow('newclown.bmp');
title('newclown.bmp');
whos i1 i2