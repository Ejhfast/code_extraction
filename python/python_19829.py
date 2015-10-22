# sqlite3 read-only on a file system that doesn't support locking
db = sqlite3.connect('file:/path/to/database?mode=ro', uri=True)
