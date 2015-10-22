# SQLAlchemy. How to order on many to many relationship?
sections = db.relationship("NoteSection",
            secondary=NoteTypeToSectionMap.__table__,
            order_by=NoteTypeToSectionMap.__table__.c.position)
