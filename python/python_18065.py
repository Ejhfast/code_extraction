# Can I save a text file in python without closing it?
file.flush()
# typically the above line would do. however this is used to ensure that the file is written
os.fsync()
