# sqlalchemy mysql connections not closing on flask api
def close(self):
    self.session.close()
    self.db.dispose()
