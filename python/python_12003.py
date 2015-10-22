# django cloudinary upload remote image via url - invalid file name
cimage = cloudinary.uploader.upload(image.encode('utf-8'), public_id = 'img_'+request.user.__str__()+"_"+title, format='jpg')
