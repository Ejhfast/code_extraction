# sqlalchemy not deleting rows on error
if key_id:
    conn.execute("DELETE FROM temporary_data_key WHERE key='{0}'".format(guid))
