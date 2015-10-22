# mysql-python fetchrow brings: TypeError: 'long' object is not callable
cursor = self.__db.cursor()
cursor.execute('select * from UserConfirm where Benutzer = \'' + ds + '\'')
return cursor.fetchone()
