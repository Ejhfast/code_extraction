# SQLAlchemy relationship cascade deletion
show = db.relationship('Show',
                           backref=db.backref('episodes', cascade="all, delete-orphan"),
                           lazy='joined')
