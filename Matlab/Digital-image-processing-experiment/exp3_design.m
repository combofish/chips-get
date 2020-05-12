clear,clc
close all

use = [0,0,1];

if use(1)
    I = imread('lena.jpg');
    figure();imshow(I); title('origin figure');

    I1 = fft2(I);I1_ = abs(I1);
    %figure();imshow(I1_,[0,255]);title('I1:FFT2 abs');

    %figure(); imshow(log(1+I1_),[0,255]); title('T1:FFT2 abs log');

    IS = abs(fftshift(I1));
    figure();imshow(IS,[ ]);title('IS:FFT2 fftshift abs');
    figure(); imshow(log(1+IS),[ ]); title('TS:FFT2 fftshift abs log');
end 

if use(2)
    f = imread('tire.tif');
    imshow(f)
    
    F = fft2(f); % 傅氏变换
    Fc = fftshift(F);% 中心化
    Fm = abs(Fc); % 取模
    figure, imshow(Fm,[ ]);
    figure, imshow(log(1+Fm),[ ]); % 对数变换，增强显示视觉效果
    G = ifftshift(Fc); % 对Fc去中心化
    g = ifft2(G); % 对G逆变换
    figure, imshow(g) % 原图像    
end 

if use(3)
    % 分别用函数flipdim和函数imresize实现任意图像的镜像变换和大小缩放变换
    F1 = imread('lena.jpg'); %512 512;
    [len,wid,layer] = size(F1);
    figure, 
    subplot(2,2,1), imshow(F1); title('origin');
    size(F1)

    F2 = imresize(F1,[len/2, wid/2]);
    subplot(2,2,2), imshow(F2), title('len/2 wid/2');
    size(F2)

    F3 = imresize(F1,50);
    subplot(2,2,3), imshow(F3), title('large 50');
    size(F3)

    F4 = imresize(F1,0.1);
    subplot(2,2,4), imshow(F4), title('small 0.8');
    size(F4)

    figure, 
    subplot(2,2,1), imshow(F1),title('origin');

    F5 = flip(F1);
    subplot(2,2,2), imshow(F5),title('flip 1');

    F6 = flip(F1,2);
    subplot(2,2,3), imshow(F6),title('flip 2');

    F7 = flip(F5,2);
    subplot(2,2,4), imshow(F7),title('flip 1 2');

end