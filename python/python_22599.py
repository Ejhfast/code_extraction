# django daemon fails to read database updates
def reset_database_connection():
    from django import db
    db.close_connection()
