# OpenCV camera calibration, can not control distortion constants
retval,camera_matrix,dist_coefs,rvecs,tvecs = cv2.calibrateCamera([obj_points],[img_points],size,camera_matrix,dist_coefs,flags=cv2.CALIB_USE_INTRINSIC_GUESS + cv2.CALIB_FIX_K3)
