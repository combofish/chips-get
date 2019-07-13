from PIL import Image
from numpy import *

im = array(Image.open('for_learn.jpeg'))
print(im.shape,im.dtype)

im = array(Image.open('for_learn.jpeg').convert('L'),'f')
print(im.shape,im.dtype)

im2 = 255 - im
im3 = (100.0/255) * im + 100
im4 = 255.0 * ( im/255.0)**2

## error
# im2.save('im1.jpg')
# im3.save('im3.jpg')
# im4.save('im4.jpg')

pil_im = Image.fromarray(im)
pil_im2 = Image.fromarray(uint8(im2))
pil_im3 = Image.fromarray(uint8(im3))
pil_im4 = Image.fromarray(uint8(im4))

# pil_im2.save('im2.jpg')
# pil_im3.save('im3.jpg')
# pil_im4.save('im4.jpg')

## resize
def imresize(im,sz):
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

im5 = imresize(im4,(200,200))
# Image.fromarray(im5).save('im5.jpg')

