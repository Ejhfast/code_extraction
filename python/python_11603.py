# 'None' is Unicode and not NoneType in python sqlite3
conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
