# Load blob image data into QPixmap
image_data = get_image_data_from_blob()
 qimg = QtGui.QImage.fromData(image_data)
 pixmap = QtGui.QPixmap.fromImage(qimg)
