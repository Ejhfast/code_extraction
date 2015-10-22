# cStringIO.StringO fails to save uploaded file stream when file is smaller than 1kByte
with open('./tmp/'+theFile.filename, "w") as f:
    f.write(theFile.file.getvalue())
