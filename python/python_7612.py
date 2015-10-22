# escaping sqlite results
c.execute('INSERT INTO documents VALUES (?, ?)', (somekey, buffer(yourstring)))
