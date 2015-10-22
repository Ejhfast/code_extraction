# OpenCV- Python: How Do I split an Image in a grid?
img = cv2.imread('sachin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
roi_gray = gray[y:y+h, x:x+w]
