# How do I properly construct an UPDATE statement that references an attached database table?
c.execute('''UPDATE table_b SET number = 1 WHERE table_b.word IN (SELECT string FROM table_a)''')
