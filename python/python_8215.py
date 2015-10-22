# Display 2D array from OpenCV in Matplotlib.pyplot.imshow()
def cv2numpy(cvarr, the_type):
  a = np.asarray(cv.GetMat(cvarr), dtype=the_type)
  return a
