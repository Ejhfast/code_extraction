# How to create thumbnails using opencv-python?
maxsize = (1024,1024)
imRes = cv2.resize(im,maxsize,interpolation=cv2.CV_INTER_AREA)
