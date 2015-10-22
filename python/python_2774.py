# What is the best way to write the contents of a StringIO to a file?
buf.seek(0)
shutil.copyfileobj(buf, fd)
