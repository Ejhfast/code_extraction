# How to get dct of an image in python using opencv
imf = np.float32(imgcv1)/255.0  # float conversion/scale
dst = cv2.dct(imf)           # the dct
imgcv1 = np.uint8(dst)*255.0    # convert back
