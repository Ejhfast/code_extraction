# Reflecting Oracle Global Temp Tables Using Pythons SQLAlchemy
Test = [sqlalchemy.Table(t, meta, autoload=True, autoload_with=_engine, schema=_schema)
        for t in schedule.tables.values]
