# How to alter column type from character varying to integer using sqlalchemy-migrate
def downgrade(migrate_engine):
    # ALTER TABLE courses ALTER COLUMN number SET DATA TYPE integer;
    migrate_engine.execute('ALTER TABLE courses ALTER COLUMN number TYPE INTEGER USING number::numeric')
