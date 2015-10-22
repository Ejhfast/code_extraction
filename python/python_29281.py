# OpenCV 3 in Python 2.7 gives error while using Brute-Force Matcher
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)
plt.imshow(img3),plt.show()
