from PIL import Image
from pylab import *

im = array(Image.open('for_learn.jpeg'))

imshow(im)

x = [100,100,400,400]
y = [200,500,200,500]

plot(x,y,'r*')
plot(x[:2],y[:2])
title('Plotting: "for_learn.jpeg"')
show()
axis('off')


im2 = array(Image.open('for_learn.jpeg').convert('L'))
figure()
gray()
contour(im2, origin='image')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
show()

