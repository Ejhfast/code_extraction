# how to use sqlalchemy for sql?
for model, category in self.current_session.query(Model, Category).join(Category).distinct():
    print model.category_id, category.name
