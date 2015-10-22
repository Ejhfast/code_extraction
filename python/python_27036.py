# SQLAlchemy ORM conversion to pandas DataFrame
df = pd.read_sql(query.statement, query.session.bind)
