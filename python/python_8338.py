# SQLAlchemy equivalent of Django ORM's relationship-spanning filter
session.query(model.Entry).join((model.Blog, model.Entry.blogid==model.Blog.id)).filter(model.Blog.name=='Beatles Blog').all()
