# filtering time range in datetime field in sqlalchemy
session.query(TableName).filter(func.convert(func.VARCHAR(8), TableName.datetimefield, 8) &gt;= datetime.time(0,0)).all()
