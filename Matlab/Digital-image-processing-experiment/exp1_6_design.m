clear,clc
close all
% 程序设计部分实验
choose = [0,0,0,1,0];

if (choose(1))
    % 对灰度图像、真彩色图像实现读取、显示和保存
    i1 = imread('rice.png');
    imwrite(i1,'new_rice.png');
    figure, imshow(i1), title('black-and-white clolor image');

    load clown
    imwrite(X,map,'clown.bmp');
    [i2,map] = imread('clown.bmp');
    figure, imshow(i1,map), title('index color image');

    i3 = imread('peppers.png');
    imwrite(i3,'new_peppers.png');
    figure, imshow(i3), title('true color image');
end

if choose(3)
    % 通过图像点运算减弱图像对比度
    i5 = imread('rice.png');
    figure, imshow(i5), title('黑白原始图像')
    I5 = double(i5);
    J = I5 * 0.8 - 40;
    I5 = uint8(J);
    figure, imshow(I5), title('对比度减弱后的图像');
end

if choose(4)
    % 分别将索引图像转换为灰度图像和二值图像，并将灰度图像转换为索引色图像
    load clown
    figure, imshow(X,map), title('index color iamge');

    % ind2gray
    % rgbimg = ind2rgb(X,map);
    % grayimg = rgb2gray(rgbimg);
    grayimg = ind2gray(X,map);
    figure, imshow(grayimg), title('index image to gray image');

    % ind2bw
    bw = im2bw(X,map);
    figure, imshow(bw), title('index image to binary image');

    % gray2ind
    [grayimg2,gray_map] = gray2ind(grayimg);
    figure, imshow(grayimg2,gray_map), title('gray iamge to index image');
end 

if 0
    i6 = imread('lena.jpg');
    figure, imshow(i6), title('彩色图像');

    i7 = imread('rice.png');
    figure, imshow(i7), title('背景图像');

    % i8 = imadd(i7,i6,'uint16');
    % i8 = i7 + i6;
    % figure, imshow(i8,[]), title('组合图像');
end 