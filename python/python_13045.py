# sqlalchemy: distinct only on one column
session.query(func.max(Table.title), Table.slug).group_by(Table.slug).all()
