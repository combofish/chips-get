close all,
clear clc

expChoose = [1 0 0];
% expChoose = [1 1 1]

% 计算图�?的矩形度
if expChoose(1)
    % 图像周长和面积的计算方法，请熟悉并掌握，下面请计算图像的矩形度
    % img_dst = imread('coins.png');
    %img_dst = imread('hands1-mask.png');
    img_dst = imread('circles.png');
    figure(), imshow(img_dst); title('coins.png');

    % img_dst = im2bw(img_dst);
    % figure(), imshow(img_dst); title('bw coins.png');

    [x,y] = size(img_dst)
    BW = bwperim(img_dst, 8);
    figure(), imshow(BW); title('BW title.png');

    A = bwarea(img_dst)
    
    ed = edge(img_dst);
    figure(), imshow(ed); title('edge title.png');
    
    L = bwlabel(BW);
    L1 = bwlabel(ed);
    Ar = zeros(1,max(L(:)));
    perimeter = zeros(1,max(L(:)));
    metric = zeros(1,max(L(:)));
    Pwl = zeros(1,max(L(:)));
    
    tmp = zeros(1,max(L(:)));
    Pr = tmp;
    Amer = tmp;
    
    for i = 1:max(L(:))
        Ar(i) = sum(BW(L == i));
        perimeter(i) = sum(ed(L == i));
        metric(i) = 4 * pi * Ar(i) / perimeter(i) ^ 2;
        [y,x] = find(L==i);
        x0 = min(x(:));
        x1 = max(x(:));
        y0 = min(y(:));
        y1 = max(y(:));
        hold on 
        rectangle('Position', [x0,y0,x1-x0,y1-y0],'edgeColor','g','LineWidth',1);
        if x1-x0 >= y1 - y0
            Pwl(i) = (x1 - x0) / (y1 - y0);
        else 
            Pwl(i) =  (y1 - y0) / (x1 - x0);
        end 
        Pr(i) = Ar(i) / ((y1 - y0) * ( x1 -x0));
        Amer(i) = (y1-y0) * (x1 -x0);
    end         

    Ar
    perimeter
    metric
    Pwl
    Amer
    Pr
    A / Amer(1)
    
end

% 计算图�?特�?中相关度和对比度
if expChoose(2)
    % 请计算图像特征中相关度和对比度
    img_dst = imread('coins.png');
    glcms = graycomatrix(img_dst);imshow(img_dst);
    stats = graycoprops(glcms,{'correlation', 'contrast'});
    correlation = [stats.Correlation]
    contrast = [ stats.Contrast]
end 


% 计算图中二值图�?的欧拉数
if expChoose(3)
    % 计算图中二值图像的欧拉数
    img_dst = imread('circles.png');
    figure()
    imshow(img_dst); title('circles.png');
    eul1 = bweuler(img_dst,4)
    eul2 = bweuler(img_dst,8)
end




