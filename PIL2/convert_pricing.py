from PIL import Image

for x in range(5, 16+1):
    filename = str(x) + ".jpg"
    new_filename_left = "pricing-left" + str(x) + "-cropped.jpg"
    new_filename_right = "pricing-right" + str(x) + "-cropped.jpg"
    
    img = Image.open(filename)
    img2_left = img.crop((75,256, 580,772))
    img2_left.save(new_filename_left)

    img2_right = img.crop((702,264, 1212,777))
    img2_right.save(new_filename_right)

    print "success cropping: " + filename