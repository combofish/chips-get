clear, clc
close all

choose = [0,0,1]

if choose(1)
    % 计算图像的圆形度
    img_dst = imread('coins.png');
    img_dst = im2bw(img_dst);
    [x,y] = size(img_dst);
    BW = bwperim(img_dst, 8);
    P1 = 0;
    P2 = 0;
    Ny = 0;
    for i = 1:x
        for j = 1:y
            if (BW(i,j) > 0)
                P2 = j;
                if ((P2 - P1) == 1) 
                    Ny = Ny + 1;
                end 
                P1 = P2;
            end 
        end 
    end 
    P1 = 0;
    P2 = 0;
    Nx = 0;
    for j = 1:y
        for i = 1:x
            if (BW(i,j) > 0)
                P2 = i;
                if ((P2 - P1) == 1)
                    Nx = Nx + 1;
                end 
                P1 = P2;
            end 
        end 
    end 
    
    SN = sum(sum(BW));
    Nd = SN - Nx - Ny;
    L = sqrt(2) * Nd + Nx +Ny;
    A = bwarea(img_dst);;
    C = (L *L) / ( 4*pi*A)
end

if choose(2)
    % 图像特征分析中，能量、相关度、对比度、同质性是四个重要信息，以其中能量为例，计算图像特征中能量信息
    figure()
    img_dst = imread('coins.png');
    imshow(img_dst), title('coins.png')
    glcms = graycomatrix(img_dst);
    stats = graycoprops(glcms,'Energy');
    con = [stats.Energy]
end 

if choose(3)
    % 计算图像的质心坐标
    img_dst = imread('lena.jpg');
    figure()
    m = logical(img_dst);
    n = regionprops(m, 'centroid');
    centroids = cat(1, n.Centroid);
    imshow(img_dst);
    title('The center of mass coordinates of the image');
    hold on
    plot(centroids(:,1), centroids(:,2), 'r*')
    centroids = centroids(1:2);
    [len,wid,x] = size(img_dst);
    len, wid, centroids
end

