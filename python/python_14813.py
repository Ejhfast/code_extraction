# python using pickled objects with sqlite
cursor.execute('INSERT INTO sometable VALUES (?, ?)', (id, pickle.dumps(menuOb))
