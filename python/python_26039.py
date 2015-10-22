# Select attributes from different joined tables with Flask and SQLAlchemy
q = db.session.query(Phrase.content, Meaning.content).join(Meaning).all()
