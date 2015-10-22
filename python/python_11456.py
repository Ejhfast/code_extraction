# How to add object to many-to-one relationship in SQLAlchemy?
def add_comment(self, comment):
    comment = ItemTypeComment()
    self.comments.append(comment)
