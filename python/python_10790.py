# Python: ValueError: unsupported format character ''' (0x27) at index 1
"SELECT fileid FROM files WHERE description LIKE '%%%s%%' OR filename LIKE '%%%s%%' OR uploader LIKE '%%%s%%' ORDER BY fileid DESC" % (search, search, search)
