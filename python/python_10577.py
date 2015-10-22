# rotating only a part of the image in python
inlay = img.crop((x1,y1,x2,y2)).rotate(90)
img.paste(inlay, (x1,y1,x2,y2))
