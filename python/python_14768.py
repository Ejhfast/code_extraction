# SQLAlchemy: about self referential relation (error: no attribute '_sa_instance_state')
parent=DBSession.query(KW).filter(KW.name==parentName).first()
