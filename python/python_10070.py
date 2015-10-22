# Inserting multiple items into DB error
g.db.execute('insert into images(fileName, fileTitle, file_height, file_width, file_size) values (?,?,?,?,?)', (filename, request.form['title'], fileMetaData['height'], fileMetaData['width'], fileMetaData['fileSize']))
