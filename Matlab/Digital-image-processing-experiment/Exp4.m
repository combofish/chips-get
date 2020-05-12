clear, clc
close all
% 调用edge函数利用多种边缘检测算子（至少4种（包括二阶微分算子））检测两幅图（可以用书上图或其它图）中的图像边缘，并对结果进行比较

I1 = imread('cell.tif');
I2 = imread('tire.tif');
figure();
subplot(2,4,1);
imshow(I1);title('origin image');

I0 = I1;
BW = edge(I0,'sobel');
subplot(2,4,2), imshow(BW); title('sobel horizontal');

% sobel both
BW = edge(I0,'sobel','both');
subplot(2,4,4), imshow(BW); title('sobel both');

% sobel vertical
BW = edge(I0,'sobel','vertical');
subplot(2,4,3), imshow(BW); title('sobel vertical');

% roberts
BW = edge(I0,'roberts');
subplot(2,4,5), imshow(BW); title('roberts');

% prewitt
BW = edge(I0,'prewitt');
subplot(2,4,6), imshow(BW); title('prewitt');

% log
BW = edge(I0,'log');
subplot(2,4,7), imshow(BW); title('log');

% canny
BW = edge(I0,'canny');
subplot(2,4,8), imshow(BW); title('canny');

figure();
I0 = I2;

subplot(2,4,1), imshow(I0), title('origin image');

BW = edge(I0,'sobel');
subplot(2,4,2), imshow(BW); title('sobel horizontal');

% sobel both
BW = edge(I0,'sobel','both');
subplot(2,4,4), imshow(BW); title('sobel both');

% sobel vertical
BW = edge(I0,'sobel','vertical');
subplot(2,4,3), imshow(BW); title('sobel vertical');

% roberts
BW = edge(I0,'roberts');
subplot(2,4,5), imshow(BW); title('roberts');

% prewitt
BW = edge(I0,'prewitt');
subplot(2,4,6), imshow(BW); title('prewitt');

% log
BW = edge(I0,'log');
subplot(2,4,7), imshow(BW); title('log');

% canny
BW = edge(I0,'canny');
subplot(2,4,8), imshow(BW); title('canny');
