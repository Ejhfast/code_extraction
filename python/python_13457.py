# SQLAlchemy: Dynamically loaded backreference to another module
class Post(Model):
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('posts', lazy='dynamic'))
