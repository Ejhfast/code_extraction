# In Python, Python Image Library 1.1.6, how can I expand the canvas without resizing?
newImage = Image.new(mode, (newWidth,newHeight))
newImage.paste(srcImage, (x1,y1,x1+oldWidth,y1+oldHeight))
