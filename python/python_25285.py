# Where does connect_to_database() comes from?
def connect_to_database():
    return sqlite3.connect(DATABASE)
