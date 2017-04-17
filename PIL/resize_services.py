from PIL import Image
from resizeimage import resizeimage

for x in range(1, 16+1):

    filename = "services-" + str(x) + "-cropped.jpg"
    new_filename = "serv-" + str(x) + ".jpg"

    fd_img = open(filename, 'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_height(img, 550)
    img.save(new_filename, img.format)
    fd_img.close()