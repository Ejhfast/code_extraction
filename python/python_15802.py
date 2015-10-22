# Don't want to create a new database if it doesn't already exists
import os
if not os.path.exists('abc.db'):
    conn = sqlite3.connect('abc.db')
