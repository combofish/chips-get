clear, clc
close all
% 基于全局阈值的图像分割实现

a = [90 130 150];
I0 = imread('cameraman.tif');
[sa,sb] = size(I0);
imshow(I0), title('origin image');
for k = 1:3
    I = I0;
    for i = 1:sa
        for j = 1:sb
            if double(I(i,j)) > a(k)
                I(i,j) = 255;
            else 
                I(i,j) = 0;
            end
        end
    end
    figure(k+1),imshow(I),title(['threshold value a = ' num2str(a(k))]);
end

