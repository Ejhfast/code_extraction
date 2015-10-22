# Python/OpenCV webcam movement backwards
rval, frame = webcam.read()
frame = cv2.flip(frame,1)
