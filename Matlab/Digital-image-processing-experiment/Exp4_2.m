I=imread('coins.png');
subplot(2,2,1),imshow(I),title('origin image');
subplot(2,2,2);
imhist(I);%直方图
title('histogram');
u=imhist(I);
for i=1:256
 m(i)=0;
end
j=0;
%求所有峰值灰度级
for i=1:254
 for b=i+1
 for c=b+1
 if u(i)<u(b)&u(b)>u(c)
 j=j+1;
 m(j)=b;
 end
 end
 end
end
%求峰值中最小灰度级
w=m(1); 
for k0=2:j
 if u(m(k0))<u(w)
 w=m(k0);
 end
end
%峰值中最大灰度级
p=m(1);
for k=2:j
 if u(m(k))>u(p)
 p=m(k);
 end
end
%求出与最大峰值相邻的峰值灰度级
l=u(w);
for k1=1:j
 if u(m(k1))>l;
 x=m(k1)-p;
 if(abs(x)>30)
 l=u(m(k1));q=m(k1);
 end
 end
end
if p>q
 k2=q;k3=p;
else k2=p;k3=q;
end
%求出直方图谷底灰度值
l1=u(k2);
for n1=(k2+1):(k3-1)
 if l1>u(n1)
 l1=u(n1);p1=n1;
 end
end
F=im2bw(I,p1/255);%二值化
subplot(2,2,3),imshow(F),title('binary image');