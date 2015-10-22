# Can only define secondary relationship using association table object but not name
notes = relationship(u'Note', secondary='MySchema.Documented', backref='documents')
