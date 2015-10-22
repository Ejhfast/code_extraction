# SQLAlchemy with PostgresSQL and Full Text Search
create_index = DDL("CREATE INDEX idx_content ON pep USING gin(to_tsvector('english', content));")
event.listen(Pep.__table__, 'after_create', create_index.execute_if(dialect='postgresql'))
