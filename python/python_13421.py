# New to Python Opencv: Motion Tracking using webcam Thresholding/dilate
retvel, t_minus_thresh = cv2.threshold(t_minus, 0, 255, cv2.THRESH_OTSU)
t_minus_dilate = cv2.dilate(t_minus_thresh, es)
