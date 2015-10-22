# Is sqlite fast enough for it to replace pre-loading stuff into memory?
conn.execute("""PRAGMA cache_size = 4000""")  # 4 Mb
