# Querying a many-to-many relationship in SQLAlchemy
.filter(Blog.keywords.any(Keyword.name.in_(['keyword1', 'keyword2', ...])))
