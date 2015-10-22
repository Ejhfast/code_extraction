# SQLAlchemy subquery - average of sums
sums = session.query(func.sum(Irterm.n).label('a1')).group_by(Irterm.item_id)
average = session.query(func.avg(sums.subquery().columns.a1)).scalar()
