# create dictionary based on filter in sqlalchemy
by_name = {g.name: g.users for g in Group.query.options(db.joinedload(Group.users))}
