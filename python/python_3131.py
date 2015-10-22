# How to query a table, in sqlalchemy
Session.query(questions).filter(questions.c.user_id==123).one()
