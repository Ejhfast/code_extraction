# Converting a StringIO object to a Django ImageFile
pi = ProductImage(product=product)
pi.source_image.save(image_name, ContentFile(image_file.read()))
pi.save()
