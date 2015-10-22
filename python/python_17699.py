# NDB query returns zero results. Datastore shows the result
cnt = Description.query(ancestor=ExamineKey).filter(Description.uuid == d_id).count()
