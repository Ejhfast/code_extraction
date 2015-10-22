# Can't compare and print SQL result in Python
cur.execute("SELECT id FROM files WHERE track_title='re.mp3';")
track_id = cur.fetchone()[0]
