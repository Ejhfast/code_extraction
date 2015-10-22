# Irreversible migrations in Alembic
def downgrade():
    raise Exception("Irreversible migration")
