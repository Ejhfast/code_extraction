# ORM query with or statement
User.query.filter(User.id.in_([1, 5, 12, 4]))
