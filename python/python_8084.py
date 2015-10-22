# sqlalchemy: and_ and the evaluation of date function in clause list
terms = [create_time&lt;=DateTime('2012-01-01')]
records = DBSession.query(myrecords).filter(and_(*terms))
