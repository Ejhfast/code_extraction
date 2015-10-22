# openCV: Sobel edge detection gives me assertion error
src = cv.LoadImageM('src.png', cv.CV_LOAD_IMAGE_GRAYSCALE)
dest = cv.CreateMat(src.height, src.width, cv.CV_16S)
cv.Sobel(src, dest, 1, 1)
