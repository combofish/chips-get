from PIL import Image
from numpy import *

im_man = array(Image.open('man.jpg').convert('L'),'f')
im_j = array(Image.open('j.jpg').convert('L'),'f')
im_t = array(Image.open('t.jpg').convert('L'),'f')

pil_man = Image.fromarray(uint8(im_man))
pil_man.save('conver/im_man.jpg')

Image.fromarray(uint8(im_j)).save('conver/im_j.jpg')
Image.fromarray(uint8(im_t)).save('conver/im_t.jpg')

