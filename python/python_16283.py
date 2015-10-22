# SQLAlchemy DateTime to datetime.datetime
candidates = session.query(User).filter((User.time - datetime.datetime.utcnow()) &gt; datetime.timedelta(weeks=8))
