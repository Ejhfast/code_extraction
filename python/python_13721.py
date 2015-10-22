# Python error when searching sqlite3 database
query = raw_input('Search for a title:')
query = '%' + query + '%'
cursor.execute("SELECT * FROM nerd WHERE title LIKE ?", (query,))
