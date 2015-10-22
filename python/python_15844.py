# SQLite insert statement failing silently using Flask
g.db.execute('insert into photos (is_favorite, galleries_id, filename) values (?, ?, ?)', [is_favorite, galleries_id, filename])
g.db.commit()
