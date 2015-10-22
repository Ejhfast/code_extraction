# Can an uploaded image be loaded directly by cv2?
img = cv2.imdecode(numpy.fromstring(request.files['file'].read(), numpy.uint8), cv2.CV_LOAD_IMAGE_UNCHANGED)
