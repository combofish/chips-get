from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('for_learn.jpeg').convert('L'))
im_blur_5 = filters.gaussian_filter(im,5)
im_blur_10 = filters.gaussian_filter(im,10)

# Image.fromarray(im_blur_5).save('./photo/im_blur_5.jpg')
# Image.fromarray(im_blur_10).save('./photo/im_blur_10.jpg')
