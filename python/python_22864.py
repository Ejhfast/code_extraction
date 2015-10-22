# How do I connect to Postgresql using SSL from SqlAchemy+pg8000?
db = create_engine('postgresql+pg8000://user:pass@hostname/dbname', connect_args={'sslmode':'require'}, echo=True).connect()
