# what is flask-sqlalchemy where in clause query syntax?
result = db_session.query(table_1).filter(table_1.id.in_((1,2,3,5))).all()
