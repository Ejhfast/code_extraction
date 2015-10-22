# How do you do a datetime based query using SQLite in Python?
c.execute('''select modified from changes where modified &gt; ?''', (last_run,))
