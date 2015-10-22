# SQLAlchemy is Throwing an IntegrityError due to a DBSession.add()
SELECT setval('heroes_id_seq', MAX(id)) FROM heroes;
