# Uploaded image is broken after writing to file
img = request.files['imugen']
filename = secure_filename(img.filename)
img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
