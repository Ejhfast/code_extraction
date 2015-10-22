# Python - How to save a list as an image?
new_img = Image.new("L", (NEW_X_SIZE, NEW_Y_SIZE), "white")
new_img.putdata(new_img_list)
new_img.save('out.tif')
