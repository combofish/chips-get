clear,clc
close all

use = [1,0,0];

if use(1)
    % ????imadjust???????????
    I1 = imread('lena.jpg');
    I2 = rgb2gray(I1);
    I3 = imadjust(I2,[0 1],[1,0]);

    subplot(1,3,1), imshow(I1), title('origin image');
    subplot(1,3,2), imshow(I2), title('gray image');
    subplot(1,3,3), imshow(I3), title('Negative image');
end 

if use(2)
    % ????????????????????
    I4 = imread('lena.jpg');
    I5 = rgb2gray(I4);

    J4 = histeq(I5);
    subplot(2,2,1), imshow(I5), title('origin gray image');
    subplot(2,2,2), imhist(I5), title('histogram');
    subplot(2,2,3), imshow(J4), title('histogram equalization image');
    subplot(2,2,4), imhist(J4), title('equalization histogram');
end

if use(3)
    % ??????????????????????
    I6 = imread('lena.jpg');
    J6 = imnoise(I6,'salt & pepper',0.06);
    J7 = imnoise(I6,'gaussian',0.06);
    K6 = imfilter(J6,fspecial('average',3));
    K7 = imfilter(J7,fspecial('average',3));
    K8 = imfilter(J6,fspecial('average',6));
    K9 = imfilter(J7,fspecial('average',6));
    K10 = imfilter(J6,fspecial('average',9));
    K11 = imfilter(J7,fspecial('average',9));

    figure();
    subplot(2,2,1),imshow(J6),title('salt & pepper(J6)');
    subplot(2,2,2),imshow(K6),title('imfilter average 3 (J6)');
    subplot(2,2,3),imshow(K8),title('imfilter average 6 (J6)');
    subplot(2,2,4),imshow(K10),title('imfilter average 9 (J6)');

    figure();
    subplot(2,2,1),imshow(J7),title('gaussian (J7)');
    subplot(2,2,2),imshow(K7),title('imfilter average 3 (J7)');
    subplot(2,2,3),imshow(K9),title('imfilter average 6 (J7)');
    subplot(2,2,4),imshow(K11),title('imfilter average 9 (J7)');
end 
