# How to protect text when doing INSERT using MySQLdb
cursor.execute (
    "INSERT INTO text (text_key, language_id, text) VALUES (%s, %s, %s)",
    (key, language_id, text))
