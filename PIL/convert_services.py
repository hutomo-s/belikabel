from PIL import Image

'''
img = Image.open("flowers.jpg")
img2 = img.crop((175, 125, 1050, 790))
img2.save("img2.jpg")
'''

top = 175
left = 125
right = 1050
bottom = 790

for x in range(1, 16+1):
    filename = str(x) + ".jpg"
    new_filename = "services-" + str(x) + "-cropped.jpg"
    
    img = Image.open(filename)
    img2 = img.crop((top, left, right, bottom))
    img2.save(new_filename)

    print "success cropping: " + new_filename