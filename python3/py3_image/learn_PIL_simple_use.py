from PIL import Image

pil_im = Image.open('./for_learn.jpeg')
pil_im_L = pil_im.convert('L')  # 转换为灰度图像
pil_im_small = pil_im.thumbnail((128,128))
out = pil_im.resize((128,128))
out1 = pil_im.rotate(45)

box = (100,100,400,400)
region = pil_im.crop(box)

# pil_im_L.save('photo_L.jpg')
# error
# pil_im_small.save('photo_small.jpg')
# end

#pil_im.save('small.jpg')
# region.save('region.jpg')

out.save('out.jpg')
out1.save('out1.jpg')
