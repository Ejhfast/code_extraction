# How to actually upload a file using Flask WTF FileField
myFile = secure_filename(form.fileName.file.filename)
    form.fileName.file.save(PATH+myFile)
