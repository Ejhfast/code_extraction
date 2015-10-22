# continuous drawing (opencv)
cv2.line(img,(ix,iy),(x,y),(0,0,255),10) # draw line between former and present pixel
ix=x # save former x coordinate
iy=y # save former y coordinate
