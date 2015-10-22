# Find image inside another in SimpleCV
diff = cv2.matchTemplate(img1, img2, cv2.TM_CCORR_NORMED)
x, y = np.unravel_index(np.argmax(diff), diff.shape)
