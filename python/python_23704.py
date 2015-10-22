# opencv2: bicubic interpolation while resizing image
img = cv2.imread('source to image here')
cv2.resize(img,fx=scaleX,fy=scaleY, interpolation = cv2.INTER_CUBIC)
